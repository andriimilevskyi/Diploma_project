import React from 'react';
import './ConfigSelector.css';
import { Link } from "react-router-dom";

const ConfigSelector = () => {
  return (
    <div className="frame-selector">
      <div className="main-frame">
        <div className="frame-placeholder">Frame Preview</div>
      </div>

      <div className="frame-options">
        <div className="option-card">
          <div className="frame-thumbnail">[Image]</div>
          <div className="frame-info">
            <h4>BC ORIGINAL FLINT</h4>
            <p>Size = L</p>
            <p>449.00€</p>
          </div>
        </div>

        <div className="option-card">
          <div className="frame-thumbnail">[Image]</div>
          <div className="frame-info">
            <h4>BC ORIGINAL FLINT</h4>
            <p>Size = M</p>
            <p>449.00€</p>
          </div>
        </div>

        <div className="option-card">
          <div className="frame-thumbnail">[Image]</div>
          <div className="frame-info">
            <h4>BC ORIGINAL FLINT</h4>
            <p>Size = M</p>
            <p>449.00€</p>
          </div>
        </div>

        <div className="option-card">
          <div className="frame-thumbnail">[Image]</div>
          <div className="frame-info">
            <h4>BC ORIGINAL FLINT</h4>
            <p>Size = M</p>
            <p>449.00€</p>
          </div>
        </div>

        <div className="option-card">
          <div className="frame-thumbnail">[Image]</div>
          <div className="frame-info">
            <h4>BC ORIGINAL FLINT</h4>
            <p>Size = M</p>
            <p>449.00€</p>
          </div>
        </div>

        <div className="option-card">
          <div className="frame-thumbnail">[Image]</div>
          <div className="frame-info">
            <h4>BC ORIGINAL FLINT</h4>
            <p>Size = M</p>
            <p>449.00€</p>
          </div>
        </div>
      </div>

      <div className="navigation-buttons">
        <button className="prev-btn"><Link to="/configdescipline" className="next-link">← Previous</Link></button>
        <button className="next-btn"><Link to="/confige" className="next-link">Next →</Link></button>
      </div>
    </div>
  );
};

export default ConfigSelector;
