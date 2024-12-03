import React from "react";
import { Link } from "react-router-dom"; // Імпортуємо Link для переходу на іншу сторінку
import './ProductCard.css';

function ProductCard({ id, imgSrc, title, description, price }) {
  return (
    <div className="product-card">
      <Link to={`/product/${id}`}> {/* Посилання на сторінку з детальною інформацією про продукт */}
        <img src={imgSrc} alt={title} />
        <h3>{title}</h3>
        <p>{description}</p>
        <p>{price}</p>
      </Link>
      <button>Buy</button>
    </div>
  );
}

export default ProductCard;