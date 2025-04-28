import React, { useState } from "react";
import './Header.css';
import logo from "../assets/images/Logo.png";
import { Link } from "react-router-dom";
import AuthModal from "./AuthModal";

function Header() {

    const [showAuth, setShowAuth] = useState(false);

  return (
    <header className="header">
      <div className="header-div">
        <Link to="/"><div className="logo"><img src={logo} alt="Logo" /></div></Link>
        <nav className="nav">
            <ul>
                <li><button className="auth-btn" onClick={() => setShowAuth(true)}>Вхід / Реєстрація</button></li>
            </ul>
            <ul>
                <li><button className="cart-btn"><Link to="/cart" className="cart-link">Кошик</Link></button></li>
            </ul>
            <ul>
                <li><button className="next-btn"><Link to="/configmeasure" className="next-link">Конфігуратор</Link></button></li>
            </ul>
        </nav>
      </div>
      {showAuth && <AuthModal onClose={() => setShowAuth(false)} />}
    </header>
  );
}

export default Header;
