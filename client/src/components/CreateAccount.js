import React from 'react'
import { FormikContext, useFormik } from 'formik'
import * as yup from 'yup'

function CreateAccount({handleLogin}) {

    const formSchema = yup.object().shape({
        username: yup.string().required("Must enter username").max(15).min(4),
        password: yup.string().required("Must enter password").max(30).min(6),
        re_password: yup.string().required("Must re-enter password")
      })
      
      const formik = useFormik({
        initialValues: {
          username: "",
          password: "",
          re_password:""
        },
    
        validationSchema: formSchema,
    
        onSubmit: (values, {resetForm}) => {

          fetch('/users', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(values)
          }).then(resp => {
            if (resp.ok){
            resp.json().then(data=> console.log(data))

            const login_obj = {
              username: values.username,
              password: values.password
            }

            handleLogin(login_obj)
            resetForm()
    
          }})
        }
      })
  return (
    <div className='component'>  
    <h1>Create Account</h1>    
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
          <label>Re-Enter Password</label><br/>
          <input 
            type='password'
            name='re_password'
            onChange={formik.handleChange}
            value={formik.values.re_password}
            /><br/>
          <button type='submit'>Sign-up</button>
      </form>
    </div>
  );
}

export default CreateAccount;
