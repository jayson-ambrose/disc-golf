import React from 'react'

function NewGameForm() {
  return (
    <div>
        <h1>Start a New Round</h1>
        <form>                
            <table>
                <tr>
                    <td><label>Course ID</label></td>
                    <td><input type='text' name='course_id'></input></td>
                </tr>                
                <tr>
                    <td><label>Tournamnet ID</label></td>
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
  );
}

export default NewGameForm;