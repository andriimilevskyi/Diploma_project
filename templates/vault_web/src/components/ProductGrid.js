import React from "react";
import ProductCard from "./ProductCard";
import './ProductGrid.css';
import { products } from "./products";

function ProductGrid() {
  return (
    <section className="products-grid">
      {products.map((product) => (
        <ProductCard
          id={product.id}
          key={product.id}
          imgSrc={product.imgSrc}
          title={product.title}
          description={product.description}
          price={product.price}
        />
      ))}
    </section>
  );
}

export default ProductGrid;
