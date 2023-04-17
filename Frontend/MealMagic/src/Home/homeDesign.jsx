import React from "react";
import "./home.css";
export default function HomeDesign() {
  return (
    <div className="home-container">
      <div className="details">
        <p>Please enter your prefered options</p>
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
          plese enter list of ingredients available
        </label>
        <input type="text" placeholder="Ingredients" />
        <button type="submit" className="home-btn">
          Get Recommendation
        </button>
      </div>

      <div className="available">
        pepper, salt and other common ingredients are assummed to be available.
      </div>
    </div>
  );
}
