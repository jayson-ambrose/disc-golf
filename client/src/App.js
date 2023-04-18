import React, { useEffect, useState } from 'react'
import './styles/App.css';
import './components/Navbar'
import Navbar from './components/Navbar';
import GameTracker from './components/GameTracker'
import Browse from './components/Browse'
import Stats from './components/Stats'
import Access from './components/Access'

function App() {

  const [user, setUser] = useState(null);

  function handleLogin (user){
      setUser(user)}

  return (
    <div>
      <h1>Pocket Caddy</h1>
      <Navbar />
      <hr/>
      {user ? (<p> hello {user.username}</p>): (<p>please log in</p>)}
      <Access handleLogin={handleLogin}/>
      <hr/>
      <GameTracker />
      <Browse />
      <Stats />
    </div>
  );
}

export default App;
