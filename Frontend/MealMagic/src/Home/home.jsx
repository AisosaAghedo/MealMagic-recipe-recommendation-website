import React from "react";
import Navbar from "../navbar/navbar";
import HomeDesign from "./homeDesign";
import './home.css'
const Home = () => {
  return (
    <>
      <Navbar />
      <div className="layout">
        <HomeDesign />
      </div>
    </>
  );
};
export default Home;
