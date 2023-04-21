import React, { useState } from 'react'
import { FormikContext, useFormik } from 'formik'
import * as yup from 'yup'

function ScoreEntry({playerList, handleEndGame, roundId, setScorecards, scorecards}) {

  const [holeNum, setHoleNum] = useState(1)

    const numPlayers = playerList.length   

   const formSchema = yup.object().shape({
    score_1: yup.number().required('must enter score'),
    score_2: numPlayers >= 2 ? yup.number().required('must enter score') : null,
    score_3: numPlayers >= 3 ? yup.number().required('must enter score') : null,
    score_4: numPlayers >= 4 ? yup.number().required('must enter score') : null
   }) 

   const formik = useFormik({
    initialValues: {
        score_1: "",
        score_2: "",
        score_3: "",
        score_4: ""
    },

    validationSchema: formSchema,

    onSubmit: (values) => {      

      const scores = [values.score_1, values.score_2, values.score_3, values.score_4]

      const patch_obj = {
        hole: (holeNum),
        players: []
      }

      let i = 0

      playerList.forEach((player) => {
        patch_obj.players.push({id: player.id, score: scores[i]})
        i += 1
      })
      
      setHoleNum(holeNum + 1)

      fetch(`/rounds/${roundId}/scorecards`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(patch_obj)
      }).then(resp => resp.json())
        .then(
          fetch(`/rounds/${roundId}/scorecards`)
          .then (resp => resp.json())
          .then (data => setScorecards(data))
        )
    }
   }) 
   
   
   
   const displayPlayers = playerList.map((player) => {

        const playerNum = playerList.indexOf(player) + 1
        return (            
            <td key={player.name}>
                <label>{player.name}</label>
                <input type='text' name={`score_${playerNum}`} onChange={formik.handleChange}/>
            </td>)
})
    
  return (
    <div>
      <h1>Enter Scores for hole {holeNum}</h1>
      <form  onSubmit={formik.handleSubmit}>  
        <table>
            <tbody>
                <tr>
                    {displayPlayers}
                </tr>
            </tbody>
        </table>
        <button type="submit">Submit Hole Scores</button>
      </form>
      <button onClick={handleEndGame}>End game</button>
    </div>
  );
}

export default ScoreEntry;
