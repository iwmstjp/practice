import { useState } from "react";
import data from "./data";
import './styles.css';
export default function Accordian() {
    const [selected, setSelected] = useState(null);
    const [enalbieMultiSelection, setEnableMultiSelection] = useState(false);
    const [multiple, setMultiple] = useState([]);

    function handleSingleSelection(getCurrentID){
        setSelected(getCurrentID === selected ? null : getCurrentID);
    }
    function handleMultiSelection(getCurrentID){
        let cpyMultiple = [...multiple];
        const findIndexOfCurrentId = cpyMultiple.indexOf(getCurrentID);
        console.log(findIndexOfCurrentId);
        if(findIndexOfCurrentId === -1) cpyMultiple.push(getCurrentID)
        else cpyMultiple.splice(findIndexOfCurrentId, 1)
        setMultiple(cpyMultiple);
    }
    function reset(){
        setEnableMultiSelection(!enalbieMultiSelection);
        setSelected(null);
        setMultiple([]);
    }

    console.log(selected, multiple)
    return <div className="wrapper">
        <button onClick={()=> reset()}>Enable Multi Selection</button>
        <div className="accordian">
            {
                data && data.length > 0 ?
                data.map(dataItem=> <div className="item">
                    <div onClick={ enalbieMultiSelection 
                        ? () => handleMultiSelection(dataItem.id) 
                        : () => handleSingleSelection(dataItem.id)} className="titile">
                        <h3>{dataItem.question}</h3>
                        <span>+</span>
                    </div>
                    {/* <div onClick={ () => handleMultiSelection(dataItem.id) } className="titile">
                        <h3>{dataItem.question}</h3>
                        <span>+</span>
                    </div> */}
                    {
                        selected === dataItem.id 
                        || multiple.indexOf(dataItem.id) !== -1
                        ?
                        <div className="content">{dataItem.answer}</div>
                        : null
                    }
                </div>
                )
                : <div>No data found !</div>
            }
        </div>
    </div>
}
// const Accordian = ()=>{
//     return (
//         <div>Hello!!</div>
//     )
// }
// export default Accordian