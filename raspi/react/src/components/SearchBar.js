import "./SearchBar.css";
import { useState } from "react";

export default function SearchBar({setSelected}) {

    const [input, setInput] = useState('');
    const [results, setResults] = useState([]);

    const handleChange = (value) => {
        setInput(value)
        if (value !== "") {
            fetchData(value);
        } else {
            setResults([]);
        }
    }

    const handleSelectButton = (selectTerm) => {
        setSelected(selectTerm);
    }

    const handleSelectDropdown = (dropdownTerm) => {
        setInput(dropdownTerm);
    }

    const fetchData = (value) => {
        const requestOptions = {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({"search": value})
        }; 
    
    
        fetch("http://127.0.0.1:5000/search", requestOptions)
        .then((response) => response.json())
        .then((json) => {
            // console.log(json);
            setResults(json);
        });
      }

    
    return (
        <div className="grid-item grid-item-2">
            <div className="search-inner">
                <input type='text' value={input} onChange={(e) => handleChange(e.target.value)} />
                <button onClick={() => handleSelectButton(input)}>Select</button>
            </div>
            <div className="dropdown">
                {   
                    results.map((result, id) => {
                        return <div onClick={() => handleSelectDropdown(result.name)} key={id}>{result.name}</div>
                    })
                }
            </div>
        </div>
    )
}
