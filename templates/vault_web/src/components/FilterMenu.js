import React, { useState } from "react";
import "./FilterMenu.css";
import Slider from "rc-slider";
import "rc-slider/assets/index.css";

const FilterMenu = ({ filters, onFilterChange, onApplyFilters }) => {
  const [isFeaturesOpen, setIsFeaturesOpen] = useState(false);
  const [isColourOpen, setIsColourOpen] = useState(false);
  const [isPriceOpen, setIsPriceOpen] = useState(false);

  const toggleFeatures = () => setIsFeaturesOpen(!isFeaturesOpen);
  const toggleColour = () => setIsColourOpen(!isColourOpen);
  const togglePrice = () => setIsPriceOpen(!isPriceOpen);

  // Обробка чекбоксів
  const handleCheckboxChange = (e) => {
    const { id, checked } = e.target;
    if (id.startsWith("color-")) {
      const color = id.split("-")[1];
      onFilterChange({
        ...filters,
        colors: {
          ...filters.colors,
          [color]: checked,
        },
      });
    } else {
      onFilterChange({
        ...filters,
        [id]: checked,
      });
    }
  };

  // Обробка кліку для кольорів
  const handleColorClick = (color) => {
    onFilterChange({
      ...filters,
      colors: {
        ...filters.colors,
        [color]: !filters.colors[color],
      },
    });
  };

  // Обробка зміни ціни
  const handlePriceChange = (values) => {
    onFilterChange({
      ...filters,
      priceRange: { min: values[0], max: values[1] },
    });
  };

  return (
    <div className="filter-menu">
      <h2>Фільтр</h2>

      {/* Features Section */}
      <div className="filter-section">
        <div className="filter-header" onClick={toggleFeatures}>
          Цільове призначення
          <span className={`arrow ${isFeaturesOpen ? "open" : ""}`}>▼</span>
        </div>
        {isFeaturesOpen && (
          <ul className="filter-options">
            <li>
              <input
                type="checkbox"
                id="magsafe"
                checked={filters.magsafe}
                onChange={handleCheckboxChange}
              />
              MagSafe® Compatible
            </li>
            <li>
              <input
                type="checkbox"
                id="thin"
                checked={filters.thin}
                onChange={handleCheckboxChange}
              />
              Thin Protective
            </li>
            <li>
              <input
                type="checkbox"
                id="designs"
                checked={filters.designs}
                onChange={handleCheckboxChange}
              />
              Spec Designs
            </li>
          </ul>
        )}
      </div>

      {/* Colour Section */}
      <div className="filter-section">
        <div className="filter-header" onClick={toggleColour}>
          Колір
          <span className={`arrow ${isColourOpen ? "open" : ""}`}>▼</span>
        </div>
        {isColourOpen && (
          <div className="colour-options">
            <div
              className={`colour-circle black ${
                filters.colors.black ? "selected" : ""
              }`}
              onClick={() => handleColorClick("black")}
            ></div>
            <div
              className={`colour-circle blue ${
                filters.colors.blue ? "selected" : ""
              }`}
              onClick={() => handleColorClick("blue")}
            ></div>
            <div
              className={`colour-circle red ${
                filters.colors.red ? "selected" : ""
              }`}
              onClick={() => handleColorClick("red")}
            ></div>
            <div
              className={`colour-circle green ${
                filters.colors.green ? "selected" : ""
              }`}
              onClick={() => handleColorClick("green")}
            ></div>
            <div
              className={`colour-circle yellow ${
                filters.colors.yellow ? "selected" : ""
              }`}
              onClick={() => handleColorClick("yellow")}
            ></div>
            <div
              className={`colour-circle purple ${
                filters.colors.purple ? "selected" : ""
              }`}
              onClick={() => handleColorClick("purple")}
            ></div>
            <div
              className={`colour-circle orange ${
                filters.colors.orange ? "selected" : ""
              }`}
              onClick={() => handleColorClick("orange")}
            ></div>
          </div>
        )}
      </div>

      {/* Price Section */}
      <div className="filter-section">
        <div className="filter-header" onClick={togglePrice}>
          Ціна
          <span className={`arrow ${isPriceOpen ? "open" : ""}`}>▼</span>
        </div>
        {isPriceOpen && (
          <div className="price-slider">
            <Slider
              range
              min={0}
              max={100}
              defaultValue={[filters.priceRange.min, filters.priceRange.max]}
              onChange={handlePriceChange}
            />
            <div className="price-labels">
              <span>€{filters.priceRange.min}</span>
              <span>€{filters.priceRange.max}</span>
            </div>
          </div>
        )}
      </div>

      <div className="filter-section">
        <div className="filter-header" onClick={toggleFeatures}>
          Тип трансмісії
          <span className={`arrow ${isFeaturesOpen ? "open" : ""}`}>▼</span>
        </div>
        {isFeaturesOpen && (
          <ul className="filter-options">
            <li>
              <input
                type="checkbox"
                id="magsafe"
                checked={filters.magsafe}
                onChange={handleCheckboxChange}
              />
              MagSafe® Compatible
            </li>
            <li>
              <input
                type="checkbox"
                id="thin"
                checked={filters.thin}
                onChange={handleCheckboxChange}
              />
              Thin Protective
            </li>
            <li>
              <input
                type="checkbox"
                id="designs"
                checked={filters.designs}
                onChange={handleCheckboxChange}
              />
              Spec Designs
            </li>
          </ul>
        )}
      </div>

      <div className="filter-section">
        <div className="filter-header" onClick={toggleFeatures}>
          Розмір рами
          <span className={`arrow ${isFeaturesOpen ? "open" : ""}`}>▼</span>
        </div>
        {isFeaturesOpen && (
          <ul className="filter-options">
            <li>
              <input
                type="checkbox"
                id="magsafe"
                checked={filters.magsafe}
                onChange={handleCheckboxChange}
              />
              MagSafe® Compatible
            </li>
            <li>
              <input
                type="checkbox"
                id="thin"
                checked={filters.thin}
                onChange={handleCheckboxChange}
              />
              Thin Protective
            </li>
            <li>
              <input
                type="checkbox"
                id="designs"
                checked={filters.designs}
                onChange={handleCheckboxChange}
              />
              Spec Designs
            </li>
          </ul>
        )}
      </div>

      {/* Apply Filters Button */}
      <button className="apply-filters" onClick={onApplyFilters}>
        Застосувати
      </button>
    </div>
  );
};

export default FilterMenu;
