import React, { useState } from "react";
import './signin.css'
import { Outlet, Link } from "react-router-dom";
import { useForm } from "react-hook-form";
import {useNavigate} from 'react-router-dom'
import { createAuthProvider } from "react-token-auth";

export const {useAuth, authFetch, login, logout} = createAuthProvider({
  accessTokenKey: "access_token",
  onUpdateToken: (token) =>
    fetch("http://127.0.0.1:5000/auth/refresh", {
      method: "POST",
      body: token.refresh_token,
    }).then((r) => r.json()),
});


export const Signin = () => {
  const {register,handleSubmit,reset,formState: { errors }} = useForm("");

  const navigate =useNavigate()

  const submitLogin=(data)=>{
    console.log(data)

    const requestOptions = {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(data)
    }

    fetch("http://127.0.0.1:5000/auth/login", requestOptions)
    .then(res=>res.json())
    .then(data=>{
      console.log(data.access_token)
      login(data.access_token)
      navigate('/')
    })
    // reset()
  }

  return (
    <div className="body" id="auth-form-container">
      <form className="signin-from">
        <label htmlFor="email" className="label-class">
          Email
        </label>
        <input className="input"
          type="email"
          placeholder="youremail@gmail.com"
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
        <label className="label-class" htmlFor="password">
          Password
        </label>
        <input
        className="input"
          type="password"
          placeholder="*******"
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
        <button
          className="submit"
          type="submit"
          onClick={handleSubmit(submitLogin)}
        >
          Login
        </button>
      </form>
      <Link to="/register">
        <button className="link-btn">
          Don't have an account? Register here.
        </button>
      </Link>
      <Outlet />
    </div>
  );
};
