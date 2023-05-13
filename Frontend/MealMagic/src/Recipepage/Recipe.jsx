import React from "react";
import { useState, useEffect } from "react";
import Navbar from "../navbar/navbar";
import RecipeCard from "./RecipeCard";
import "./Recipe.css";

const Recipe = () => {
  return (
    <div>
      <Navbar />
      <RecipeCard/>
      
    </div>
  );
};
export default Recipe;
