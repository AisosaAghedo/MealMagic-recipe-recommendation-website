
import { useState } from "react";
import { Outlet, Link } from "react-router-dom";
import './navbar.css'
import logoImage from "../assets/Logo.jpg";

const Navbar = () => {
  const [current, setCurrent] = useState("h");
  const onClick = (e) => {
    console.log("click ", e);
    setCurrent(e.key);
  };
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
          <Link to="/" className="nav">
            Home
          </Link>
          <Link to="/Recipe" className="nav">
            Recipe
          </Link>
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
        </div>
      </div>
    </>
  );
};
export default Navbar;

    