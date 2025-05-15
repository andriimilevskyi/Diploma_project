import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';
import './ConfigSelectorFork.css';
import './BikePreview.css';

const ConfigFork = () => {
  const [forks, setForks] = useState([]);
  const [selected, setSelected] = useState(null);

  const location = useLocation();
  const navigate = useNavigate();

  const { frame_id, frameImage } = location.state || {};

  useEffect(() => {
    if (!frame_id) {
      console.error("Frame ID is missing.");
      return;
    }

    const fetchForks = async () => {
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/conf/forks/?frame_id=${frame_id}`);
        const data = await res.json();
        setForks(data);
      } catch (err) {
        console.error("Помилка при завантаженні вилок:", err);
      }
    };

    fetchForks();
  }, [frame_id]);

  const handleButtonClick = (index) => {
    setSelected(index);
  };

  const handleNext = () => {
    if (selected === null) {
      alert("Оберіть вилку перед переходом.");
      return;
    }

    const selectedFork = forks[selected];

    console.log("Вибрана вилка:", selectedFork);
    // navigate('/configwheels', { state: { forkId: selectedFork.id } });
  };

  return (
    <div className="frame-selector">
      <div className="main-frame">
        <div className="frame-placeholder2">
          {frameImage && (
              <img src={frameImage} alt="Рама" className="frame-image" />
            )}
            {selected !== null && forks[selected] && (
              <img src={forks[selected].image} alt="Вилка" className="fork-overlay" />
            )}
        </div>
      </div>

      <div className="frame-options">
        {forks.map((fork, index) => (
          <button
            key={fork.id}
            className={`option-card-btn ${selected === index ? 'selected' : ''}`}
            onClick={() => handleButtonClick(index)}
          >
            <div className="option-card">
              <div className="frame-thumbnail2">
                <img src={fork.image} alt={fork.series} />
              </div>
              <div className="frame-info">
                <h4>{fork.series}</h4>
                <p>Тип: {fork.type}</p>
                <p>{fork.price}€</p>
              </div>
            </div>
          </button>
        ))}
      </div>

      <div className="navigation-buttons">
        <button className="prev-btn"><Link to="/configselector" className="next-link">← Назад</Link></button>
        <button className="next-btn" onClick={handleNext}>Далі →</button>
      </div>
    </div>
  );
};

export default ConfigFork;
