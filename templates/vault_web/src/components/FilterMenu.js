import React, { useState } from 'react';
import './FilterMenu.css';

const FilterMenu = () => {
  const [isFeaturesOpen, setIsFeaturesOpen] = useState(false);
  const [isColourOpen, setIsColourOpen] = useState(false);
  const [isPriceOpen, setIsPriceOpen] = useState(false);

  const toggleFeatures = () => setIsFeaturesOpen(!isFeaturesOpen);
  const toggleColour = () => setIsColourOpen(!isColourOpen);
  const togglePrice = () => setIsPriceOpen(!isPriceOpen);

  return (
    <div className="filter-menu">
      <h2>Filter & Sort</h2>

      {/* Features Section */}
      <div className="filter-section">
        <div className="filter-header" onClick={toggleFeatures}>
          Features
          <span className={`arrow ${isFeaturesOpen ? 'open' : ''}`}>▼</span>
        </div>
        {isFeaturesOpen && (
          <ul className="filter-options">
            <li><input type="checkbox" id="magsafe" /> MagSafe® Compatible</li>
            <li><input type="checkbox" id="printed" /> Printed Designs</li>
            <li><input type="checkbox" id="superthin" /> Super Thin</li>
            <li><input type="checkbox" id="ultra" /> Ultra Protective</li>
          </ul>
        )}
      </div>


      {/* Colour Section */}
      <div className="filter-section">
        <div className="filter-header" onClick={toggleColour}>
          Colour
          <span className={`arrow ${isColourOpen ? 'open' : ''}`}>▼</span>
        </div>
        {isColourOpen && (
          <div className="colour-options">
            <div className="colour-circle black"></div>
            <div className="colour-circle blue"></div>
            <div className="colour-circle red"></div>
            <div className="colour-circle green"></div>
            <div className="colour-circle yellow"></div>
            <div className="colour-circle purple"></div>
            <div className="colour-circle orange"></div>
          </div>
        )}
      </div>

      {/* Price Section */}
      <div className="filter-section">
        <div className="filter-header" onClick={togglePrice}>
          Price
          <span className={`arrow ${isPriceOpen ? 'open' : ''}`}>▼</span>
        </div>
        {isPriceOpen && (
          <div className="price-range">
            <input type="range" min="0" max="7999" />
            <div className="price-labels">
              <span>£0</span>
              <span>£100</span>
            </div>
          </div>
        )}
      </div>

      <button className="apply-filters">Apply Filters</button>
    </div>
  );
};

export default FilterMenu;