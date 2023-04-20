import React, { useState } from 'react'
import NewGameForm from './NewGameForm'
import ScoreSheet from './ScoreSheet'
import ScoreEntry from './ScoreEntry'

function GameTracker() {

    const [gameOn, setGameOn] = useState(true) //set back to false for production
    const [playerList, setPlayerList] = useState(['jayson', 'eric'])    
    const [roundId, setRoundId] = useState(0)

    const [players, setPlayers] = useState([
       { id1: '' },
       { id2: '' },
       { id3: '' },
       { id4: '' }
    ])

    function handleGameOn () {
        //retrieve player list by round id
        setGameOn(true)
    }

    function handleEndGame () {
        //anything else we need to do when the game ends. persist info to scorecards maybe?
        setGameOn(false)
    }

    return(
        <div className='component'>
            {gameOn ? <ScoreEntry playerList={playerList} handleEndGame={handleEndGame}/> : <NewGameForm gameOn={gameOn} handleGameOn={handleGameOn}/>}            
            {gameOn ? <ScoreSheet playerList={playerList} roundId={roundId}/> : null} 
        </div>
    )
}

export default GameTracker;
