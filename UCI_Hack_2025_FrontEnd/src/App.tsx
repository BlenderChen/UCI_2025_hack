import "./App.css";
import { useState, useEffect, SetStateAction } from "react";

export default function App() {
  { /*const [searchQuery, setSearchQuery] = useState("");*/ } 
  const [suggestions, setSuggestions] = useState<string[]>([]);
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


  useEffect(() => {
    fetch("http://127.0.0.1:5000/getsuggestions") // Replace with your backend endpoint
      .then((response) => response.json())
      .then((data) => {
        setSuggestions(data); // Assuming the backend returns an array of suggestions
      })
      .catch((error) => console.error("Error fetching suggestions:", error));
  }, []);

  function handleSuggestionClick(suggestion: SetStateAction<string>) {
    setQuery(suggestion); // Populate search bar with the clicked suggestion
  }

  return (
    <div id="root">
      <h1>Search Example</h1>

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
      {/* Suggestions */}
      {query && (
        <ul className="suggestions-list">
          {suggestions
            .filter((item) =>
              item.toLowerCase().includes(query.toLowerCase())
            )
            .map((item, index) => (
              <li
                key={index}
                onClick={() => handleSuggestionClick(item)}
                className="suggestion-item"
              >
                {item}
              </li>
            ))}
          {suggestions.filter((item) =>
            item.toLowerCase().includes(query.toLowerCase())
          ).length === 0 && <li>No suggestions found.</li>}
        </ul>
      )}
    </div>
  );

}