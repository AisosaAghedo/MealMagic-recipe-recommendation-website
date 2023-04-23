import React, { useState } from "react";
import "./home.css";
import { useForm } from "react-hook-form";


export default function HomeDesign() {
const {register, watch, handleSubmit,reset, formState:{errors}} =useForm('')
  const s = (data)=>{

  }
  /*const [ingredients, setIngredients] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch(
      "http://localhost:5000/api/meal_magic//recipes/ingredients",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          ingredients
        }),
      }
    );

    if (res.status === 201) {
      window.alert("Registration Succesful baddo sneh");
    } else {
      window.alert("Registration unSuccesful loser sneh");
    }
  };
*/
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
        />
        <div className="available">
          pepper, salt and other common ingredients are assummed to be
          available.
        </div>
        <button type="submit" className="home-btn" onClick={Hallo}>
          Get Recommendation
        </button>
      </div>
    </div>
  );
}
