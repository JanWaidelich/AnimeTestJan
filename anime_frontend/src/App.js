// anime_frontend/src/App.js
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [animeList, setAnimeList] = useState([]);

  useEffect(() => {
    // Adjust this URL if using Docker Compose:
    //    "http://anime_backend:8000/anime-list"
    const url = "http://localhost:8000/anime-list";
    
    axios.get(url)
      .then(response => {
        console.log("GET /anime-list response.data =>", response.data);
        // Expecting response.data = { "anime": [...] }
        if (response.data.anime) {
          setAnimeList(response.data.anime);
        } else {
          console.error("No 'anime' key in response:", response.data);
        }
      })
      .catch(error => {
        console.error("GET /anime-list error:", error);
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Anime List (GET Request Example)</h1>
      <ul>
        {animeList.map(a => (
          <li key={a.id}>
            {a.title}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
