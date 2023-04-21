import React, { useEffect, useState } from 'react'
import './styles/App.css';
import { Switch, Route } from "react-router-dom";
import './components/Navbar'
import Navbar from './components/Navbar';
import GameTracker from './components/GameTracker'
import Browse from './components/Browse'
import Stats from './components/Stats'
import Login from './components/Login'
import CreateAccount from './components/CreateAccount'
import User from './components/User'

function App() {

  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch('/check_session')
    .then(resp => {
      if (resp.ok){
        resp.json().then(data => setUser(data))
      }
      else {
        setUser(null)
      }
    })
    
  }, [])

  function handleLogin (val){

    fetch('/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(val)
      }).then(resp => {
        if (resp.ok){
        resp.json().then(data=> setUser(data))
        }})}
      

   let greeting
   if (user) {
     greeting = <h1>{user.username} is logged in.</h1>
   }
   else {
     greeting = <h1>Log In</h1>
  }

  function handleLogout (user) {
    fetch('/logout', {
      method: 'DELETE'
    }).then(() => setUser(null))
  }

  return (
    <div className='component'>
      <h1>Pocket Caddy</h1>
      <Navbar />
      <hr/>
      {greeting}
      {!user ? <Login handleLogin={handleLogin}/> : <button onClick={handleLogout}>Logout</button>}
      <hr/>
      <Switch>
        
        <Route exact path='/GameTracker'>
          <GameTracker user={user}/>
        </Route>
        {/* <Route exact path='/Browse'>
          <Browse />
        </Route> */}
        {/* <Route exact path='/Stats'>
          <Stats />
        </Route>  */}
        <Route exact path='/CreateAccount'>
          <CreateAccount handleLogin={handleLogin} />
        </Route>  
        <Route exact path='/Account'>
          <User user={user} setUser={setUser}/>
        </Route>
      </Switch>
    </div>
  );
}

export default App;
