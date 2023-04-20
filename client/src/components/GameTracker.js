import React, { useState } from 'react'
import NewGameForm from './NewGameForm'

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
            <table>
                <tr>
                    <th>HL</th>
                    <th>PAR</th>
                    <th>DIST</th>
                    <th>P1</th>
                    <th>P2</th>
                    <th>P3</th>
                    <th>P4</th>
                </tr>
            </table>
        </div>
    )
}

export default GameTracker;
