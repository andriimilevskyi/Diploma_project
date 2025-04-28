import React, { useState } from 'react';
import './ConfigSelector.css';
import { Link } from "react-router-dom";
import frameImage1 from '../assets/images/G53989_JEALOUS_CF_RA2500_800x800@2x.jpg';
import frameImage2 from '../assets/images/d983ad9e5edbe3b7.png';
import frameImage3 from '../assets/images/8519aaa9fd63ba3e.png';
import frameImage4 from '../assets/images/sticker 2.png';

const ConfigSelector = () => {
  // Стан для відстеження вибраної кнопки
  const [selected, setSelected] = useState(null);

  // Обробник для натискання кнопки
  const handleButtonClick = (index) => {
    setSelected(index === selected ? null : index); // Вибір нової кнопки або скидання вибору
  };

  return (
    <div className="frame-selector">
      <div className="main-frame">
        <div className="frame-placeholder"><img src={frameImage4} alt="frame" /></div>
      </div>

      <div className="frame-options">
        {[frameImage1, frameImage2, frameImage3, frameImage4, frameImage1, frameImage1].map((image, index) => (
          <button
            key={index}
            className={`option-card-btn ${selected === index ? 'selected' : ''}`}
            onClick={() => handleButtonClick(index)}
          >
            <div className="option-card">
              <div className="frame-thumbnail"><img src={image} alt="frame" /></div>
              <div className="frame-info">
                <h4>BC ORIGINAL FLINT</h4>
                <p>Size = M</p>
                <p>449.00€</p>
              </div>
            </div>
          </button>
        ))}
      </div>

      <div className="navigation-buttons">
        <button className="prev-btn"><Link to="/configdescipline" className="next-link">← Назад</Link></button>
        <button className="next-btn"><Link to="/confige" className="next-link">Далі →</Link></button>
      </div>
    </div>
  );
};

export default ConfigSelector;
