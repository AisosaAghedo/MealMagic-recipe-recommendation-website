import React from "react";
import "./aboutus.css";
import Logo from '../assets/Logo.jpg';


const AboutUs = () => {
  return (
    <>
      <div id="about" className="section">
      <div className="container">
          <header className="section-header">
            <h2 className="section-title">About Us</h2>
            <p className="section-tagline">Everything about us</p>
          </header>
          <div className="section-body">
            <div className="row">
              <div className="col-1-2">
                  <img src={Logo} alt="" width="460" height="460"/>
                </div>
            <div className="col-1-2">
              <h3>Who are we</h3>
              <p className="p">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p>
              <h3>Our culture</h3>
              <p className="p">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p>
              <h3>How we work</h3>
              <p className="p">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsum, omnis expedita! Eum, praesentium cumque accusantium rem, sit quaerat est nisi ratione, deserunt ducimus quidem iste dicta quibusdam atque maxime cum!</p>
            </div>
          </div>
        </div>
        </div>
      </div>
      <div id="contact" className="section">
        <div className="container">
          <header className="section-header">
            <h2 className="section-title">Contact</h2>
            <p className="section-tagline">We’d love to hear from you!</p>
          </header>
        </div>
      </div>
      
      <footer className="footer" data-section-theme="dark">
      <div  className="container">
        <div className="row">
          <div className="col-1-2">
           
            <address className="footer-address">
                <h3>Frontend Team</h3>
              Aisisa Aghedo<br />
              <a href="https://github.com/AisosaAghedo" className="github-link">Github</a><br />
              <strong>Email : allysonaghedo@gmail.com </strong><br /><br />
              Mustapha Olamide Usman<br />
              <a href="https://github.com/horlamyday" className="github-link">Github</a><br />
              <strong>Email : Horlamyday@gmail.com</strong>
              
            </address>
          </div>
          <div className="col-1-2">
            <address className="footer-address">
                <h3>Bankend Team</h3>
                Yaekob Demisse<br />
              <a href="https://github.com/Jamescog" className="github-link">Github</a><br />
              <strong>Email : jamescog72@gmail.com </strong><br /><br />
              Nosakhare Aghedo<br />
              <a href="https://github.com/Coder1967" className="github-link">Github</a><br />
              <strong>Email : nosakhareaghedo42@gmail.com </strong>
            </address>
          </div>
        </div>
        </div>
        </footer>   
  </>

  );
}

export default AboutUs;
