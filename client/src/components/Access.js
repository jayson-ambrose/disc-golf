import React from 'react'

function Access() {
  return (
    <form>
        <label for='username'>Username</label><br/>
        <input type='text' /><br/>
        <label for='password'>Password</label><br/>
        <input type='password' /><br/>
        <button type='submit'>Login</button>
    </form>
  );
}

export default Access;
