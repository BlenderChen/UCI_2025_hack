import "./App.css";
import { useState, useEffect, SetStateAction } from "react";

export default function App() {
  const [suggestions, setSuggestions] = useState<string[]>([]);
  const [query, setQuery] = useState('');
  const [responseMessage, setResponseMessage] = useState(''); // Response from the Flask backend
  const [data, setData] = useState<{
    dictionary1: Record<string, string>;
    dictionary2: Record<string, string>;
    dictionary3: Record<string, string>;
  } | null>(null);
  const [firstValue, setFirstValue] = useState<string>("");
  const [secondValue, setSecondValue] = useState<string>("");
  const [thirdValue, setThirdValue] = useState<string>("");

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

  // Fetch the dictionaries from the backend
  const fetchData = async () => {
    const response = await fetch("http://127.0.0.1:5000/get_data", {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });

    const jsonData = await response.json();
    setData(jsonData); // Update the grid with the fetched dictionaries
    if (jsonData.dictionary1) {

      const firstValueFromDict = Object.values(jsonData.dictionary1)[0]; // Get the first value from dictionary1

      setFirstValue(firstValueFromDict); // Store it in the state

    }

  };

  // Handle clicks on suggestion items
  const handleSuggestionClick = (suggestion: SetStateAction<string>) => {
    setQuery(suggestion); // Populate search bar with the clicked suggestion
  };

  return (
    <div id="root">
      <h1>New Horizons</h1>

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
            .filter((item) => item.toLowerCase().includes(query.toLowerCase()))
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

      {/* Fetch and Display Dictionaries */}
      <button
        onClick={fetchData}
        style={{ margin: "20px", padding: "10px", fontSize: "16px" }}
      >
        Load Dictionaries
      </button>

      {data && (
        <div style={{ display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: "20px" }}>
          <div style={{ border: "1px solid #ccc", padding: "10px" }}>
            <h2>#1 Location</h2>
            {Object.entries(data.dictionary1).map(([key, value]) => (
              <p key={key}>
                <strong>{key}:</strong> {value}
              </p>
            ))}
            {/* Conditionally Render Image Based on the First Value */}
            {firstValue && firstValue === "value1" && (
              <div style={{ marginTop: "20px", textAlign: "center" }}>
                <img
                  src="https://a.espncdn.com/i/headshots/nba/players/full/1966.png" // Replace with your image URL
                  alt="Sample Image"
                  style={{ maxWidth: "100%" }}
                />
                <p>Image for the first dictionary's first value!</p>
        </div>
      )}
          </div>

          <div style={{ border: "1px solid #ccc", padding: "10px" }}>
            <h2>#2 Location</h2>
            {Object.entries(data.dictionary2).map(([key, value]) => (
              <p key={key}>
                <strong>{key}:</strong> {value}
              </p>
            ))}
          </div>

          <div style={{ border: "1px solid #ccc", padding: "10px" }}>
            <h2>#3 Location</h2>
            {Object.entries(data.dictionary3).map(([key, value]) => (
              <p key={key}>
                <strong>{key}:</strong> {value}
              </p>
            ))}
          </div>
        </div>
      )}

    </div>
  );
}
