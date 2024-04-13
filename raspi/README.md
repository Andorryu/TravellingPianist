import { useState, useEffect } from "react";
import "./ControlButtons.css";

export default function ControlButtons({selected, setSelected}) {

    const blankStyle = {
        backgroundColor: "grey",
    };

    const trueStyle = {
        backgroundColor: "green",
    };

    const falseStyle = {
        backgroundColor: "red",
    };

    const [uploadstatus, setUploadstatus] = useState("False");
    const [uploadstyle, setUploadstyle] = useState(falseStyle);
    const [playstatus, setPlaystatus] = useState("False");
    const [playstyle, setPlaystyle] = useState(falseStyle);
    const [resetstatus, setResetstatus] = useState("False");
    const [resetstyle, setResetstyle] = useState(falseStyle);


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
    useEffect( () => {
        if (uploadstatus === "True") {
            // set upload button to green
            setUploadstyle(() => (trueStyle));
    
            // reset pins and stop current song
            fetch("http://127.0.0.1:5000/play", {
                method: 'PUT',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({})
            });
    
            setResetstatus("False");
            setResetstyle(() => (falseStyle));
    
            setPlaystatus("False");
            setPlaystyle(() => (falseStyle));

        } else {
            console.log("FALSE upload response!");
            setUploadstyle(() => (blankStyle));

        }
    }, [uploadstatus]);

    
    const fetchPlay = () => {
        fetch("http://127.0.0.1:5000/play")
        .then((response) => response.json())
        .then((json) => {
            // console.log(json.state);
            setPlaystatus(json.state);
        });
    }
    useEffect( () => {
        if (playstatus === "True") {

            setPlaystyle(() => (trueStyle));
    
            // maybe implement timer or something similar?
            // TIMER HERE

            setUploadstatus("True");
            setUploadstyle(() => (trueStyle));
   
            setResetstatus("False");
            setResetstyle(() => (falseStyle));
    

        } else {
            console.log("FALSE play response!");
            setPlaystyle(() => (blankStyle));
        }
    }, [playstatus]);
    
    const handlePlay = () => {
        // upload must be true to play
        if (uploadstatus === "True") {
            fetchPlay();
        }
    }


    const fetchReset = () => {
        const requestOptions = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({})
        }; 

        fetch("http://127.0.0.1:5000/play", requestOptions)
        .then((response) => response.json())
        .then((json) => {
            // console.log(json.state);
            setResetstatus(json.state);
            setSelected("");
        });
    }
    useEffect( () => {
        if (resetstatus === "True") {

            setResetstyle(() => (trueStyle));
    
            setPlaystatus("False");
            setPlaystyle(() => (falseStyle));
    
            setUploadstatus("False");
            setUploadstyle(() => (falseStyle));
            
        } else {
            console.log("FALSE reset response!");
            setResetstyle(() => (blankStyle));  
        }
    }, [resetstatus]);
    

    return (
        <div className="grid-item-4">
            <div className="control-container">
                <button className="control-button" onClick={() => fetchUpload(selected)}>Upload</button>
                <div className="status-container">
                    <div className="status-label">Status</div>
                    <div className="status-upload" style={uploadstyle}>{uploadstatus}</div>
                </div>
            </div>
            <div className="control-container">
                <button className="control-button" onClick={() => handlePlay()}>Play</button>
                <div className="status-container">
                    <div className="status-label">Status</div>
                    <div className="status-play" style={playstyle}>{playstatus}</div>
                </div>
            </div>
            <div className="control-container">
                <button className="control-button" onClick={() => fetchReset()}>Reset</button>
                <div className="status-container">
                    <div className="status-label">Status</div>
                    <div className="status-reset" style={resetstyle}>{resetstatus}</div>
                </div>
            </div>
        </div>
    )
}
