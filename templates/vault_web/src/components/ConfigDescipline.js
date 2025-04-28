import { useState } from "react";
import './ConfigDescipline.css';
import { Link } from "react-router-dom";
import xcimg from "../assets/images/XC.png";
import dhimg from "../assets/images/DH.png";
import cityimg from "../assets/images/City.png";
import roadimg from "../assets/images/Road.png";
import gravelimg from "../assets/images/Gravel.png";

const ConfigDescipline = () => {
    const [selectedDiscipline, setSelectedDiscipline] = useState(null);

    const handleSelect = (discipline) => {
        setSelectedDiscipline(discipline);
        console.log("User selected:", discipline);
    };

    const handleSubmit = () => {
        if (selectedDiscipline) {
            console.log("Submitting:", selectedDiscipline);
            // Тут можна зберегти вибір або передати його далі
        } else {
            alert("Please select a discipline before proceeding.");
        }
    };

    return (
        <div className="descrcon">
            <div className="configdescp">
                <h2>Choose your descipline</h2>

                <div className="in-container">
                    {[
                        { name: "XC", img: xcimg },
                        { name: "DH", img: dhimg },
                        { name: "City", img: cityimg },
                        { name: "Road", img: roadimg },
                        { name: "Gravel", img: gravelimg }
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


                    <button className="prev-btn"><Link to="/configmeasure" className="next-link">← Назад</Link></button>
                    <button className="next-btn" onClick={handleSubmit}><Link to="/configselector" className="next-link">Далі →</Link></button>

            </div>
        </div>
    );
};

export default ConfigDescipline;
