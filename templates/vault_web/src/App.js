import React, { useState } from "react";
import FilterMenu from "./components/FilterMenu";
import ProductGrid from "./components/ProductGrid";
import "./App.css";
import Header from "./components/Header";
import Footer from "./components/Footer";

function App() {
  const [filterMagSafe, setFilterMagSafe] = useState(false);

  const handleFilterChange = (isMagSafeCompatible) => {
    setFilterMagSafe(isMagSafeCompatible);
  };

  return (
    <div className="App">
      <Header />

      <div className="main-content">
        <FilterMenu onFilterChange={handleFilterChange} />
        <ProductGrid filterMagSafe={filterMagSafe} />
      </div>
      
      <Footer />
    </div>
  );
}

export default App;