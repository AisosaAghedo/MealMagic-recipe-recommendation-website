
import { useState } from "react";
import { Outlet, Link } from "react-router-dom";
import './navbar.css'
import logoImage from "../assets/Logo.jpg";
import {useAuth, logout} from '../signin/Signin'

const LoggedIn = () => {
  /* This function is called when the user is logged in */
  return (
    <>
      <Link to="/" className="nav">
        Home
      </Link>
      <Link to="about" className="nav">
        About
      </Link>

      <Link
        className="nav"
        to="/login"
        onClick={() => {
          logout();
        }}
      >
        Log Out
      </Link>

      <Outlet />
    </>
  );
}

const LoggedOut = () => {
  /* This function is called when the user is logged out */
  return (
    <>
      <Link to="/register" className="nav">
        Sign up
      </Link>
      <Link to="/login" className="nav">
        Login
      </Link>
      <Link to="/about" className="nav">
        About
      </Link>
      <Outlet />
    </>
  );
}
const Navbar = () => {
  /* This function displays the navbar for when
a user is logged in or logged out */

  const [logged] = useAuth();
  return (
    <>
      <div className="navclass">
        <div className="logo-holder">
          <div className="logo">
            <img
              className="img"
              src={logoImage}
              alt="Logo of the website"
            ></img>
          </div>
        </div>
        <div className="nav-holder">
          {logged ? <LoggedIn /> : <LoggedOut />}
        </div>
      </div>
    </>
  );
};
export default Navbar;

    