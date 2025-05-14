import React, { useState, useEffect } from 'react';
import { useLocation, Link } from "react-router-dom";
import './ConfigSelector.css';

const ConfigSelector = () => {
  const [frames, setFrames] = useState([]);
  const [selected, setSelected] = useState(null);

  // Отримуємо стан із попередньої форми, якщо він є
  const location = useLocation();
  const { height, inseam, discipline } = location.state || { height: 180, inseam: 70, discipline: 1 };

  useEffect(() => {
    const fetchFrames = () => {
      const apiUrl = `http://127.0.0.1:8000/api/conf/frames/?discipline=${discipline}&height=${height}&inseam=${inseam}`;
      fetch(apiUrl, {
        method: "GET",
        headers: {
          "Accept": "application/json",
          "X-CSRFToken": "F8bcVkhrUT1tt3W8kpGcxzan1zxtQ9KQ38nblbEwaHxnTbdiOfbfI6gbcYqcOKlAQ"
        }
      })
        .then(res => res.json())
        .then(data => setFrames(data))
        .catch(err => console.error("Fetch error:", err));
    };

    fetchFrames();
  }, [height, inseam, discipline]); // Перезавантажувати дані, коли height, inseam або discipline змінюються

  const handleButtonClick = (index) => {
    setSelected(index);
  };

  return (
    <div className="frame-selector">
      <div className="main-frame">
        <div className="frame-placeholder">
          {selected !== null && frames[selected] ? (
            <img src={frames[selected].image} alt="frame" />
          ) : (
            <p>Оберіть раму справа</p>
          )}
        </div>
      </div>

      <div className="frame-options">
        {frames.map((frame, index) => (
          <button
            key={index}
            className={`option-card-btn ${selected === index ? 'selected' : ''}`}
            onClick={() => handleButtonClick(index)}
          >
            <div className="option-card">
              <div className="frame-thumbnail">
                <img src={frame.image} alt={frame.series} />
              </div>
              <div className="frame-info">
                <h4>{frame.series}</h4>
                <p>Size: {frame.size}</p>
                <p>{frame.price}€</p>
              </div>
            </div>
          </button>
        ))}
      </div>

      <div className="navigation-buttons">
        <button className="prev-btn">
          <Link to="/configdescipline" className="next-link">← Назад</Link>
        </button>
        <button className="next-btn">
          <Link to="/confige" className="next-link">Далі →</Link>
        </button>
      </div>
    </div>
  );
};

export default ConfigSelector;
