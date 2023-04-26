import React, { useState } from "react";
import "./home.css";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { useAuth, logout } from "../signin/Signin";

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
  );
  
}

const LoggedOut_Home = ()=>{
  return (
    <div>
      HEY
    </div>
  )
}

export default function HomeDesign() {
  const [logged] = useAuth();

  return <div>{logged ? <Loggedin_Home /> : <LoggedOut_Home />}</div>;
  
}
