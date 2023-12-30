import "./SearchBar.css";
import { useState } from "react";
import { FaSearch } from "react-icons/fa"

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
        <div className="grid-item-2">
            <div className="input-container">
                <FaSearch id="search-icon" />
                <input type='text' placeholder="Type to search..." value={input} onChange={(e) => handleChange(e.target.value)} />
            </div>
            <div className="button-container">
                <button onClick={() => handleSelectButton(input)}>Select</button>
            </div>
            <div className="results-list">
                {   
                    results.map((result, id) => {
                        return <div className="result-individual" onClick={() => handleSelectDropdown(result.name)} key={id}>{result.name}</div>
                    })
                }
            </div>
        </div>
    )
}
