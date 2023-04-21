import React from 'react'

function UserRound({ courseName, roundDate, players, scores }) {

    const playerList = [];
    for (const player of players) {
        playerList.push(player['name'])
    };
    const playerNames = players.forEach(player => {
        const pScore = scores.find(score => score.player_id === player.id);
        return (
            <>
                <td>{player.name}</td>
                <td>{pScore.total_score}</td>
            </>
        )
    })

    return (
        <tr className='user-round table-row'>
            <td>{courseName}</td>
            <td>{roundDate}</td>
            {playerNames}
        </tr>
    )
}

export default UserRound