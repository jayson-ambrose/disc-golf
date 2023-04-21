import React, { useState, useEffect } from 'react'
import { FormikContext, useFormik } from 'formik'
import * as yup from 'yup'

function Login({ handleLogin }) {

  const formSchema = yup.object().shape({
    username: yup.string().required("Must enter username").max(15).min(4),
    password: yup.string().required("Must enter password").max(30).min(6)
  })
  
  const formik = useFormik({
    initialValues: {
      username: "",
      password: ""
    },

    validationSchema: formSchema,

    onSubmit: (values, {resetForm}) => {

      handleLogin(values)
      resetForm()

      }})

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
          <label>Password</label><br/>
          <input 
            type='password'
            name='password'
            onChange={formik.handleChange}
            value={formik.values.password}
            /><br/>
          <button type='submit'>Login</button>
      </form>
    </div>
  );

}

export default Login;
