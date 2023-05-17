import React, {useState, useEffect} from "react";
import { useParams } from 'react-router-dom';
import {Audio, Oval} from 'react-loader-spinner';
import styled from 'styled-components';
import {Splide, SplideSlide} from '@splidejs/react-splide';
import "@splidejs/splide/dist/css/splide.min.css"
import { Link } from "react-router-dom";
import Recipe_details from "../recipe-details";
import './Recipe.css'



const RecipeCard = () => {
  const [recipes, setRecipes] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  function getRecipes() {
    const { ingredients } = useParams();
    return (ingredients)
    // console.log(ingredients);
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
        setIsLoading(true);
        fetch("http://localhost:5000/api/meal_magic/get_recipes", fetchOptions)
          .then((res) => res.json())
          .then((data) => {
            i++;
            list_of_recipes.push(data);
             
            if (i === 10){
              console.log(list_of_recipes);
             
              setRecipes(list_of_recipes);
              setIsLoading(false);
            }
          })
      }
    })
    .catch((err) => console.log(err));
    
  }, [])
  return (
    <>
      {!isLoading ? (
        <Wrapper>
          <h1>Recommended Recipes</h1>
          <Splide
            options={{
              perPage: 3,
              pagination: false,
              drag: "free",
              gap: "5rem",
              breakpoints: {
                900: {
                  perPage: 2,
                },
                640: {
                  perPage: 1,
                },
              },
            }}
          >
            {recipes.map((recipe) => {
              return (
                <SplideSlide key={recipe.id}>
                  <Card>
                    <Link to={"/Recipe_details/" + recipe.name}>
                      <Gradient></Gradient>
                      <p>{recipe.name}</p>
                      <img src={recipe.img_url} alt={recipe.name} />
                    </Link>
                  </Card>
                </SplideSlide>
              );
            })}
          </Splide>
        </Wrapper>
      ) : (
        <Oval
          width={80}
          height={80}
          ariaLabel="loading"
          wrapperClass="wrapper-class"
          wrapperStyle={{}}
        />
      )}
    </>
  );
  
}
const Wrapper = styled.div`
  margin: 4rem 0rem;
  height: 100vh;
  width:100vw;

  h1 {
    text-align: center;
    margin-bottom: 1rem;
  }
`;

const Card = styled.div`
  overflow: hidden;
  position: relative;
  height: 80vh;
  border-radius: 2rem;
  display: flex;
  img {
    border-radius: 1rem;
    position: absolute;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    
  }
  p {
    position: absolute;
    z-index: 10;
    left: 50%;
    bottom: 0%;
    transform: translate(-50%, 0%);
    color: white;
    width: 100%;
    text-align: center;
    font-weight: 600;
    font-size: 2rem;
    height: 40%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
`;
const Gradient = styled.div`
  z-index: 3;
  position: absolute;
  width: 100%;
  height: 100%;
  background: linear-gradient(rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.5));
  
`;

export default RecipeCard;