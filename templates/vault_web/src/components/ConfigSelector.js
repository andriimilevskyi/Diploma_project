import React, { useState, useEffect, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { ConfigContext } from '../components/ConfigContext.js'
import './ConfigSelectorFrame.css';

const ConfigSelector = () => {
  const { config, updateConfig } = useContext(ConfigContext);
  const [frames, setFrames] = useState([]);
  const [selected, setSelected] = useState(null);

  const navigate = useNavigate();

  useEffect(() => {
    if (!config.height || !config.inseam || !config.discipline) {
    console.log('Waiting for all params:', {height: config.height, inseam: config.inseam, discipline: config.discipline});
    return;
  }
    const apiUrl = `http://127.0.0.1:8000/api/conf/frames/?discipline=${config.discipline}&height=${config.height}&inseam=${config.inseam}`;
    console.log('Fetching frames from:', apiUrl);
    fetch(apiUrl)
      .then(res => res.json())
      .then((data) => {
        console.log('Frames received:', data);
        setFrames(data);
        // Відновлюємо selected по id, якщо frame вже обраний
        if (config.frame) {
          const index = data.findIndex(f => f.id === config.frame.id);
          setSelected(index !== -1 ? index : null);
        }
      })
      .catch(err => console.error("Fetch error:", err));
  }, [config]);

  useEffect(() => {
    if (config.frame && frames.length > 0) {
      const index = frames.findIndex(f => f.id === config.frame.id);
      setSelected(index !== -1 ? index : null);
    }
  }, [frames, config.frame]);

  const handleButtonClick = (index) => {
    setSelected(index);
  };

  const handleNext = () => {
    if (selected !== null) {
      const selectedFrame = frames[selected];
      updateConfig({ frame: selectedFrame });
      navigate("/configfork");
    } else {
      alert("Будь ласка, оберіть раму перед переходом далі.");
    }
  };

  const handlePrev = () => {
    navigate("/configdescipline");
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
        <button className="prev-btn" onClick={handlePrev}>← Назад</button>
        <button className="next-btn" onClick={handleNext}>Далі →</button>
      </div>
    </div>
  );
};

export default ConfigSelector;
