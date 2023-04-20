import React from 'react'
import { FormikContext, useFormik } from 'formik'
import * as yup from 'yup'

function NewGameForm({handleGameOn}) {

    const formSchema = yup.object().shape({
        course_id: yup.number().required("Must enter a course ID."),
        tournament_id: yup.number().required("Must enter a tournament ID. Use '1' for a casual round"),
        player_1: yup.string().required("Must enter at least one player."),
        player_2:   yup.string(),
        player_3:   yup.string(),
        player_4:   yup.string()
    })

    const formik = useFormik({
        initialValues : {
            course_id: '',
            tournament_id: '',
            player_1 : '',
            player_2: '',
            player_3: '',
            player_4: ''
    },

    validationSchema: formSchema,

    onSubmit: (values) => {
        const post_values = {
            course_id: values.course_id,
            tournament_id: values.tournament_id,
            players: []
        }

        const playersList = [values.player_1, values.player_2, values.player_3, values.player_4]

        playersList.forEach((player)=> {
            if (player != '') {
                post_values.players.push(player)
            }
        })

        handleGameOn()

        console.log('game on!')
        console.log(post_values)

        fetch('/rounds', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(post_values)
          }).then(resp => {
            if (resp.ok){
            resp.json().then(data=> console.log(data))    
          }})

        // console.log(post_values)
        //post request will go here to try generating a scorecard for each player.

    }})

    return (
        <div>
            <h1>Start a New Round</h1>
            <form onSubmit={formik.handleSubmit}>                
                <table>
                    <tbody>
                        <tr>
                            <td><label>Course ID</label></td>
                            <td><input
                                type='text'
                                name='course_id'
                                onChange={formik.handleChange}/>
                            </td>
                        </tr>                
                        <tr>
                            <td><label>Tournamnet ID</label></td>
                            <td><input
                                type='text'
                                name='tournament_id'
                                onChange={formik.handleChange}/>
                            </td>
                        </tr>                
                        <tr>
                            <td><label>Player 1 Name</label></td>
                            <td><input
                                type='text'
                                name='player_1'
                                onChange={formik.handleChange}/>
                            </td>
                        </tr>  
                        <tr>
                            <td><label>Player 2 Name</label></td>
                            <td><input
                                type='text'
                                name='player_2'
                                onChange={formik.handleChange}/>
                            </td>
                        </tr>  
                        <tr>
                            <td><label>Player 3 Name</label></td>
                            <td><input
                                type='text'
                                name='player_3'
                                onChange={formik.handleChange}/>
                            </td>
                        </tr>  
                        <tr>
                            <td><label>Player 4 Name</label></td>
                            <td><input
                                type='text'
                                name='player_4'
                                onChange={formik.handleChange}/>
                            </td>
                        </tr>
                    </tbody>  
                </table><br/>
            <button type='submit'>Start Round</button> 
            </form><br/>
        </div>
  );
}

export default NewGameForm;