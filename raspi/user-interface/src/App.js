import ControlButton from './ControlButton';
import { useReducer } from "react";

import './styles.css';
import img1 from "./images/logo_1.png";
import checkmark from "./images/checkmark.png";
import xmark from "./images/xmark.jpeg";
import animation from "./images/stream.jpg"


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
        <iframe className="iframe" src="https://musescore.org/en"></iframe>
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