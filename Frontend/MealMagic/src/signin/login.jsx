import React from "react";
import Navbar from "../navbar/navbar";
import { Signin } from "./Signin";
const Login = () => {
  return (
    <>
      <Navbar />
      <div className="layout">
        <Signin />
      </div>
    </>
  );
};
export default Login;
