import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import "./RecomSys.css";

const RecommendationStrip = () => {
  const [recommendations, setRecommendations] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [scrollIndex, setScrollIndex] = useState(0);
  const visibleCount = 4;

  useEffect(() => {
    // Беремо id останнього переглянутого товару з sessionStorage
    const productId = sessionStorage.getItem("lastViewedProduct");

    if (!productId) {
      // Якщо немає id — нічого не показуємо
      setIsLoading(false);
      return;
    }

    // Запит рекомендацій
    fetch(`http://127.0.0.1:8000/api/recommendations/mtb/?bike_id=${productId}`)
      .then((res) => {
        if (!res.ok) throw new Error("Помилка мережі");
        return res.json();
      })
      .then((data) => {
        setRecommendations(data);
        setIsLoading(false);
      })
      .catch((err) => {
        console.error("Помилка при отриманні рекомендацій:", err);
        setIsLoading(false);
      });
  }, []);

  if (isLoading || recommendations.length === 0) return null;

  const maxIndex = recommendations.length - visibleCount;

  const handlePrev = () => {
    setScrollIndex((prev) => Math.max(prev - 1, 0));
  };

  const handleNext = () => {
    setScrollIndex((prev) => Math.min(prev + 1, maxIndex));
  };

  return (
    <div className="recommendation-strip">
      <h3>Рекомендовано для вас</h3>
      <div className="carousel-container">
        <button
          className="carousel-button prev"
          onClick={handlePrev}
          disabled={scrollIndex === 0}
        >
          ‹
        </button>
        <div className="recommendation-scroll">
          {recommendations
            .slice(scrollIndex, scrollIndex + visibleCount)
            .map((rec) => (
              <Link
                to={`/product/${rec.id}`}
                key={rec.id}
                className="recommendation-card"
              >
                <img src={rec.preview_image} alt={rec.series} />
                <p>{rec.series}</p>
                <p>{rec.price}€</p>
              </Link>
            ))}
        </div>
        <button
          className="carousel-button next"
          onClick={handleNext}
          disabled={scrollIndex >= maxIndex}
        >
          ›
        </button>
      </div>
    </div>
  );
};

export default RecommendationStrip;
