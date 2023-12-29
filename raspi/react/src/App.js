// import ControlButton from './components/ControlButton';
import SearchBar from './components/SearchBar';
import { useReducer, useState } from "react";

import './App.css';
import logo from "./images/logo_1.jpg";
import animation from "./images/stream.jpg";


export const ACTIONS = {
  // for button uses?
}

function App() {
  // remove for reducer soon
  const dispatch = [];

  const [selected, setSelected] = useState("");

  

  return (
    <div className="grid-container">
      <div className="grid-item grid-item-1">
        <img src={logo} alt="Traveling Pianst Logo"></img>
      </div>
      <SearchBar setSelected={setSelected} />
      <div className="grid-item grid-item-3">
        <div>{selected}</div>
        <div>uploaded check/X</div>
      </div>
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