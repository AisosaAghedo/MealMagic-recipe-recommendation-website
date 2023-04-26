import React, { useState } from "react";
import "./home.css";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useAuth, logout } from "../signin/Signin";
import ingredientsImg from '../assets/ingredients_img.jpg'

const Loggedin_Home = ()=>{
  const navigate = useNavigate();
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm("");
  const submitIngredients = (data) => {
    navigate(`/Recipe/${data.ingredients}`);
  };

  return (
    <div className="layout">
      <div className="home-container">
        <div className="ingredients">
          <label htmlFor="Ingrediets" className="label">
            <h2>please enter list of ingredients available</h2>
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

const LoggedOut_Home = ()=>{
  return (
    <div className="loggedout">
      <div class="content">
        <div class="text">
          <h1>
            MealMagic
          </h1>
          <p>
            Pepsi is a carbonated soft drink manufactured by PepsiCo. <br />
            Originally created and developed in 1893 by Caleb Bradham <br />
            and introduced as Brad's Drink, it was renamed as Pepsi-Cola in
            1898, and then shortened to Pepsi in 1961.
          </p>
        </div>
        <div class="pepsi">
          <img src={ingredientsImg} alt="image" />
        </div>
      </div>
      <div className="button">
        <button class="btn3">Buy Now</button>
      </div>
    </div>
  );
}

export default function HomeDesign() {
  const [logged] = useAuth();

  return <div>{logged ? <Loggedin_Home /> : <LoggedOut_Home />}</div>;
  
}
