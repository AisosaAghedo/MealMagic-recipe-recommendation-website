import React, {useState} from "react";
import "./Signup.css";
import { Outlet, Link, useNavigate } from "react-router-dom";
import {useForm} from 'react-hook-form';

export  default function SignupDesign(props) {
    
  const {register, watch, handleSubmit,reset, formState:{errors}} =useForm('')
  const submitRegister = (data)=>{
    if(data.password === data.confirmPassword){

      const body={
        name:data.name,
        email:data.email,
        password:data.password
      }

    const requestOptions={
      method:'POST',
      headers:{
        'content-type':'application/json'
      },
      body:JSON.stringify(body)
    }

    fetch("http://localhost:5000/api/meal_magic/users", requestOptions)
      .then((res) => res.json())
      .then((data) => console.log(data))
      .then(console.log(`User ${data.name} created succcesfully`))
      .catch((err) => console.log(err));
    
    reset()
  }
  else{
    alert("Password and confirm password don't match")
  }
}
  return (
    <>
      <div className="container">
        <form method="POST">
          <label className="signup_label" htmlFor="">
            Username
          </label>
          <input
            className="signup_input"
            type="text"
            placeholder=" Your Username"
            {...register("name", { required: true, maxLength: 25 })}
          />
          {errors.name && (
            <p style={{ color: "red" }}>
              <small>Username is required</small>
            </p>
          )}
          {errors.name?.type === "maxLength" && (
            <p style={{ color: "red" }}>
              <small>Maximum characters should be 25</small>
            </p>
          )}
          <label className="signup_label" htmlFor="">
            Email
          </label>
          <input
            className="signup_input"
            type="email"
            placeholder="Email"
            {...register("email", { required: true, maxLength: 75 })}
          />
          {errors.email && (
            <p style={{ color: "red" }}>
              <small>Email is required</small>
            </p>
          )}
          {errors.email?.type === "maxLength" && (
            <p style={{ color: "red" }}>
              <small>Maximum characters should be 75</small>
            </p>
          )}
          <label className="signup_label" htmlFor="">
            Password
          </label>
          <input
            className="signup_input"
            type="password"
            placeholder="Password"
            {...register("password", { required: true, minLength: 8 })}
          />
          {errors.password && (
            <p style={{ color: "red" }}>
              <small>Password is required</small>
            </p>
          )}
          {errors.password?.type === "minLength" && (
            <p style={{ color: "red" }}>
              <small>Minimum characters should be 8</small>
            </p>
          )}
          <label className="signup_label" htmlFor="">
            Confirm Password
          </label>
          <input
            className="signup_input"
            type="password"
            placeholder="Confirm Password"
            {...register("confirmPassword", { required: true, minLength: 8 })}
          />
          {errors.confirmPassword && (
            <p style={{ color: "red" }}>
              <small>confirmPassword is required</small>
            </p>
          )}
          {errors.confirmPassword?.type === "minLength" && (
            <p style={{ color: "red" }}>
              <small>Minimum characters should be 8</small>
            </p>
          )}
          <button
            type="submit"
            className="btn"
            onClick={handleSubmit(submitRegister)}
          >
            Sign Up
          </button>
        </form>
        <Link to="/login">
          <button className="link-btn">Already signed up? Login here.</button>
        </Link>
        <Outlet />
      </div>
    </>
  );
}
