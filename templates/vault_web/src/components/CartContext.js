import React, { createContext, useState, useEffect } from "react";

export const CartContext = createContext();

export function CartProvider({ children }) {
  const savedCartItems = JSON.parse(localStorage.getItem("cartItems")) || [];

  const [cartItems, setCartItems] = useState(savedCartItems);

  useEffect(() => {
    localStorage.setItem("cartItems", JSON.stringify(cartItems));
  }, [cartItems]);

  const addToCart = (product) => {
    setCartItems(prev => [...prev, product]);
  };

  const clearCart = () => {
    setCartItems([]);
  };

  const removeItem = (index) => {
    setCartItems((prevItems) => prevItems.filter((_, i) => i !== index));
  };

  return (
    <CartContext.Provider value={{ cartItems, addToCart, removeItem, clearCart }}>
      {children}
    </CartContext.Provider>
  );
}
