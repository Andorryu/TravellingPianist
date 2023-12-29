import { useState } from "react";
import "./ControlButtons.css";

export default function ControlButtons({selected, setSelected}) {

    const [uploadstatus, setUploadstatus] = useState("False");
    const [playstatus, setPlaystatus] = useState("False");
    const [resetstatus, setResetstatus] = useState("False");

    const fetchUpload = (value) => {
        const requestOptions = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({"name": value})
        }; 
    
    
        fetch("http://127.0.0.1:5000/upload", requestOptions)
        .then((response) => response.json())
        .then((json) => {
            // console.log(json.state);
            setUploadstatus(json.state);
        });
      }

    
    const fetchPlay = () => {
        fetch("http://127.0.0.1:5000/play")
        .then((response) => response.json())
        .then((json) => {
            // console.log(json.state);
            setPlaystatus(json.state);
        });
    }

    const handlePlay = () => {
        if (uploadstatus == "True") {
            fetchPlay();
            setPlaystatus("True");
        } else {
            setPlaystatus("False")
        }
    }


    const fetchReset = () => {
        fetch("http://127.0.0.1:5000/reset")
        .then((response) => response.json())
        .then((json) => {
            // console.log(json.state);
            setResetstatus(json.state);
            setSelected("");
        });
    }
    

    return (
        <div className="grid-item grid-item-4">
            <div className="upload-container">
                <button className="upload-button" onClick={() => fetchUpload(selected)}>Upload</button>
                <div className="status-label">Status</div>
                <div className="status-upload">{uploadstatus}</div>
            </div>
            <div className="play-container">
                <button className="play-button" onClick={() => handlePlay()}>Play</button>
                <div className="status-label">Status</div>
                <div className="play-upload">{playstatus}</div>
            </div>
            <div className="reset-container">
                <button className="reset-button" onClick={() => fetchReset()}>Reset</button>
                <div className="status-label">Status</div>
                <div className="status-reset">{resetstatus}</div>
            </div>
        </div>
    )
}
