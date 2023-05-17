import React, { useEffect, useState } from "react";
import { styled } from "styled-components";
import { useParams } from "react-router-dom";
import Navbar from "./navbar/navbar";

const Recipe_details = () => {
  let params = useParams();
  const [details, setDetails] = useState({});
  const [activeTab, setActiveTab] = useState("directions")

  const requestOptions = {
    method: "POST",
    headers: {
      "content-type": "application/json",
    },
    body: JSON.stringify({ name: `${params.name}` }),
  };
  useEffect(() => {
    let i = 0;
    let list_of_recipes = [];
    fetch("http://localhost:5000/api/meal_magic/get_recipes", requestOptions)
      .then((res) => res.json())
      .then((data) => {
        // console.log(data)
        setDetails(data);
        // console.log(details)
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <>
      <Navbar />
      <Wrapper>
        <div>
          <h2>{details.name}</h2>
          <img src={details.img_url} alt={details.name} />
        </div>
        <Info>
          <Button
            className={activeTab === "ingredients" ? "active" : ""}
            onClick={() => setActiveTab("ingredients")}
          >
            Ingredients
          </Button>
          <Button
            className={activeTab === "directions" ? "active" : ""}
            onClick={() => setActiveTab("directions")}
          >
            Instructions
          </Button>
          {activeTab === "ingredients" && (
            <ul key={details.id}>
              {details.ingredients.map((ingredient) => (
                <li>{ingredient}</li>
              ))}
            </ul>
          )}

          {activeTab === "directions" && (
            <ol key={details.key}>
              {details.directions?.map((direction) => (
                <li>{direction}</li>
              ))}
            </ol>
          )}
        </Info>
      </Wrapper>
    </>
  );
};

const Wrapper = styled.div`
  margin-top: 5rem;
  margin-bottom: 5rem;
  display: flex;

  @media (max-width: 1068px) {
    flex-direction: column;
  }

  .active {
    background: linear-gradient(35deg, #494949, #313131);
    color: #fff;
  }
  img {
    width: 20rem;
    height: 20rem;
  }

  h2 {
    margin-bottom: 2rem;
  }

  ul, ol {
    margin-top: 2rem;
    width: 50vw;
  }

  li {
    font-size: 1rem;
    line-height: 2.5rem;
  }

  p {
    margin: 1rem 0;
    font-size: 1.1rem;
    line-height: 1.8rem;

    &:first-child {
      margin-top: 2rem;
    }
  }
`;

const Button = styled.button`
  padding: 1rem 2rem;
  color: #313131;
  background: #fff;
  border: 2px solid #000;
  margin-right: 2rem;
  font-weight: 600;
`;

const Info = styled.div`
  margin-left: 5rem;

  @media (max-width: 1068px) {
    margin-top: 3rem;
    margin-left: 1rem;
  }
`;


export default Recipe_details;
