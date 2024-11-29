import React, { useState } from "react";
import FilterMenu from "./FilterMenu";
import ProductGrid from "./ProductGrid";

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

  const products = [
    {
      id: 1,
      imgSrc: require("../images/fibre.jpg"),
      title: "SAVIOR",
      description: "MagSafe® Compatible Aramid Fibre Phone Case",
      price: "€34,99",
      tags: ["magsafe"],
      color: "green",
    },
    {
      id: 2,
      imgSrc: require("../images/plastic.png"),
      title: "CARRION",
      description: "MagSafe® Compatible Clear Phone Case",
      price: "€69,99",
      tags: ["magsafe", "designs"],
      color: "black",
    },
    {
      id: 3,
      imgSrc: require("../images/silicon.jpg"),
      title: "INLOCK",
      description: "Thin Protective Phone Case",
      price: "€59,99",
      tags: ["thin"],
      color: "blue",
    },
    {
      id: 4,
      imgSrc: require("../images/bringin.jpg"),
      title: "BRINGIN",
      description: "MagSafe® Compatible Carbon Fibre Case",
      price: "€59,99",
      tags: ["magsafe"],
      color: "black",
    },
    {
      id: 5,
      imgSrc: require("../images/defense.jpg"),
      title: "DEFENSE",
      description: "Heavy Duty Defense Case",
      price: "€79,99",
      tags: ["thin"],
      color: "light",
    },
    {
      id: 6,
      imgSrc: require("../images/holden.jpg"),
      title: "HOLDEN",
      description: "Shockproof Alpha Case",
      price: "€49,99",
      tags: ["designs"],
      color: "light",
    },
  ];

  // Функція для перетворення ціни з рядка на число
  const parsePrice = (priceStr) => {
    return parseFloat(priceStr.replace("€", "").replace(",", "."));
  };

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  const handleApplyFilters = () => {
    if (Object.values(filters).every((val) => !val) && // перевірка на вимкнені фільтри
        !Object.values(filters.colors).some(Boolean) && // перевірка на вимкнені кольори
        filters.priceRange.min === 0 && filters.priceRange.max === 100) {
      setAppliedFilters(null); // Якщо фільтри вимкнені, показуємо всі продукти
    } else {
      setAppliedFilters(filters); // Якщо є активні фільтри, застосовуємо їх
    }
  };


  // Якщо фільтри не застосовані, показуємо всі продукти
  const filteredProducts = appliedFilters
    ? products.filter((product) => {
        const { magsafe, thin, designs, colors, priceRange } = appliedFilters;

        const passesFeaturesFilter =
          (!magsafe || product.tags.includes('magsafe')) &&
          (!thin || product.tags.includes('thin')) &&
          (!designs || product.tags.includes('designs'));

        const passesColorFilter =
          !Object.values(colors).some(Boolean) || colors[product.color];

        // Перевірка фільтру за ціною після перетворення на число
        const passesPriceFilter =
          parsePrice(product.price) >= priceRange.min && parsePrice(product.price) <= priceRange.max;

        return passesFeaturesFilter && passesColorFilter && passesPriceFilter;
      })
    : products;

  return (
    <div className="main-content">
      <FilterMenu filters={filters} onFilterChange={handleFilterChange} onApplyFilters={handleApplyFilters} />
      <ProductGrid products={filteredProducts} />
    </div>
  );
};

export default MainContentRealisator;
