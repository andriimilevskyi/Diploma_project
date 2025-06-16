import React, { useEffect, useContext } from "react";
import {useParams} from "react-router-dom"; // Для отримання параметра з URL
import './ProductDetails.css';
import useProducts from './hook';
import { CartContext } from "./CartContext";

const ProductDetails = () => {
    const { id } = useParams();
    const { products, loading, error } = useProducts();
    const { addToCart } = useContext(CartContext);

        useEffect(() => {
        localStorage.setItem("lastViewedProduct", id); // Зберігаємо ID
      }, [id]);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error.message}</div>;

    const product = products.find(p => p.id === Number(id)); // Переводимо id у число

    if (!product) return <div>Товар не знайдено</div>;

    const handleBuyClick = () => {
        addToCart(product); // Додаємо продукт до кошика
        alert('Товар додано до кошика!'); // Показуємо модальне вікно
    };

    return (
        <div className="product-details">
            <img src={product.preview_image} alt={product.series}/>
            <div className="description">
                <h1>{product.series}</h1>
                <p>Створений для складних маршрутів, гірських стежок і бездоріжжя, цей велосипед поєднує міцність,
                    легкість і комфорт. Надійна рама, амортизаційна вилка та потужні гальма забезпечують повний контроль
                    навіть у найекстремальніших умовах. З MTB ти відчуєш справжню свободу руху і
                    зможеш підкорити будь-який маршрут!</p>
                <p>{product.price}</p>
                <button onClick={handleBuyClick}>Купити!</button>
            </div>
        </div>
    );
};

export default ProductDetails;
