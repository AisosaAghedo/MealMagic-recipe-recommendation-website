import React from "react";
import { useParams } from 'react-router-dom'

const RecipeCard = () => {
  function getRecipes() {
    const { ingredients } = useParams();
    return (ingredients)
    console.log(ingredients);
  }
  getRecipes();

  const requestOptions = {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({'ingredients': getRecipes()}),
  };

  const fetchOptions = {
    method: "GET",
    headers: {
      "content-type": "application/json",
    },
  };

  fetch(
    "http://localhost:5000/api/meal_magic/recipes/ingredients",
    requestOptions
  )
    .then((res) => res.json())
    .then((data) => {
      for (let value of data.suggested_recipe) {
        console.log(value[0]);
        fetchOptions.body = JSON.stringify({name: value[0]})
        fetch("http://localhost:5000/api/meal_magic/get_recipes",fetchOptions)
        .then(res => res.json())
        .then(data => console.log(data))
      }
    })

    .catch((err) => console.log(err));

  // reset()

  return (
    <div className="container1">
      <div className="recipe">
        <h3>Instruction</h3>
      </div>
      <div className="photo">
        <img className="size" src="" alt="Recipe images" />
      </div>
    </div>
  );
}
export default RecipeCard;