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


const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route>
        <Route path="/register" element={<Layout />} />
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login/>} />
        <Route path="/Recipe/:ingredients" element={<Recipe />} />
        <Route path="/About" element={<About/>} />
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

    