import logo from './logo.svg';
import './App.css';
import Accordian from './components/accordian';
import RandomColor from './components/random-color';
import StarRating from './components/star-rating';
import ToDoList from './components/to-do-list';
import Weather from './components/weather';

function App() {
  return (
    <div className="App">
      {/* <Accordian/> */}
      {/* <RandomColor/> */}
      {/* <StarRating noOfStars={10}/> */}
      {/* <ToDoList/> */}
      <Weather/>
    </div>
  );
}

export default App;
