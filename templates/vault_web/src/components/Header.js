import React from "react";
import './Header.css';
import logo from "../assets/images/Logo.png";
import { Link } from "react-router-dom";

function Header() {
  return (
    <header className="header">
      <div className="header-div">
        <div className="logo"><img src={logo} alt="Logo" /></div>
        <nav className="nav">
            <ul>
                <li><Link to="/configmeasure" className="next-link">Configurator</Link></li>
            </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
