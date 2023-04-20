import React from 'react'
import { FormikContext, useFormik } from 'formik'
import * as yup from 'yup'

function ScoreEntry({playerList, handleEndGame}) {

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
        console.log(values)
    }
   })
   
   const displayPlayers = playerList.map((player) => {

        const playerNum = playerList.indexOf(player) + 1
        return (            
            <td key={player}>
                <label>{player}</label>
                <input type='text' name={`score_${playerNum}`} onChange={formik.handleChange}/>
            </td>)
})
    
  return (
    <div>
      <h1>Enter Scores</h1>
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
