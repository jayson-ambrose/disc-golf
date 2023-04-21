import React, { useState } from 'react'
import NewGameForm from './NewGameForm'
import ScoreSheet from './ScoreSheet'
import ScoreEntry from './ScoreEntry'

function GameTracker({user}) {

    const [gameOn, setGameOn] = useState(false) //set back to false for production
    const [playerList, setPlayerList] = useState([])    
    const [roundId, setRoundId] = useState(0)
    const [courseId, setCourseId] = useState(0)
    const [scorecards, setScorecards] = useState([])

    function getScorecards (id) {
        fetch(`/rounds/${id}/scorecards`)
        .then(resp => resp.json())
        .then(data => setScorecards(data))
    }

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
        
        setRoundId(roundData.round.id)
        setCourseId(roundData.round.course_id)
        getPlayersByRoundId(roundData.round.id)
        getScorecards(roundData.round.id)
        setGameOn(true)

    }

    function handleEndGame () {
        //anything else we need to do when the game ends. persist info to scorecards maybe?

        setPlayerList([])
        setScorecards([])        
        setGameOn(false)
    }

    if (user === null){
        return(
            <h2>Please log in or sign up to use game tracker.</h2>
        )
    }

    return(
        <div className='component'>
            {gameOn ? <ScoreEntry playerList={playerList} handleEndGame={handleEndGame} courseId={courseId} roundId={roundId} setScorecards={setScorecards} scorecards={scorecards}/>
             : <NewGameForm gameOn={gameOn} handleGameOn={handleGameOn} getScorecards={getScorecards} getPlayersByRoundId={getPlayersByRoundId}/>}            
            {gameOn ? <ScoreSheet scorecards={scorecards} playerList={playerList} courseId={courseId} roundId={roundId} /> : null} 
        </div>
    )
}

export default GameTracker;
