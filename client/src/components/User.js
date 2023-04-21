import React, { useState, useEffect } from 'react'
import UserRound from './UserRound'

function User({ user }) {
    const [rounds, setRounds] = useState([]);

    useEffect(() => {
        fetch(`/users/${user['id']}/rounds`)
            .then(r => {
                if (r.ok) {
                    r.json();
                }
            })
            .then(data => {
                setRounds(data)
            })
    },[user]);


    const roundList = rounds.forEach(round => {
        return (
            <UserRound courseName={round['course']} roundDate={round['date']} players={round['players']}/>
        )
    })


    return (
        <div>
            <h1>Your Rounds</h1>
            <table>
                <tr>
                    <th>Course</th>
                    <th>Date</th>
                    <th>Players</th>
                </tr>
                {rounds ? roundList : null}
            </table>
        </div>
    );
}

export default User;