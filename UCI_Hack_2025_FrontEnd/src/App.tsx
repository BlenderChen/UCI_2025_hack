import "./App.css";
import { useState, useEffect } from "react";

export default function App() {
  { /*const [searchQuery, setSearchQuery] = useState(""); 
  const [suggestions, setSuggestions] = useState([]); */ }
  const [query, setQuery] = useState('')
  const [responseMessage, setResponseMessage] = useState(''); // Response from the Flask backend

  const handleSearchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(event.target.value);
  };
  
  const handleSearchSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    fetch(`http://127.0.0.1:5000/suggestions?query=${encodeURIComponent(query)}`)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      setResponseMessage(`Backend received: ${data.query}`);
    })
    .catch((error) => {
      console.error('Error:', error);
      setResponseMessage('Error connecting to the backend.');
    });
  };

  return (
    <div id="root">
      <h1>Search Bar Example</h1>

      {/* Search Form */}
      <form onSubmit={handleSearchSubmit}>
        <input
          type="text"
          placeholder="Enter your search query.."
          value={query}
          onChange={handleSearchChange} // Update the query as the user types
        />
        <button type="submit">Submit</button>
      </form>

      {/* Display the backend's response */}
      <p>{responseMessage}</p>
    </div>
  );





  // Fetch suggestions from the backend
  useEffect(() => {
    fetch("http://127.0.0.1:5000/suggestions") // Replace with your backend endpoint
      .then((response) => response.json())
      .then((data) => {
        setSuggestions(data); // Assuming the backend returns an array of suggestions
      })
      .catch((error) => console.error("Error fetching suggestions:", error));
  }, []);

  function handleSuggestionClick(suggestion) {
    setSearchQuery(suggestion); // Populate search bar with the clicked suggestion
  }

  return (
    <div style={{ padding: "20px", maxWidth: "400px", margin: "auto" }}>
      <h1>New Horizon</h1>

      {/* Search Bar */}
      <input
        type="text"
        placeholder="Search real estate"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
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
          {suggestions
            .filter((item) =>
              item.toLowerCase().includes(searchQuery.toLowerCase())
            )
            .map((item, index) => (
              <li
                key={index}
                onClick={() => handleSuggestionClick(item)}
                style={{
                  padding: "5px",
                  cursor: "pointer",
                  borderBottom: "1px solid #eee",
                }}
              >
                {item}
              </li>
            ))}
          {suggestions.filter((item) =>
            item.toLowerCase().includes(searchQuery.toLowerCase())
          ).length === 0 && <li>No suggestions found.</li>}
        </ul>
      )}
    </div>
  );
}
