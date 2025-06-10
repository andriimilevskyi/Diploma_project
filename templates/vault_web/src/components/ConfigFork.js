import React, { useState, useEffect, useContext } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { ConfigContext } from './ConfigContext';
import './ConfigSelectorFork.css';
import './BikePreview.css';

const ConfigFork = () => {
  const [forks, setForks] = useState([]);
  const [selected, setSelected] = useState(null);

  const navigate = useNavigate();
  const { config, updateConfig } = useContext(ConfigContext);
  const frame = config.frame;

  useEffect(() => {
    if (!frame?.id) {
      console.error("Frame ID is missing.");
      return;
    }

    const fetchForks = async () => {
      try {
        const res = await fetch(`http://127.0.0.1:8000/api/conf/forks/?frame_id=${frame.id}`);
        const data = await res.json();
        setForks(data);

        // Якщо вилка вже вибрана — встановити її як вибрану
        const preSelectedIndex = data.findIndex(f => f.id === config.fork?.id);
        if (preSelectedIndex >= 0) {
          setSelected(preSelectedIndex);
        }
      } catch (err) {
        console.error("Помилка при завантаженні вилок:", err);
      }
    };

    fetchForks();
  }, [frame, config.fork]);

  const handleButtonClick = (index) => {
    setSelected(index);
  };

  const handleNext = () => {
    if (selected === null) {
      alert("Оберіть вилку перед переходом.");
      return;
    }

    const selectedFork = forks[selected];
    updateConfig({ fork: selectedFork });
    navigate('/configwheels'); // Перейти до наступного кроку (наприклад, колеса)
  };

  return (
    <div className="frame-selector">
      <div className="main-frame">
        <div className="frame-placeholder2">
          {selected !== null && forks[selected] && (
            <img src={forks[selected].image} alt="Вилка" className="fork-overlay" />
          )}
          {frame?.image && (
            <img src={frame.image} alt="Рама" className="frame-image" />
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
        <button className="prev-btn">
          <Link to="/configselector" className="next-link">← Назад</Link>
        </button>
        <button className="next-btn" onClick={handleNext}>Далі →</button>
      </div>
    </div>
  );
};

export default ConfigFork;
