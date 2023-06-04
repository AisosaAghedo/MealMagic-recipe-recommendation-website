import React, {useState} from "react";
import {
  Route,
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";
import Home from "./Home/home";
import "./index.css";
import Layout from "./layout/layout";
import Login from "./signin/login";
import Recipe from "./Recipepage/Recipe";
import About from "./AboutPage/About";
import Recipe_details from "./Recipepage/recipe-details";


const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route>
        <Route path="/register" element={<Layout />} />
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/Recipe/:ingredients" element={<Recipe />} />
        <Route path="/Recipe_details/:name" element={<Recipe_details />} />
        <Route path="/About" element={<About />} />
      </Route>
    </>
  )
);

function App({ routes }) {
  return (
    <>
      <RouterProvider router={router} />
    </>
  );
}
export default App;

    