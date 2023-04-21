import React, { useState } from "react";
import './signin.css'
import { Outlet, Link } from "react-router-dom";
export const Signin = (props) => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(email);
  };
  return (
    <div className="auth-form-container">
      <form className="signin-from" onSubmit={handleSubmit}>
        <label htmlFor="email" className="label-class">
          Email
        </label>
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          type="email"
          placeholder="youremail@gmail.com"
          id="email"
          name="email"
        />
        <label className="label-class" htmlFor="password">
          Password
        </label>
        <input
          value={pass}
          onChange={(e) => setPass(e.target.value)}
          type="password"
          placeholder="*******"
          id="password"
          name="password"
        />
        <button className="submit" type="submit">
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
