import React, { useState, useEffect } from 'react'
import UserRound from './UserRound'

function User({ user, setUser }) {
    const [rounds, setRounds] = useState([]);

    useEffect(() => {
        if (user !== null){
        fetch(`/users/${user['id']}/rounds`)
            .then(r => r.json())
            .then(data => {
                console.log(data);
                setRounds(data)
            })
    }},[user]);
    
    let userRound
    function createRoundList (rounds) {
        userRound = rounds.map(round => {
            return (
                <UserRound courseName={round['course']['name']} roundDate={round['date']} players={round['players']} scores={round['scorecards']} key={round['id']}/>
            )
        })
    }

    if (rounds.length !== 0) {
        createRoundList(rounds)
    }

    function handleDelete(e) {
        if (window.confirm('Are you sure you want to delete your account? This deletes any rounds you might have played.')) {
            fetch(`/users/${user['id']}`,{
                method: 'DELETE'
            }).then(() => setUser(null));
        }
    }

    return (
        <div>
            <h1>Your Rounds</h1>
            <table className='account table'>
                <thead>
                    <tr>
                        <th>Course</th>
                        <th>Date</th>
                        <th>Player 1 Name</th>
                        <th>Player 1 Score</th>
                        <th>Player 2 Name</th>
                        <th>Player 2 Score</th>
                        <th>Player 3 Name</th>
                        <th>Player 3 Score</th>
                        <th>Player 4 Name</th>
                        <th>Player 4 Score</th>

                    </tr>
                </thead>
                <tbody>
                    {userRound}
                </tbody>
            </table>
            <button onClick={handleDelete}>Delete Account</button>
        </div>
    );
}

export default User;