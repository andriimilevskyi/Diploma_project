import React from "react";
import ProductCard from "./ProductCard";
import './ProductGrid.css';
// import {products} from "./products";
import useProducts from './hook';


function ProductGrid() {
  const { products, loading, error } = useProducts();

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <section className="products-grid">
      {products.map((product) => (
        <ProductCard
          id={product.id}
          key={product.id}
          image={product.image}
          title={product.title}
          description={product.description}
          price={product.price}
        />
      ))}
      {/*<ProductGrid products={products} />*/}
    </section>
  );
}

export default ProductGrid;
