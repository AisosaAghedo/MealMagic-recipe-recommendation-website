import React from 'react';
import logoImage from "../assets/Logo.jpg";
import "./logo.css";
export default function Logo(){
  return (
    <>
      <div className="logo-holder">
        <div className="logo">
          <img src={logoImage} alt="Logo of the website"></img>
        </div>
      </div>
    </>
  );
}