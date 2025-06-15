import React from "react";
import './App.css';
import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { ConfigContext, ConfigProvider } from './components/ConfigContext.js'
import ConfigMeasure from "./components/ConfigMeasure.js";
import ConfigDescipline from "./components/ConfigDescipline.js";
import ConfigSelector from "./components/ConfigSelector.js";
import ConfigFork from "./components/ConfigFork.js";
import MainContentRealisator from "./components/MainContentRealisator";
import ProductDetails from './components/ProductDetails';
import CartPage from "./components/CartPage";

function App() {
  return (
    <ConfigProvider>
        <Router>
          <div className="App">
            <Header />
            <Routes>
              <Route path="/" element={<MainContentRealisator />} />
              <Route path="/configmeasure" element={<ConfigMeasure />} />
              <Route path="/configdescipline" element={<ConfigDescipline />} />
              <Route path="/configselector" element={<ConfigSelector />} />
              <Route path="/configfork" element={<ConfigFork />} />
              <Route path="/product/:id" element={<ProductDetails />} />
              <Route path="/cart" element={<CartPage />} />
            </Routes>
            <Footer />
          </div>
        </Router>
    </ConfigProvider>
  );
}

export default App;
