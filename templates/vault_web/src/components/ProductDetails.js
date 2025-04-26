import React from "react";
import {useParams} from "react-router-dom"; // Для отримання параметра з URL
import './ProductDetails.css';
import useProducts from './hook';

const ProductDetails = () => {
    const { id } = useParams();
    const { products, loading, error } = useProducts();

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    const product = products.find(p => p.id === Number(id)); // Переводимо id у число

    if (!product) return <div>Product not found</div>;

    return (
        <div className="product-details">
            <img src={product.preview_image} alt={product.series}/>
            <div className="description">
                <h1>{product.series}</h1>
                <p>{product.description}</p>
                <p>{product.price}</p>
                <button>Buy Now</button>
            </div>
        </div>
    );
};

export default ProductDetails;
