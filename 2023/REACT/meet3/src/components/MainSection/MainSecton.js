import React, {useState, useEffect} from "react"
import "./MainSection.css"

function MainSection(props){

    

    const  [state, setState] = useState({
        num1 : Math.floor((Math.random() * 10)),
        num2 : Math.floor((Math.random() * 10)),
        score : 0,
        response : "",
        incorrect : false
    })

    function updateResponse(event){
        setState({
            ...state,
            response : event.target.value
        })
    }

    function checkResponse(event){
        if (event.key === "Enter"){
            if (parseInt(state.response) === state.num1 + state.num2){
                setState({
                    score : state.score + 1,
                    response : "",
                    num1 : Math.floor((Math.random() * 10)),
                    num2 : Math.floor((Math.random() * 10)),
                    incorrect: false

                })
            }
            else {
                setState({
                    ...state,
                    incorrect: true,
                    score: state.score - 1,
                    response: ""    
                })
            }
        }
    }

    if (state.score > 5){
        return(
            <div className="container">
                <h1>you win</h1>
            </div>
        )
        
    }

    else if (state.score < -5){
        
        return(
            <div className="container">
                <h1>you lose</h1>
            </div>
        )
    }

    return(
        <section className="main">
            <div className="container">
                <h1 className={state.incorrect ? "incorrect": ""}>{state.num1} + {state.num2}</h1>
                <input 
                    type="text" 
                    value= {state.response}
                    onChange = {updateResponse}
                    onKeyPress={checkResponse} />
                <p>your score is : {state.score}</p>
                                           
            </div>
        </section>
    )
}

export default MainSection;
