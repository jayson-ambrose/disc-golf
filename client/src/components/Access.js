import React, { useState, useEffect } from 'react'
import { FormikContext, useFormik } from 'formik'
import * as yup from 'yup'

function Access({ handleLogin }) {

  // useEffect(() => {
  //   fetch('http://127.0.0.1:5555/users')
  //   .then(resp => resp.json())
  //   .then(data => {
  //     setUsers(data)
  //     console.log(data)
  //   })
  // }, [])

  const formSchema = yup.object().shape({
    username: yup.string().required("Must enter username").max(15).min(5)
  })
  
  const formik = useFormik({
    initialValues: {
      username: ""
    },

    validationSchema: formSchema,

    onSubmit: (values) => {
      fetch('http://127.0.0.1:5555/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values)
      }).then(resp => resp.json())
      .then(data => {
        data ? handleLogin(data) : handleLogin(null)
      })
    }
  })

  return (
    <div>      
      <form onSubmit={formik.handleSubmit}>

          <label>Username</label><br/>
          <input 
            type='text'
            name='username'
            onChange={formik.handleChange}
            value={formik.values.username}
            /><br/>
          <button type='submit'>Login</button>
      </form>
    </div>
  );

}

export default Access;
