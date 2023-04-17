import React from 'react'
import './styles/App.css';
import './components/Navbar'
import Navbar from './components/Navbar';
import GameTracker from './components/GameTracker'
import Browse from './components/Browse'
import Stats from './components/Stats'
import Access from './components/Access'

function App() {
  return (
    <div>
      <h1>Pocket Caddy</h1>
      <Navbar />
      <hr/>
      <Access />
      <hr/>
      <GameTracker />
      <Browse />
      <Stats />
    </div>
  );
}

export default App;
