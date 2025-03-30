import React from "react";
import './ProductCard.css';

function ProductCard({ imgSrc, title, description, price }) {
  return (
    <div className="product-card">
      <img src={imgSrc} alt="Product" />
      <h3>{title}</h3>
      <p>{description}</p>
      <p>{price}</p>
    </div>
  );
}

export default ProductCard;