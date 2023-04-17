import React from 'react'

function GameTracker() {

    const loggedIn = true

    if(loggedIn === true) {

        return (
            <div>
                <h1>GAME TRACKER</h1>   
                <button>Start New Round</button>
            </div>
        );
    }

    else return (
        <div>
            <h1>GAME TRACKER</h1>
            <p>Please log in to continue...</p> 
        </div>
    )

    
    
}

export default GameTracker;
