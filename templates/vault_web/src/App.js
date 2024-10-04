import React from "react";
import './App.css';
import Header from "./components/Header.js";
import Footer from "./components/Footer.js";
import MainContentRealisator from "./components/MainContentRealisator";

function App() {
    return (
      <div className="App">
        <Header />

        <div className="main-content">
          <MainContentRealisator />
        </div>

        <Footer />
      </div>
    );
  }

export default App;