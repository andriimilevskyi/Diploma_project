import React, { useState } from "react";
import FilterMenu from "./FilterMenu";
import ProductGrid from "./ProductGrid";

const MainContentRealisator = () => {
  // Стан для тимчасових фільтрів (до натискання кнопки)
  const [tempFilters, setTempFilters] = useState({
    magsafe: false,
    thin: false,
    designs: false,
    colors: {
      black: false,
      blue: false,
      light: false,
      green: false,
    },
  });

  // Стан для підтверджених фільтрів (після натискання кнопки)
  const [confirmedFilters, setConfirmedFilters] = useState({
    magsafe: false,
    thin: false,
    designs: false,
    colors: {
      black: false,
      blue: false,
      light: false,
      green: false,
    },
  });

  const products = [
    {
      imgSrc: require("../images/fibre.jpg"),
      title: "SAVIOR",
      description: "MagSafe® Compatible Aramid Fibre Phone Case",
      price: "€34,99",
      tags: ["magsafe"],
      color: "green",
    },
    {
      imgSrc: require("../images/plastic.png"),
      title: "CARRION",
      description: "MagSafe® Compatible Clear Phone Case",
      price: "€69,99",
      tags: ["magsafe", "designs"],
      color: "black",
    },
    {
      imgSrc: require("../images/silicon.jpg"),
      title: "INLOCK",
      description: "Thin Protective Phone Case",
      price: "€59,99",
      tags: ["thin"],
      color: "blue",
    },
    {
      imgSrc: require("../images/bringin.jpg"),
      title: "BRINGIN",
      description: "MagSafe® Compatible Carbon Fibre Case",
      price: "€59,99",
      tags: ["magsafe"],
      color: "black",
    },
    {
      imgSrc: require("../images/defense.jpg"),
      title: "DEFENSE",
      description: "Heavy Duty Defense Case",
      price: "€79,99",
      tags: ["thin"],
      color: "light",
    },
    {
      imgSrc: require("../images/holden.jpg"),
      title: "HOLDEN",
      description: "Shockproof Alpha Case",
      price: "€49,99",
      tags: ["designs"],
      color: "light",
    },
  ];

  // Обробка зміни тимчасових фільтрів
  const handleFilterChange = (newFilters) => {
    setTempFilters(newFilters);
  };

  // Застосування фільтрів після натискання кнопки "Apply Filters"
  const applyFilters = () => {
    setConfirmedFilters(tempFilters); // Підтверджуємо вибрані фільтри
  };

  // Фільтрація продуктів на основі підтверджених фільтрів
  const filteredProducts = products.filter((product) => {
    const { magsafe, thin, designs, colors } = confirmedFilters;

    // Логіка фільтрації за характеристиками
    const passesFeaturesFilter =
      (!magsafe || product.tags.includes("magsafe")) &&
      (!thin || product.tags.includes("thin")) &&
      (!designs || product.tags.includes("designs"));

    // Логіка фільтрації за кольорами
    const passesColorFilter =
      !Object.values(colors).some(Boolean) || colors[product.color];

    return passesFeaturesFilter && passesColorFilter;
  });

  return (
    <div className="main-content">
      <FilterMenu
        filters={tempFilters}
        onFilterChange={handleFilterChange}
        onApplyFilters={applyFilters}
      />
      <ProductGrid products={filteredProducts} />
    </div>
  );
};

export default MainContentRealisator;
