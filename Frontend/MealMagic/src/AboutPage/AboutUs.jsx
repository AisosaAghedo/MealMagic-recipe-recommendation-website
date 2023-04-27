import React from "react";
import "./aboutus.css";
import Logo from '../assets/Logo.jpg';


const AboutUs = () => {
  return (
    <>
      <div id="about" className="section">
        <div className="about_container">
          <header className="section-header">
            <h2 className="section-title">About Us</h2>
            <p className="section-tagline">Everything about us</p>
          </header>
          <div className="section-body">
            <div className="row">
              <div className="col-1-2">
                <img src={Logo} alt="" width="460" height="460" />
              </div>
              <div className="col-1-2">
                <h3>Who are we</h3>
                <p className="p">
                  {" "}
                  MealMagic is a website that helps our users think! Yes, you
                  don't need to start thinking of what to make for breakfast,
                  lunch or dinner, Mealmagic helps to provide you with various
                  recipes from around the world using ingredients you already
                  have at home
                </p>
                <h3>Our culture</h3>
                <p className="p">
                  We don't only care about individual recipes, but about
                  planning and organizing entire meals for you and your friends
                  and family. With MealMagic, you can easily browse through a
                  vast collection of recipes, Whether you're a seasoned chef or just starting
                  out in the kitchen, MealMagic has everything you need to take
                  your cooking skills to the next level
                </p>
                <h3>How we work</h3>
                <p className="p">
                  MealMagic is Machine Learning based recipe recommendation
                  website that uses content-based filtering to provide
                  personalized recipe suggestions. Users will enter their
                  ingredients and get recommendation based ingredients they
                  entered
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div id="contact" className="section">
        <div className="container">
          <header className="section-header">
            <h2 className="section-title">Contact Us</h2>
            <p className="section-tagline">We’d love to hear from you!</p>
          </header>
        </div>
      </div>

      <footer className="footer" data-section-theme="dark">
        <div className="container">
          <div className="row">
            <div className="col-1-2">
              <address className="footer-address">
                <h3>Frontend Team</h3>
                Aisosa Aghedo
                <br />
                <a
                  href="https://github.com/AisosaAghedo"
                  className="github-link"
                >
                  Github
                </a>
                <br />
                <strong>Email : allysonaghedo@gmail.com </strong>
                <br />
                <br />
                Mustapha Olamide Usman
                <br />
                <a href="https://github.com/horlamyday" className="github-link">
                  Github
                </a>
                <br />
                <strong>Email : Horlamyday@gmail.com</strong>
              </address>
            </div>
            <div className="col-1-2">
              <address className="footer-address">
                <h3>Backend Team</h3>
                Yaekob Demisse
                <br />
                <a href="https://github.com/Jamescog" className="github-link">
                  Github
                </a>
                <br />
                <strong>Email : jamescog72@gmail.com </strong>
                <br />
                <br />
                Nosakhare Aghedo
                <br />
                <a href="https://github.com/Coder1967" className="github-link">
                  Github
                </a>
                <br />
                <strong>Email : nosakhareaghedo42@gmail.com </strong>
              </address>
            </div>
          </div>
        </div>
            {" "}
      </footer>
    </>
  );
}

export default AboutUs;
