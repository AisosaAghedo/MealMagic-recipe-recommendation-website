import React, {useState, useEffect} from "react";
import { useParams } from 'react-router-dom'


const RecipeCard = () => {
  const [recipes, setRecipes] = useState([]);


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
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
  };
 useEffect(
        () => {
  fetch(
    "http://localhost:5000/api/meal_magic/recipes/ingredients",
    requestOptions
  )
    .then((res) => res.json())
    .then((data) => {
      let i = 0;
      let list_of_recipes = []
      for (let value of data.suggested_recipe) {
        fetchOptions.body = JSON.stringify({ name: value[0] });
        fetch("http://localhost:5000/api/meal_magic/get_recipes", fetchOptions)
          .then((res) => res.json())
          .then((data) => {
            i++;
            list_of_recipes.push(data);
            // console.log(list_of_recipes)
            if (i === 10){
              console.log(list_of_recipes);
              // list_of_recipes.shift()
              setRecipes(list_of_recipes);
            }
          })
      }
    })
    .catch((err) => console.log(err));
  }, [])
  
  return (
    <div className="main">
      <h1 className="h1">Recommended Recipes</h1>
      {recipes.map((recipe) => (
      <div className="recipe_" key={recipe.id}>
        <div className="recipe_name">
          <h2>{recipe.name}</h2>
          </div>
          <div className="recipe_container">
            <div className="recipe_contain">
              <img className="image" src={recipe.img_url} />
              <h3 className="img_name">Image of {recipe.name}</h3>
              </div>
              <div className="recipe_instructions">
                <div className="recipe_ingredients">
                  <h3>Ingredients</h3>
                  {recipe.ingredients.join(",")}
                  </div>
                  <div className="recipe_directions">
                    <details>
                      <summary>Directions</summary>
                      <p>{recipe.directions.join(".")}</p>
                      </details>
                      </div>
                      </div>
                      </div>
                      </div>
                      ))}
                      </div>
                      );
  
   

  
}
export default RecipeCard;