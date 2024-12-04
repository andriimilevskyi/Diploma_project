import React from "react";
import {useParams} from "react-router-dom"; // Для отримання параметра з URL
import './ProductDetails.css';
// import {products} from "./products";
import useProducts from './hook';

const ProductDetails = () => {
    const {id} = useParams(); // Отримуємо ID продукту з URL

    const {products, loading, error} = useProducts();

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    // Знайдемо продукт за ID
    const product = products.find(p => p.id.toString() === id);

    if (!product) {
        return <div>Product not found</div>;
    }

    return (
        <div className="product-details">
            <img src={product.image} alt={product.title}/>
            <div className="description">
                <h1>{product.title}</h1>
                <p>{product.description}</p>
                <p>{product.price}</p>
                <button>Buy Now</button>
            </div>
        </div>
    );
};

export default ProductDetails;