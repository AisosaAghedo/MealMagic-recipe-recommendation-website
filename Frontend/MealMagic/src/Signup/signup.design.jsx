import React from "react";
import "./Signup.css";

export default function SignupDesign() {
  return (
    <>
      <div className="container">
        <form action="">
          <label htmlFor="">Username</label>
          <input type="text" placeholder="Username" />
          <label htmlFor="">Email</label>
          <input type="email" placeholder="Email" />
          <label htmlFor="">Password</label>
          <input type="password" placeholder="Password" />
          <label htmlFor="">Confirm Password</label>
          <input type="password" placeholder="Confirm Password" />
          <button type="submit" className="btn">
            Sign Up
          </button>
        </form>
        <button className="link-btn">
          Already signed up? <span>Login here.</span>
        </button>
      </div>
    </>
  );
}