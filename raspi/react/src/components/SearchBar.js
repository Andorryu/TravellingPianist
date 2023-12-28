import "./SearchBar.css";
import { FaSearch } from "react-icons/fa";
import React, { useState } from "react";


export default function SearchBar() {
    const [input, setInput] = useState("");

    const fetchData = (value) => {
        // fetch("https://jsonplaceholder.typicode.com/users")
        // .then((response) => response.json())
        // .then((json) => {
        //     console.log(json);
        // })
        fetch("http://127.0.0.1:5000/search/hotline")
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