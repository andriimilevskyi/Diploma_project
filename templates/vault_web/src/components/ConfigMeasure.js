import { useState } from "react";
import './ConfigMeasure.css';
import { Link } from "react-router-dom";
import heightimg from "../assets/images/Height.png";
import inseamimg from "../assets/images/Inseam.png";

const ConfigMeasure = () => {
    const [height, setHeight] = useState("");
    const [innerHeight, setInnerHeight] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(`Зріст: ${height} см, Внутрішня висота: ${innerHeight} см`);
    };

    return (
    <div className="bodycon">
        <div className="configmeasure">
            <h2>Який ваш зріст?</h2>

            <div className="inputs-container">
                <div className="input-block">
                    <img src={heightimg} alt="Зріст" />
                    <label>Введіть зріст</label>
                    <input
                        type="number"
                        value={height}
                        onChange={(e) => setHeight(e.target.value)}
                        placeholder="СМ"
                        required
                    />
                </div>

                <div className="input-block">
                    <img src={inseamimg} alt="Внутрішня висота" />
                    <label>Введіть довжину ноги</label>
                    <input
                        type="number"
                        value={innerHeight}
                        onChange={(e) => setInnerHeight(e.target.value)}
                        placeholder="СМ"
                        required
                    />
                </div>
            </div>

            <button className="next-btn" onClick={handleSubmit}><Link to="/configdescipline" className="next-link">Далі →</Link></button>
        </div>
        </div>
    );
};

export default ConfigMeasure;
