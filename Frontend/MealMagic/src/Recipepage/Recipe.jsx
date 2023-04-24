import React from "react";
import { useState, useEffect } from "react";
import Navbar from "../navbar/navbar";
import RecipeCard from "./RecipeCard";
import "./Recipe.css";

const Home = () => {
  return (
    <div>
      <Navbar />
      <RecipeCard />
    </div>
  )
};
export default Home;
