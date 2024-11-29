import React from "react";
import { useParams } from "react-router-dom"; // Для отримання параметра з URL

const ProductDetails = () => {
  const { id } = useParams(); // Отримуємо ID продукту з URL
  const products = [
    {
      id: 1,
      imgSrc: require("../images/fibre.jpg"),
      title: "SAVIOR",
      description: "MagSafe® Compatible Aramid Fibre Phone Case",
      price: "€34,99",
      tags: ["magsafe"],
      color: "green",
    },
    {
      id: 2,
      imgSrc: require("../images/plastic.png"),
      title: "CARRION",
      description: "MagSafe® Compatible Clear Phone Case",
      price: "€69,99",
      tags: ["magsafe", "designs"],
      color: "black",
    },
    // Інші продукти
  ];

  // Знайдемо продукт за ID
  const product = products.find(product => product.id === parseInt(id));

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