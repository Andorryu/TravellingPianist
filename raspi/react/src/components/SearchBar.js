import "./SearchBar.css";
import { FaSearch } from "react-icons/fa";
import React, { useState } from "react";


export default function SearchBar() {
    const [input, setInput] = useState("");

    const fetchData = (value) => {
        const requestOptions = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({"search": value})
        }; 

        fetch("http://127.0.0.1:5000/search", requestOptions)
        .then((response) => response.json())
        .then((json) => {
            console.log(json);
        })
    }

    const handleChange = (value) => {
        setInput(value)
        fetchData(value)
    }

    return (
        <div className="input-wrapper">
            <FaSearch id="search-icon" />
            <input 
                placeholder="Search local library or download new..."
                value = {input}
                onChange={(e) => handleChange(e.target.value)}
            />  
        </div>
    )
}