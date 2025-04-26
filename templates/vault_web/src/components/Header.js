import React from "react";
import './Header.css';
import logo from "../assets/images/Logo.png";
import { Link } from "react-router-dom";

function Header() {
  return (
    <header className="header">
      <div className="header-div">
        <Link to="/"><div className="logo"><img src={logo} alt="Logo" /></div></Link>
        <nav className="nav">
            <ul>
                <li><button className="next-btn"><Link to="/configmeasure" className="next-link">Configurator</Link></button></li>
            </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
