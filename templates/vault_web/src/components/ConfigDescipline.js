import { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { ConfigContext } from "../components/ConfigContext";
import './ConfigDescipline.css';

const disciplineMap = {
    "Крос-кантрі": 1,
    "Даунхіл": 2,
    "Місто": 3,
    "Траса": 4,
    "Гравій": 5,
};

const ConfigDescipline = () => {
    const navigate = useNavigate();
    const { config, setConfig } = useContext(ConfigContext);
    const [selectedDiscipline, setSelectedDiscipline] = useState(
      Object.keys(disciplineMap).find(key => disciplineMap[key] === config.discipline) || null
    );

    const handleSelect = (discipline) => {
        setSelectedDiscipline(discipline);
    };

    const handleSubmit = () => {
        if (!selectedDiscipline) {
            alert("Будь ласка, оберіть дисципліну.");
            return;
        }

        setConfig(prev => ({
          ...prev,
          discipline: disciplineMap[selectedDiscipline]
        }));

        navigate("/configselector");
    };

    return (
        <div className="descrcon">
            <div className="configdescp">
                <h2>Оберіть дисципліну</h2>

                <div className="in-container">
                    {Object.keys(disciplineMap).map((name) => (
                        <button
                            key={name}
                            onClick={() => handleSelect(name)}
                            className={selectedDiscipline === name ? "selected" : ""}
                        >
                            <div className="in-block">
                                {name}
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
