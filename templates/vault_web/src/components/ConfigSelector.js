import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';
import './ConfigSelectorFrame.css';

const ConfigSelector = () => {
    const [frames, setFrames] = useState([]);
    const [selected, setSelected] = useState(null);

    const location = useLocation();
    const navigate = useNavigate();

    const { height, inseam, discipline } = location.state || {};

    useEffect(() => {
        if (!height || !inseam || !discipline) return;

        const apiUrl = `http://127.0.0.1:8000/api/conf/frames/?discipline=${discipline}&height=${height}&inseam=${inseam}`;
        fetch(apiUrl)
            .then(res => res.json())
            .then(data => setFrames(data))
            .catch(err => console.error("Fetch error:", err));
    }, [height, inseam, discipline]);

    const handleButtonClick = (index) => {
        setSelected(index);
    };

    const handleNext = () => {
        if (selected !== null) {
          const selectedFrame = frames[selected];
          navigate("/configfork", {
            state: {
              frame_id: selectedFrame.id
            }
          });
        } else {
          alert("Будь ласка, оберіть раму перед переходом далі.");
        }
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
                <button className="prev-btn"><Link to="/configdescipline" className="next-link">← Назад</Link></button>
                <button className="next-btn" onClick={handleNext}>Далі →</button>
            </div>
        </div>
    );
};

export default ConfigSelector;
