import React, { useContext } from "react";
import { CartContext } from "./CartContext";

function CartPage() {
  const { cartItems, clearCart } = useContext(CartContext);

  const totalPrice = cartItems.reduce((sum, item) => sum + Number(item.price), 0);

  return (
    <div>
      <h1>Ваш кошик</h1>
      {cartItems.length === 0 ? (
        <p>Кошик порожній</p>
      ) : (
        <>
          {cartItems.map((item, index) => (
            <div key={index} style={{border: '1px solid gray', marginBottom: '10px', padding: '10px'}}>
              <img src={item.preview_image} alt={item.series} style={{width: '500px'}}/>
              <h3>{item.series}</h3>
              <p>{item.price}€</p>
            </div>
          ))}
          <div style={{marginBottom: '100px'}}>
              <h2>Всього: {totalPrice}€</h2>
              <button onClick={clearCart}>Оплатити</button>
          </div>
        </>
      )}
    </div>
  );
}

export default CartPage;
