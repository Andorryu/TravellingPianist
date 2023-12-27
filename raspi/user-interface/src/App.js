import ControlButton from './ControlButton';
import { useReducer } from "react";

import './styles.css';
import img1 from "./images/logo_1.png";
import checkmark from "./images/checkmark.png";
import xmark from "./images/xmark.jpeg";
import animation from "./images/stream.jpg"


/////////////////////////////////////////////////////////////////////////////////////
// iframe bypass allowing for musescore click-attack defense to be disabled
customElements.define('x-frame-bypass', class extends HTMLIFrameElement {
	static get observedAttributes() {
		return ['src']
	}
	constructor () {
		super()
	}
	attributeChangedCallback () {
		this.load(this.src)
	}
	connectedCallback () {
		this.sandbox = '' + this.sandbox || 'allow-forms allow-modals allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-presentation allow-same-origin allow-scripts allow-top-navigation-by-user-activation' // all except allow-top-navigation
	}
	load (url, options) {
		if (!url || !url.startsWith('http'))
			throw new Error(`X-Frame-Bypass src ${url} does not start with http(s)://`)
		console.log('X-Frame-Bypass loading:', url)
		this.srcdoc = `
      <html>
        <head>
          <style>
          .loader {
            position: absolute;
            top: calc(50% - 25px);
            left: calc(50% - 25px);
            width: 50px;
            height: 50px;
            background-color: #333;
            border-radius: 50%;  
            animation: loader 1s infinite ease-in-out;
          }
          @keyframes loader {
            0% {
            transform: scale(0);
            }
            100% {
            transform: scale(1);
            opacity: 0;
            }
          }
          </style>
        </head>
        <body>
          <div class="loader"></div>
        </body>
      </html>`
		this.fetchProxy(url, options, 0).then(res => res.text()).then(data => {
			if (data)
				this.srcdoc = data.replace(/<head([^>]*)>/i, `<head$1>
	<base href="${url}">
	<script>
	// X-Frame-Bypass navigation event handlers
	document.addEventListener('click', e => {
		if (frameElement && document.activeElement && document.activeElement.href) {
			e.preventDefault()
			frameElement.load(document.activeElement.href)
		}
	})
	document.addEventListener('submit', e => {
		if (frameElement && document.activeElement && document.activeElement.form && document.activeElement.form.action) {
			e.preventDefault()
			if (document.activeElement.form.method === 'post')
				frameElement.load(document.activeElement.form.action, {method: 'post', body: new FormData(document.activeElement.form)})
			else
				frameElement.load(document.activeElement.form.action + '?' + new URLSearchParams(new FormData(document.activeElement.form)))
		}
	})
	</script>`)
		}).catch(e => console.error('Cannot load X-Frame-Bypass:', e))
	}
	fetchProxy (url, options, i) {
		const proxies = (options || {}).proxies || [
			'https://cors-anywhere.herokuapp.com/',
			'https://yacdn.org/proxy/',
			'https://api.codetabs.com/v1/proxy/?quest='
		]
		return fetch(proxies[i] + url, options).then(res => {
			if (!res.ok)
				throw new Error(`${res.status} ${res.statusText}`);
			return res
		}).catch(error => {
			if (i === proxies.length - 1)
				throw error
			return this.fetchProxy(url, options, i + 1)
		})
	}
}, {extends: 'iframe'})
/////////////////////////////////////////////////////////////////////////////////////

var musescore_url = "https://musescore.org/en"

export const ACTIONS = {

}

function App() {
  // remove for reducer soon
  const dispatch = [];

  // will keep track of status of download and upload
  var download_status = checkmark;
  var upload_status = xmark;
  var reset_status = xmark;

  return (
    <div className="grid-container">
      <div className="logo grid-item-1">
        <img className="logo-image" scr={img1} alt="Traveling Piano Logo" />
      </div>
      <div className="grid-item grid-item-2">
        {/* "iframe" is now a custom element rather than the traditional iframe tag */}
        <iframe is="x-frame-bypass" src={musescore_url}></iframe>
      </div>
      <div className="grid-item grid-item-3">test</div>
      <div className="grid-item grid-item-4">
        <ControlButton label="Download" dispatch={dispatch} />
        <ControlButton label="Upload" dispatch={dispatch} />
        <ControlButton label="Restart" dispatch={dispatch} />
      </div>
      <div className="grid-item grid-item-5">
        <div className="status-bar">
          <img src={download_status}/>
        </div>
        <div className="status-bar">
          <img src={upload_status}/>
        </div>
        <div className="status-bar">
          <img src={reset_status}/>
        </div>
      </div>
      <div className="grid-item grid-item-6">
        <img src={animation} />
      </div>
    </div>
  );
}

export default App;