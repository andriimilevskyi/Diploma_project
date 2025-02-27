import React from "react";
import './App.css';
import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
import MainContentRealisator from "./components/MainContentRealisator";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProductDetails from './components/ProductDetails'; // Імпортуємо компонент для детальної інформації
import Configurator from "./components/Configurator";

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<MainContentRealisator />} />
          <Route path="/product/:id" element={<ProductDetails />} />
          <Route path="/configurator" element={<Configurator />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
