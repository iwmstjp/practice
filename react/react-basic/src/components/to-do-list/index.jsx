import { useState } from 'react'
import {FaStar} from 'react-icons/fa'
import './styles.css'

export default function ToDoList({noOfStars = 5}){
    const [tasks, setTasks] = useState(["Lunch"]);
    const [newTask, setNewTask] = useState("");

    function handleInputChange(event){
        setNewTask(event.target.value);
    }

    function addTask(){
        if(newTask.trim() !== ""){
            setTasks(t => [...t, newTask]);
            setNewTask("");
        }
    }
    function doneTask(index){
        const updatedTasks = tasks.filter((_,i) => i !== index);
        setTasks(updatedTasks);
    }
    function upTask(index){
        const updateTasks = [...tasks]
        if (index > 0){
            [updateTasks[index], updateTasks[index - 1]]= [updateTasks[index - 1], updateTasks[index]];
            setTasks(updateTasks);
        }
    }
    function downTask(index){
        const updateTasks = [...tasks]
        if (index < tasks.length - 1){
            [updateTasks[index], updateTasks[index + 1]]= [updateTasks[index + 1], updateTasks[index]];
            setTasks(updateTasks);
        }
    }

    return (
        <div className="to-do-list">
            <h1>To Do List</h1>
            <div>
                <input 
                    type="text"
                    placeholder='Enter a task ...'
                    value={newTask}
                    onChange={handleInputChange} />
                <button 
                    className='add-button'
                    onClick={addTask}>
                    Add
                </button>
            </div>
            <ol>
                {tasks.map((task, index) => 
                <li key={index}>
                    <span className='text'>{task}</span>
                    <button 
                        className='done-button'
                        onClick={() => doneTask(index)}>
                        Done
                    </button>
                    <button 
                        className='move-button'
                        onClick={() => upTask(index)}>
                        Up
                    </button>
                    <button 
                        className='move-button'
                        onClick={() => downTask(index)}>
                        Down
                    </button>
                </li>

            )}
            </ol>
        </div>
    )
    
}