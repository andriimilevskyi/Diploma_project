import React from "react";
import './Header.css';

function Header() {
  return (
    <header className="header">
      <div className="header-div">
        <div className="logo">Vault</div>
        <nav className="nav">
          <ul>
            <li>Cases & Accessories</li>
            <li>Bags & Pouches</li>
            <li>Mounts & Chargers</li>
            <li>Sale</li>
          </ul>
        </nav>
        <div className="user-actions">
          <span>🌐</span>
          <span>€</span>
          <span>❤️</span>
          <span>👤</span>
          <span>🛒</span>
        </div>
      </div>
    </header>
  );
}

export default Header;
