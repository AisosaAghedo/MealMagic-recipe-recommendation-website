import React, { useState } from "react";
import './signin.css'
export const Signin = (props) => {
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");

  const handleSubmit = () => {
    e.preventDefault();
    console.log(email);
  };
  return (
    <div className="auth-form-container">
      <form className="signin-from" onsubmit={handleSubmit}>
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
      <button
        className="link-btn"
        onClick={() => props.onFormSwitch("Register")}
      >
        Don't have an account? Register here.
      </button>
    </div>
  );
};
