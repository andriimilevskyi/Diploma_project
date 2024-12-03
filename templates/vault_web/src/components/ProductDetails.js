import React  from "react";
import { useParams } from "react-router-dom"; // Для отримання параметра з URL
import { products } from "./products";

const ProductDetails = () => {
  const { id } = useParams(); // Отримуємо ID продукту з URL

  // Знайдемо продукт за ID
  const product = products.find(p => p.id.toString() === id);

  if (!product) {
    return <div>Product not found</div>;
  }

  return (
    <div className="product-details">
      <img src={product.imgSrc} alt={product.title} />
      <h1>{product.title}</h1>
      <p>{product.description}</p>
      <p>{product.price}</p>
      <button>Buy Now</button>
    </div>
  );
};

export default ProductDetails;