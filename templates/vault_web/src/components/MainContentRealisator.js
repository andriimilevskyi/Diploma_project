import React, {useState} from "react";
import FilterMenu from "./FilterMenu";
import ProductGrid from "./ProductGrid";
import ProductCard from "./ProductCard";
import useProducts from './hook';


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

   const {products, loading, error} = useProducts();

   if (loading) return <div>Loading...</div>;
   if (error) return <div>Error: {error.message}</div>;

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