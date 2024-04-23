import { useEffect, useState } from "react";
import Search from "../search";
import data from "./server";

export default function Weather() {
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(false);
  const [weatherData, setWeatherData] = useState(null);
  const key = data;

  async function fetchWeatherData(param) {
    setLoading(true);
    try {
      const response = await fetch(
        `https://api.openweathermap.org/data/2.5/weather?q=${param}&appid=${key}`
      );
      const data = await response.json();
      if (data) {
        setWeatherData(data);
        setLoading(false);
        // console.log(data);
      }
    } catch (e) {
      setLoading(false);
      console.log(e);
    }
  }

  function handleSearch() {
    // console.log(search);
    fetchWeatherData(search);
  }
  useEffect(() => {
    fetchWeatherData("tokyo");
  }, []);

  return (
    <div>
      <Search
        search={search}
        setSearch={setSearch}
        handleSearch={handleSearch}
      />
      {loading ? (
        <div className="loading">Loading</div>
      ) : (
        <div>
          <div className="city-name">
            {weatherData?.name} <span>{weatherData?.sys?.country}</span>
          </div>
          <div className="temp">{weatherData?.main?.temp}</div>
          <p className="description">
            {weatherData && weatherData.weather && weatherData.weather[0]
              ? weatherData.weather[0].description
              : ""}
          </p>
          <div className="weather-info">
            <div className="column">
              <p className="wind">{weatherData?.wind?.speed}</p>
              <p>Wind Speed</p>
            </div>
            <div className="column">
              <p className="humidity">{weatherData?.main?.humidity}</p>
              <p>Humidity</p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
