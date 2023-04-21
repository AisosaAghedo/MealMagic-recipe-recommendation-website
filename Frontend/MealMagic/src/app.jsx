import React from "react";
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

const router = createBrowserRouter(
  createRoutesFromElements(
    <>
      <Route>
        <Route path="/register" element={<Layout />} />
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
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

    