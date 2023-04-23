
import { useState } from "react";
import { Outlet, Link } from "react-router-dom";
import './navbar.css'
import logoImage from "../assets/Logo.jpg";
import {useAuth, logout} from '../signin/Signin'

const LoggedIn = () => {
  return (
    <>
      <Link to="/" className="nav">
        Home
      </Link>
      <Link to="/Recipe" className="nav">
        Recipe
      </Link>
      <Link to="about" className="nav">
        About
      </Link>
      <a
        className="nav"
        href="#"
        onClick={() => {
          logout();
        }}
      >
        Log Out
      </a>
      <Outlet />
    </>
  );
}

const LoggedOut = () => {
    return (
      <>
        <Link to="/register" className="nav">
          Sign up
        </Link>
        <Link to="/login" className="nav">
          Login
        </Link>
        <Link to="about" className="nav">
          About
        </Link>
        <Outlet />
      </>
    );}
const Navbar = () => {

  const [logged]=useAuth();
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

    