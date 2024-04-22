import { useEffect, useState } from "react";
import Search from "../search";

export default function Weather(){
    const [search, setSearch] = useState('');
    const [loading, setLoading] = useState(false);
    const [weatherData, setWeatherData] = useState(null);

    async function fetchWeatherData(param){
        setLoading(true)
        try{
            const response = await fetch(
                `https://api.openweathermap.org/data/2.5/weather?q=${param}&appid=5e157b12a85a9c1de074d745226a415f`)
            const data = await response.json();
            if(data){
                setWeatherData(data);
                setLoading(false);
            }
        }catch(e){
            setLoading(false);
            console.log(e);
        }
    }

    function handleSearch(){
        console.log(search)
        fetchWeatherData(search)
    };
    useEffect(
        ()=>{
            fetchWeatherData("tokyo")
        },[]
    )

    return <div>
        <Search
        search={search}
        setSearch={setSearch}
        handleSearch={handleSearch}
        />
        Weather
    </div>
}