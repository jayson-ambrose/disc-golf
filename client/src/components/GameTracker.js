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

    function getPlayers () {

        fetch(`/rounds/${id}/players`)
        .then(resp => resp.json())
        .then(data => setPlayers(...players , [
            {id1: data.player1.id},
            {id2: data.player2.id},
            {id3: data.player3.id},
            {id4: data.player4.id}
        ]))
    }

    const startNewGameForm = (
        <div>
            <h1>Start a New Round</h1>
            <form>                
                <table>
                    <tr>
                        <td><label>Course ID</label></td>
                        <td><input type='text' name='course_id'></input></td>
                    </tr>                
                    <tr>
                        <td><label>Tournament ID</label></td>
                        <td><input type='text' name='tournament_id'></input></td>
                    </tr>                
                    <tr>
                        <td><label>Player 1 Name</label></td>
                        <td><input type='text' name='p1_name'></input></td>
                    </tr>  
                    <tr>
                        <td><label>Player 2 Name</label></td>
                        <td><input type='text' name='p2_name'></input></td>
                    </tr>  
                    <tr>
                        <td><label>Player 3 Name</label></td>
                        <td><input type='text' name='p3_name'></input></td>
                    </tr>  
                    <tr>
                        <td><label>Player 4 Name</label></td>
                        <td><input type='text' name='p4_name'></input></td>
                    </tr>  
                </table><br/>
            <button type='submit'>Start Round</button> 
            </form><br/>
        </div>
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
