import React, { useState } from 'react'
import NewGameForm from './NewGameForm'
import ScoreSheet from './ScoreSheet'

function GameTracker() {

    const [gameActive, setGameActive] = useState(false)
    const [round, setRound] = useState(0)
    const [players, setPlayers] = useState([
       { id1: '' },
       { id2: '' },
       { id3: '' },
       { id4: '' }

    ])

    const startNewGameForm = (
        <NewGameForm />
    )

    const gameProcess = (
        <div>
            <h1>Game Running</h1>
            <form>
                <table>
                    <tr></tr>
                </table>
            </form>
        </div>
    )

    return(
        <div className='component'>
            {startNewGameForm}
            <ScoreSheet />
        </div>
    )
}

export default GameTracker;
