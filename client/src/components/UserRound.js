import React from 'react'

function UserRound({ courseName, roundDate, players }) {

    const playerList = [];
    for (const player of players) {
        playerList.push(player['name'])
    };
    const playerNames = playerList.join(', ')

    return (
        <tr className='user-round table-row'>
            <td>{courseName}</td>
            <td>{roundDate}</td>
            <td>{playerNames}</td>
        </tr>
    )
}

export default UserRound