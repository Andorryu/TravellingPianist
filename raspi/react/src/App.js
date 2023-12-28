import ControlButton from './components/ControlButton';
import SearchBar from './components/SearchBar';
import SearchResult from './components/SearchResult';
import { useReducer, useState } from "react";

import './App.css';
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
      <div className="grid-item grid-item-1">
        <img src={logo} alt="Traveling Pianst Logo"></img>
      </div>
      <div className="grid-item grid-item-2">
        <SearchBar />
        <SearchResult />
      </div>
      <div className="grid-item grid-item-3">selcted song</div>
      <div className="grid-item grid-item-4">
        {/* <ControlButton label="Upload" dispatch={dispatch} />
        <ControlButton label="Play" dispatch={dispatch} />
        <ControlButton label="Reset" dispatch={dispatch} /> */}
        buttons
      </div>
      <div className="grid-item grid-item-5">animation</div>
    </div>
  );
}

export default App;