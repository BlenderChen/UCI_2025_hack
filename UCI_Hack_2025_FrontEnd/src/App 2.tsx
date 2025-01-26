import "./App.css";
import { useState } from "react";

export default function App() {
  const [searchQuery, setSearchQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  // Function to fetch suggestions from the backend
  const fetchSuggestions = (query) => {
    fetch("http://127.0.0.1:5000/suggestion", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ query }), // Send user input as JSON
    })
      .then((response) => response.json())
      .then((data) => {
        setSuggestions(data); // Update suggestions state
      })
      .catch((error) => console.error("Error fetching suggestions:", error));
  };

  // Handle input change
  const handleInputChange = (e) => {
    const query = e.target.value;
    setSearchQuery(query);

    if (query.trim()) {
      fetchSuggestions(query); // Fetch suggestions when input changes
    } else {
      setSuggestions([]); // Clear suggestions if input is empty
    }
  };

  return (
    <div style={{ padding: "20px", maxWidth: "400px", margin: "auto" }}>
      <h1>New Horizon</h1>

      {/* Search Bar */}
      <input
        type="text"
        placeholder="Search real estate"
        value={searchQuery}
        onChange={handleInputChange}
        style={{
          width: "100%",
          padding: "10px",
          marginBottom: "5px",
          border: "1px solid #ccc",
          borderRadius: "5px",
        }}
      />

      {/* Suggestions */}
      {searchQuery && (
        <ul
          style={{
            border: "1px solid #ccc",
            borderRadius: "5px",
            maxHeight: "150px",
            overflowY: "auto",
            listStyleType: "none",
            padding: "10px",
            margin: 0,
            background: "white",
          }}
        >
          {suggestions.map((item, index) => (
            <li
              key={index}
              onClick={() => setSearchQuery(item)} // Populate search bar with the clicked suggestion
              style={{
                padding: "5px",
                cursor: "pointer",
                borderBottom: "1px solid #eee",
              }}
            >
              {item}
            </li>
          ))}
          {suggestions.length === 0 && <li>No suggestions found.</li>}
        </ul>
      )}
    </div>
  );
}
