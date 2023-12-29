import ControlButtons from './components/ControlButtons';
import SearchBar from './components/SearchBar';
import { useState } from "react";

import './App.css';
import logo from "./images/logo_1.jpg";
// import animation from "./images/stream.jpg";




function App() {

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
      <ControlButtons selected={selected} setSelected={setSelected}/>
      <div className="grid-item grid-item-5">animation</div>
    </div>
  );
}

export default App;