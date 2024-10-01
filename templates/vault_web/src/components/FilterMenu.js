import React, { useState } from 'react';
import './FilterMenu.css';

const FilterMenu = ({ filters, onFilterChange, onApplyFilters }) => {
  const [isFeaturesOpen, setIsFeaturesOpen] = useState(false);
  const [isColourOpen, setIsColourOpen] = useState(false);

  const toggleFeatures = () => setIsFeaturesOpen(!isFeaturesOpen);
  const toggleColour = () => setIsColourOpen(!isColourOpen);

  // Обробка чекбоксів
  const handleCheckboxChange = (e) => {
    const { id, checked } = e.target;

    if (id.startsWith("color-")) {
      // Обробка кольорів через подію click
      const color = id.split('-')[1];
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

  // Обробка кліку для вибору кольору
  const handleColorClick = (color) => {
    onFilterChange({
      ...filters,
      colors: {
        ...filters.colors,
        [color]: !filters.colors[color], // Змінюємо стан кольору
      },
    });
  };

  const applyFilters = () => {
    onApplyFilters(); // Викликаємо функцію для застосування фільтрів
  };

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
            <li>
              <input type="checkbox" id="magsafe" checked={filters.magsafe} onChange={handleCheckboxChange} />
              MagSafe® Compatible
            </li>
            <li>
              <input type="checkbox" id="thin" checked={filters.thin} onChange={handleCheckboxChange} />
              Thin Protective
            </li>
            <li>
              <input type="checkbox" id="designs" checked={filters.designs} onChange={handleCheckboxChange} />
              Spec Designs
            </li>
          </ul>
        )}
      </div>

      {/* Colour Section */}
      <div className="filter-section">
        <div className="filter-header" onClick={toggleColour}>
          Color
          <span className={`arrow ${isColourOpen ? 'open' : ''}`}>▼</span>
        </div>
        {isColourOpen && (
          <div className="colour-options">
            <div className={`colour-circle black ${filters.colors.black ? 'selected' : ''}`} onClick={() => handleColorClick('black')}></div>
            <div className={`colour-circle blue ${filters.colors.blue ? 'selected' : ''}`} onClick={() => handleColorClick('blue')}></div>
            <div className={`colour-circle red ${filters.colors.red ? 'selected' : ''}`} onClick={() => handleColorClick('red')}></div>
            <div className={`colour-circle green ${filters.colors.green ? 'selected' : ''}`} onClick={() => handleColorClick('green')}></div>
            <div className={`colour-circle yellow ${filters.colors.yellow ? 'selected' : ''}`} onClick={() => handleColorClick('yellow')}></div>
            <div className={`colour-circle purple ${filters.colors.purple ? 'selected' : ''}`} onClick={() => handleColorClick('purple')}></div>
            <div className={`colour-circle orange ${filters.colors.orange ? 'selected' : ''}`} onClick={() => handleColorClick('orange')}></div>
          </div>
        )}
      </div>

      {/* Apply Filters Button */}
      <button className="apply-filters" onClick={applyFilters}>
        Apply Filters
      </button>
    </div>
  );
};

export default FilterMenu;