import React from "react";
import ProductCard from "./ProductCard";
import './ProductGrid.css';

function ProductGrid({ products }) {
  return (
    <section className="products-grid">
      {products.map((product) => (
        <ProductCard
          key={product.title}
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