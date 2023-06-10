import React, { useState } from "react";
import "./home.css";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useAuth, logout } from "../signin/Signin";
import ingredientsImg from '../assets/ingredients_img.jpg'
import { Outlet, Link } from "react-router-dom";


export default function HomeDesign(){
  /* This function return a page for users to
  input ingredients available */

  const navigate = useNavigate();
  const {register,handleSubmit,reset,formState: { errors },} = useForm("");
  
  const submitIngredients = (data) => {
    /* This function navigates to the recipe page and takes ingedients entered as url parameters */
    navigate(`/Recipe/${data.ingredients}`);
    
  };

  return (
    <div className="layout">
      <div className="home-container">
        <div className="ingredients">
          <label htmlFor="Ingrediets" className="label">
            <h2>Please enter list of ingredients available</h2>
          </label>
          <input
            className="home_input

        "
            type="text"
            placeholder="Ingredients"
            {...register("ingredients", { required: true })}
          />
          {errors.ingredients && (
            <p style={{ color: "red" }}>
              <small>Ingredients are required</small>
            </p>
          )}
          <div className="available">
            pepper, salt and other common ingredients are assummed to be
            available.
          </div>
          <button
            type="submit"
            className="home-btn"
            onClick={handleSubmit(submitIngredients)} 
          >
            Get Recommendation
          </button>
        </div>
      </div>
    </div>
  );
  
}


