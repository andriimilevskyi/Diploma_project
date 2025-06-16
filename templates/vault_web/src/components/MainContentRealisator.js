import React, { useState, useEffect } from "react";
import FilterMenu from "./FilterMenu";
import ProductGrid from "./ProductGrid";
import useProducts from './hook';
import { Link } from 'react-router-dom';
import './RecomSys.css';

const MainContentRealisator = () => {
  const [filters, setFilters] = useState({
    magsafe: false,
    thin: false,
    designs: false,
    colors: {
      black: false,
      blue: false,
      light: false,
      green: false,
    },
    priceRange: {
      min: 0,
      max: 100,
    },
  });

  const [appliedFilters, setAppliedFilters] = useState(null);
  const { products, loading, error } = useProducts();

  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const productId = localStorage.getItem("lastViewedProduct");
    if (productId) {
      fetch(`http://127.0.0.1:8000/api/recommendations/mtb/?bike_id=${productId}`)
        .then(res => res.json())
        .then(data => setRecommendations(data))
        .catch(err => console.error("Помилка при отриманні рекомендацій:", err));
    }
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  const parsePrice = (priceStr) => {
    return parseFloat(priceStr.replace("€", "").replace(",", "."));
  };

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  const handleApplyFilters = () => {
    if (
      Object.values(filters).every((val) => !val) &&
      !Object.values(filters.colors).some(Boolean) &&
      filters.priceRange.min === 0 &&
      filters.priceRange.max === 100
    ) {
      setAppliedFilters(null);
    } else {
      setAppliedFilters(filters);
    }
  };

  const filteredProducts = appliedFilters
    ? products.filter((product) => {
        const { magsafe, thin, designs, colors, priceRange } = appliedFilters;

        const passesFeaturesFilter =
          (!magsafe || product.tags.includes('magsafe')) &&
          (!thin || product.tags.includes('thin')) &&
          (!designs || product.tags.includes('designs'));

        const passesColorFilter =
          !Object.values(colors).some(Boolean) || colors[product.color];

        const passesPriceFilter =
          parsePrice(product.price) >= priceRange.min &&
          parsePrice(product.price) <= priceRange.max;

        return passesFeaturesFilter && passesColorFilter && passesPriceFilter;
      })
    : products;

  return (
    <div className="main-content">
      {/* РЕКОМЕНДАЦІЇ ПІД ХЕДЕРОМ */}
      {recommendations.length > 0 && (
        <div className="recommendation-strip">
          <h3>Рекомендовано для вас</h3>
          <div className="recommendation-list">
            {recommendations.map((rec) => (
              <Link to={`/product/${rec.id}`} key={rec.id} className="recommendation-card">
                <img src={rec.image} alt={rec.series} />
                <p>{rec.series}</p>
                <p>{rec.price}€</p>
              </Link>
            ))}
          </div>
        </div>
      )}

      {/* ФІЛЬТРИ ТА ПРОДУКТИ */}
      <FilterMenu
        filters={filters}
        onFilterChange={handleFilterChange}
        onApplyFilters={handleApplyFilters}
      />
      <ProductGrid products={filteredProducts} />
    </div>
  );
};

export default MainContentRealisator;
