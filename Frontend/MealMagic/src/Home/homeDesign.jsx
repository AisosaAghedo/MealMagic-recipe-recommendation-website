import React, { useState } from "react";
import "./home.css";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useAuth, logout } from "../signin/Signin";
import ingredientsImg from '../assets/ingredients_img.jpg'
import { Outlet, Link } from "react-router-dom";

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

const LoggedOut_Home = ()=>{
  return (
    <div className="loggedout">
      <div className="content">
        <div className="text"> 
          <h2>
            MealMagic Recipe Recommendation
          </h2>

          <p className="para">
            MealMagic is a website that helps our users think! Yes, you don't
            need to start thinking of what to make for breakfast, lunch or
            dinner, Mealmagic helps to provide you with various recipes from
            around the world using ingredients you already have at home. <br />
            Whether you're a seasoned chef or just starting out in the kitchen,
            MealMagic has everything you need to take your cooking skills to the
            next level <br />
          </p>
          <div className="button">
            <Link to="/register">
              <button className="btn3">Sign Up Here</button>
            </Link>
            <Outlet />
          </div>
        </div>
        <div className="pepsi">
          <img className="home_img" src={ingredientsImg} alt="image" />
        </div>
      </div>
    </div>
  );
}

export default function HomeDesign() {
  const [logged] = useAuth();

  return <div>{logged ? <Loggedin_Home /> : <LoggedOut_Home />}</div>;
  
}
