import ControlButtons from './components/ControlButtons';
import SearchBar from './components/SearchBar';
import Animation from './components/Animation';
import { useState } from "react";

import './App.css';
import logo from "./images/logo_1.jpg";
// import animation from "./images/stream.jpg";




function App() {

  const [selected, setSelected] = useState("");

  

  return (
    <div className="grid-container">
      <div className="grid-item-1">
        <img src={logo} alt="Traveling Pianst Logo"></img>
      </div>
      <SearchBar setSelected={setSelected} />
      <div className="grid-item-3">
        <div className="selected-title">Selected Song:</div>
        <div className="selected-container">{selected}</div>
      </div>
      <ControlButtons selected={selected} setSelected={setSelected}/>
      <Animation />
      <div className="grid-item-6">&copy; TEAM PIANO</div>
    </div>
  );
}

export default App;