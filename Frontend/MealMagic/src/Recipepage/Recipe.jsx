import React from "react";
import { useState, useEffect } from "react";
import Navbar from "../navbar/navbar";
import RecipeCard from "./RecipeCard";
import SearchBar from "./SearchBar";
import "./Recipe.css";
const Home = () => {
  return (
    <div>
      <Navbar />
      <SearchBar />
      <RecipeCard />
    </div>
  )
};
export default Home;
