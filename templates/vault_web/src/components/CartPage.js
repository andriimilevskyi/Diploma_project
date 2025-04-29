import React, { useContext } from "react";
import { CartContext } from "./CartContext";

function CartPage() {
  const { cartItems, removeItem, clearCart } = useContext(CartContext);

  const totalPrice = cartItems.reduce((sum, item) => sum + Number(item.price), 0);

  return (
    <div style={{ marginLeft: '100px', marginRight: '100px'}}>
      <h1>Ваш кошик</h1>
      {cartItems.length === 0 ? (
        <p>Кошик порожній</p>
      ) : (
        <>
          {cartItems.map((item, index) => (

            <div key={index} style={{borderBottom: '1px solid gray', marginBottom: '10px', padding: '10px'}}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div style={{ display: 'flex'}}>
                  <img src={item.preview_image} alt={item.series} style={{width: '200px', borderRadius: '10px'}}/>
                  <div style={{ marginLeft: '10px' }}>
                      <h3>{item.series}</h3>
                      <p>{item.price}€</p>
                  </div>
                </div>
                <button style={{ fontSize: '20px', border: 'none', background: 'transparent', cursor: 'pointer', color: 'black', width: '40px' }}
                                 onClick={() => removeItem(index)}>X</button>
              </div>
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
