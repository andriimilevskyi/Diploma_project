import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { ConfigContext } from "../components/ConfigContext";
import './ConfigMeasure.css';
import heightimg from '../assets/images/Height.png';
import inseamimg from '../assets/images/Inseam.png';

const ConfigMeasure = () => {
    const [height, setHeight] = useState('');
    const [innerHeight, setInnerHeight] = useState('');
    const navigate = useNavigate();

    const { setConfig } = useContext(ConfigContext);

    const handleSubmit = () => {
        if (!height || !innerHeight) {
            alert("Будь ласка, введіть усі дані.");
            return;
        }

        setConfig(prev => ({
            ...prev,
            height: Number(height),
            inseam: Number(innerHeight)
        }));

        navigate("/configdescipline");
    };

    return (
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

            <button className="next-btn" onClick={handleSubmit}>Далі →</button>
        </div>
    );
};

export default ConfigMeasure;
