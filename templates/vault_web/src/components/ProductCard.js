import React from "react";
import './ProductCard.css';
import { Link } from 'react-router-dom';

function ProductCard({ id, image, series, description, price }) {
  return (
    <div className="product-card">
      <Link
        to={`/product/${id}`}
        onClick={() => sessionStorage.setItem("lastViewedProduct", id)}
      >
        <img src={image} alt="Product" />
        <h3>{series}</h3>
        <p>{description}</p>
        <p>{price}€</p>
      </Link>
    </div>
  );
}

export default ProductCard;
