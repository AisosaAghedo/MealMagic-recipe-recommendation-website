import React, { useState } from "react";
import "./home.css";


export default function HomeDesign() {

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
      <div className="details">
        <h2>Please enter your prefered options</h2>
        <label htmlFor="diet">Dietary restrictions</label>
        <select name="Dietary restrictions" id="diet">
          <option value="Vegan">Vegan</option>
          <option value="Non vegan">Non vegan</option>
        </select>
        <label htmlFor="cuisine">Cuisine</label>
        <select name="Cuisine" id="cuisine">
          <option value="Nigeria"> Nigerian Cuisine</option>
          <option value="Ethiopia">Ethiopian Cuisine</option>
          <option value="french">French Cuisine</option>
          <option value="china">Chinese Cuisine</option>
          <option value="italy">Italian Cuisine</option>
        </select>
        <label htmlFor="Ingrediets" className="label">
          please enter list of ingredients available
        </label>
        <input
          /*value={ingredient}
          onChange={(e) => setIngredients(e.target.value)}*/
          type="text"
          placeholder="Ingredients"
        />
        <button type="submit" className="home-btn" onClick>
          Get Recommendation
        </button>
      </div>

      <div className="available">
        pepper, salt and other common ingredients are assummed to be available.
      </div>
    </div>
  );
}
