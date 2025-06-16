import { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ConfigContext } from "../components/ConfigContext";
import './ConfigDescipline.css';

import xcimg from "../assets/images/XC.png";
import dhimg from "../assets/images/DH.png";
import cityimg from "../assets/images/City.png";
import roadimg from "../assets/images/Road.png";
import gravelimg from "../assets/images/Gravel.png";

// Тепер disciplineMap має об'єкти з name, value, img
const disciplineMap = {
  "Крос-кантрі": { value: 1, img: xcimg },
  "Даунхіл": { value: 2, img: dhimg },
  "Місто": { value: 3, img: cityimg },
  "Траса": { value: 4, img: roadimg },
  "Гравій": { value: 5, img: gravelimg }
};

const ConfigDescipline = () => {
  const navigate = useNavigate();
  const { config, setConfig } = useContext(ConfigContext);

  const [selectedDiscipline, setSelectedDiscipline] = useState(
    Object.entries(disciplineMap).find(([_, val]) => val.value === config.discipline)?.[0] || null
  );

  const handleSelect = (discipline) => {
    setSelectedDiscipline(discipline);
  };

  const handleSubmit = () => {
    if (!selectedDiscipline) return;

    setConfig(prev => ({
      ...prev,
      discipline: disciplineMap[selectedDiscipline].value
    }));

    navigate("/configselector");
  };

  return (
    <div className="descrcon">
      <div className="configdescp">
        <h2>Оберіть дисципліну</h2>

        <div className="in-container">
          {Object.entries(disciplineMap).map(([name, data]) => (
            <button
              key={name}
              onClick={() => handleSelect(name)}
              className={selectedDiscipline === name ? "selected" : ""}
            >
              <div className="in-block">
                <img src={data.img} alt={name} />
                <span>{name}</span>
              </div>
            </button>
          ))}
        </div>

        <button className="prev-btn" onClick={() => navigate("/configmeasure")}>← Назад</button>
        <button className="next-btn" onClick={handleSubmit}>Далі →</button>
      </div>
    </div>
  );
};

export default ConfigDescipline;
