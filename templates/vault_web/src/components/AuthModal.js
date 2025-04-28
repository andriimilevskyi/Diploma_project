import React from "react";
import './AuthModal.css'; // окремі стилі для модалки (можна скопіювати з App.css)

function AuthModal({ onClose }) {
  return (
    <div className="auth-modal">
      <div className="auth-content">
        <button onClick={onClose}>X</button>
        <h2>Вхід / Реєстрація</h2>
        <form>
          <input type="email" placeholder="Email" required />
          <input type="password" placeholder="Пароль" required />
          <button type="submit">Увійти</button>
          <button type="button">Зареєструватися</button>
        </form>
      </div>
    </div>
  );
}

export default AuthModal;
