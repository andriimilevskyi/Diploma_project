import { useState } from "react";
import './Configurator.css';
import heightimg from "../assets/images/Height.png";
import inseamimg from "../assets/images/Inseam.png";

const Configurator = () => {
    const [height, setHeight] = useState("");
    const [innerHeight, setInnerHeight] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log(`Зріст: ${height} см, Внутрішня висота: ${innerHeight} см`);
    };

    return (
    <div className="bodycon">
        <div className="configurator">
            <h2>What is your height?</h2>

            <div className="inputs-container">
                <div className="input-block">
                    <img src={heightimg} alt="Зріст" />
                    <label>Enter height</label>
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
                    <label>Enter inseam length</label>
                    <input
                        type="number"
                        value={innerHeight}
                        onChange={(e) => setInnerHeight(e.target.value)}
                        placeholder="СМ"
                        required
                    />
                </div>
            </div>

            <button className="next-btn" onClick={handleSubmit}>Next →</button>
        </div>
        </div>
    );
};

export default Configurator;
