import React from 'react'
import { Link } from 'react-router-dom'

function Navbar() {
  return (

    <div className='component navbar'>      
      <Link to='GameTracker'>
        <li>-Game Tracker-</li>
      </Link>
      <Link to='Browse'>
        <li>-Browse-</li>
      </Link>
      <Link to='Stats'>
        <li>-Stats-</li>
      </Link>
      <Link to='CreateAccount'>
        <li>-Create Account-</li>
      </Link>
      <Link to='Account'>
        <li>View Account</li>
      </Link>
    </div>

  );
}

export default Navbar;
