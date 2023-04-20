import React, { useState } from 'react'
import NewGameForm from './NewGameForm'
import ScoreSheet from './ScoreSheet'
import ScoreEntry from './ScoreEntry'

function GameTracker() {

    const [gameOn, setGameOn] = useState(false) //set back to false for production
    const [playerList, setPlayerList] = useState([])    
    const [roundId, setRoundId] = useState(0)
    const [courseId, setCourseId] = useState(0)

    function getPlayersByRoundId (id) {
        fetch(`/rounds/${id}/players`)
        .then(resp => resp.json())
        .then(data => {
            const playerArray = []
            data.players.forEach((player) => {
                playerArray.push(player)
            })
            setPlayerList(playerArray)            
        })
    }

    function handleGameOn (roundData) {

        setGameOn(true)
        setRoundId(roundData.round.id)
        setCourseId(roundData.round.course_id)
        getPlayersByRoundId(roundData.round.id)

    }

    function handleEndGame () {
        //anything else we need to do when the game ends. persist info to scorecards maybe?
        setGameOn(false)
    }

    return(
        <div className='component'>
            {gameOn ? <ScoreEntry playerList={playerList} handleEndGame={handleEndGame} courseId={courseId} roundId={roundId}/> : <NewGameForm gameOn={gameOn} handleGameOn={handleGameOn}/>}            
            {gameOn ? <ScoreSheet playerList={playerList} courseId={courseId} roundId={roundId}/> : null} 
        </div>
    )
}

export default GameTracker;
