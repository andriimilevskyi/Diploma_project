import { useLocation, useNavigate } from "react-router-dom";
import { useState } from "react";
import './ConfigDescipline.css';
import xcimg from "../assets/images/XC.png";
import dhimg from "../assets/images/DH.png";
import cityimg from "../assets/images/City.png";
import roadimg from "../assets/images/Road.png";
import gravelimg from "../assets/images/Gravel.png";

const disciplineMap = {
    XC: 1,
    DH: 2,
    "Місто": 3,
    "Траса": 4,
    "Гравій": 5,
};

const ConfigDescipline = () => {
    const navigate = useNavigate();
    const location = useLocation();
    const { height, inseam } = location.state || {};
    const [selectedDiscipline, setSelectedDiscipline] = useState(null);

    const handleSelect = (discipline) => {
        setSelectedDiscipline(discipline);
    };

    const handleSubmit = () => {
        if (!selectedDiscipline) {
            alert("Будь ласка, оберіть дисципліну.");
            return;
        }

        navigate("/configselector", {
            state: {
                height,
                inseam,
                discipline: disciplineMap[selectedDiscipline],
            },
        });
    };

    return (
        <div className="descrcon">
            <div className="configdescp">
                <h2>Оберіть дисципліну</h2>

                <div className="in-container">
                    {[
                        { name: "XC", img: xcimg },
                        { name: "DH", img: dhimg },
                        { name: "Місто", img: cityimg },
                        { name: "Траса", img: roadimg },
                        { name: "Гравій", img: gravelimg }
                    ].map((item) => (
                        <button
                            key={item.name}
                            onClick={() => handleSelect(item.name)}
                            className={selectedDiscipline === item.name ? "selected" : ""}
                        >
                            <div className="in-block">
                                <img src={item.img} alt={item.name} />
                                {item.name}
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
