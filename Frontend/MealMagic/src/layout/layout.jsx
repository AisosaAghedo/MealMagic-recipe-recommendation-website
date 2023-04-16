import React from 'react';
import Navbar from '../navbar/navbar'
// import Logo from '../logo/logo'
import SignupDesign from '../Signup/signup.design';
import './layout.css'
const Layout = () => {
 return (
   <>
     <Navbar />
     <div className="layout">
       <SignupDesign />
     </div>
   </>
 );
}
export default Layout;