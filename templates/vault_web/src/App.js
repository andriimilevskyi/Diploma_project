import React from "react";
import './App.css';
import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ConfigMeasure from "./components/ConfigMeasure.js";
import ConfigDescipline from "./components/ConfigDescipline.js";
import ConfigSelector from "./components/ConfigSelector.js";
import MainContentRealisator from "./components/MainContentRealisator";
import ProductDetails from './components/ProductDetails';


function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<MainContentRealisator />} />
          <Route path="/configmeasure" element={<ConfigMeasure />} />
          <Route path="/configdescipline" element={<ConfigDescipline />} />
          <Route path="/configselector" element={<ConfigSelector />} />
          <Route path="/product/:id" element={<ProductDetails />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
