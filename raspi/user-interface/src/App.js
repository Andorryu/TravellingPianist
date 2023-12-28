import ControlButton from './components/ControlButton';
import { SearchBar } from "./components/SearchBar";
import { SearchResultsList } from "./components/SearchResultsList";
import { useReducer, useState } from "react";

import './styles.css';
import logo from "./images/logo_1.jpg";
import animation from "./images/stream.jpg";



export const ACTIONS = {

}



function App() {
  // remove for reducer soon
  const dispatch = [];

  const [results, setResults] = useState([]);

  return (
    <div className="grid-container">
      <div className="logo grid-item-1">
        <img scr={animation} alt="Traveling Piano Logo" />
      </div>
      <div className="grid-item grid-item-2">
        <SearchBar setResults={setResults} />
        {results && results.length > 0 && <SearchResultsList results={results} />}
      </div>
      <div className="grid-item grid-item-3">selcted song</div>
      <div className="grid-item grid-item-4">
        <ControlButton label="Upload" dispatch={dispatch} />
        <ControlButton label="Play" dispatch={dispatch} />
        <ControlButton label="Reset" dispatch={dispatch} />
      </div>
      <div className="grid-item grid-item-5">
        {/* <img src={animation} /> */}
      </div>
    </div>
  );
}

export default App;