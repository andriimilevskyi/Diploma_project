import React from "react";
import ProductCard from "./ProductCard";
import './ProductGrid.css';

function ProductGrid() {
  return (
    <section className="products-grid">
      <ProductCard
        imgSrc={require("../images/fibre.jpg")}
        title="SAVIOR"
        description="MagSafe® Compatible Aramid Fibre Phone Case"
        price="€34,99"
      />
      <ProductCard
        imgSrc={require("../images/plastic.png")}
        title="CARRION"
        description="MagSafe® Compatible Clear Phone Case"
        price="€69,99"
      />
      <ProductCard
        imgSrc={require("../images/silicon.jpg")}
        title="INLOCK"
        description="Phone Case"
        price="€59,99"
      />
      <ProductCard
        imgSrc={require("../images/bringin.jpg")}
        title="BRINGIN"
        description="MagSafe® Compatible Carbon Fibre Case"
        price="€59,99"
      />
      <ProductCard
        imgSrc={require("../images/defense.jpg")}
        title="DEFENSE"
        description="Heavy Duty Defense Case"
        price="€79,99"
      />
      <ProductCard
        imgSrc={require("../images/holden.jpg")}
        title="HOLDEN"
        description="Shockproof Alpha Case"
        price="€49,99"
      />
    </section>
  );
}

export default ProductGrid;
