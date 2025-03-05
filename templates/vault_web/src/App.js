import React from "react";
import './App.css';
import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ConfigMeasure from "./components/ConfigMeasure.js";
import ConfigDescipline from "./components/ConfigDescipline.js";

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/configmeasure" element={<ConfigMeasure />} />
          <Route path="/configdescipline" element={<ConfigDescipline />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
