import React from "react";
import ProductCard from "./ProductCard";
import './ProductGrid.css';
import useProducts from './hook';

function ProductGrid({ products }) {
  if (!products || products.length === 0) return <div>Немає доступних продуктів.</div>;

  return (
    <section className="products-grid">
      {products.map((product) => (
        <ProductCard
          key={product.id}
          id={product.id}
          image={product.preview_image}
          series={product.series}
          description={product.description}
          price={product.price}
        />
      ))}
    </section>
  );
}

export default ProductGrid;