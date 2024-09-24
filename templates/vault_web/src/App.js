// App.js
import React from "react";
import "./App.css";

function App() {
  return (
    <div className="App">
      {/* Header */}
      <header className="header">
        <div className="header-div">
          <div className="logo">Logo</div>
          <nav className="nav">
            <ul>
              <li>Cases & Accessories</li>
              <li>Bags & Pouches</li>
              <li>Mounts & Chargers</li>
              <li>Sale</li>
            </ul>
          </nav>
          <div className="user-actions">
            <span>🌐</span>
            <span>€</span>
            <span>❤️</span>
            <span>👤</span>
            <span>🛒</span>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="main-content">
        {/* Sidebar Filters */}
        <aside className="filter-sidebar">
          <h2>Filter & Sort</h2>
          <div className="filter-category">
            <label>Sort By:</label>
            <select>
              <option>Featured</option>
              <option>Price: Low to High</option>
              <option>Price: High to Low</option>
            </select>
          </div>
          

          <div className="filter-category">
            <label>Color:</label>
            <select>
              <option>All</option>
              <option>Red</option>
              <option>Blue</option>
              <option>Green</option>
              <option>Black</option>
              <option>White</option>
            </select>
          </div>

          <div className="filter-category">
            <label>Price:</label>
            <select>
              <option>All</option>
              <option>Under €50</option>
              <option>€50 - €100</option>
              <option>Over €100</option>
            </select>
          </div>

          <button>Apply Filters</button>
        </aside>

        {/* Product Grid */}
        <section className="products-grid">
          {/* Product Card 1 */}
          <div className="product-card">
            <img src={require(".//images/fibre.jpg")} alt="img" />
            <h3>SAVIOR</h3>
            <p>MagSafe® Compatible Aramid Fibre Phone Case</p>
            <p>€34,99</p>
            <button>Buy</button>
          </div>

          {/* Product Card 2 */}
          <div className="product-card">
            <img src={require(".//images/plastic.png")} alt="img" />
            <h3>CARRION</h3>
            <p>MagSafe® Compatible Clear Phone Case</p>
            <p>€69,99</p>
            <button>Buy</button>
          </div>

          {/* Product Card 3 */}
          <div className="product-card">
            <img src={require(".//images/silicon.jpg")} alt="img" />
            <h3>INLOCK</h3>
            <p>Phone Case</p>
            <p>€59,99</p>
            <button>Buy</button>
          </div>

          {/* Additional Product Cards */}
          <div className="product-card">
            <img src={require(".//images/plastic.png")} alt="img" />
            <h3>BRINGIN</h3>
            <p>MagSafe® Compatible Carbon Fibre Case</p>
            <p>€59,99</p>
            <button>Buy</button>
          </div>

          <div className="product-card">
            <img src={require(".//images/plastic.png")} alt="img" />
            <h3>HOLDEN</h3>
            <p>Shockproof Alpha Case</p>
            <p>€49,99</p>
            <button>Buy</button>
          </div>

          <div className="product-card">
            <img src={require(".//images/plastic.png")} alt="img" />
            <h3>DEFENSE</h3>
            <p>Heavy Duty Defense Case - Black</p>
            <p>€79,99</p>
            <button>Buy</button>
          </div>

          <div className="product-card">
            <img src={require(".//images/plastic.png")} alt="img" />
            <h3>EDGE</h3>
            <p>Edge-to-Edge Protection Case</p>
            <p>€89,99 €75,99</p>
            <button>Buy</button>
          </div>

          <div className="product-card">
            <img src={require(".//images/plastic.png")} alt="img" />
            <h3>TOUGH</h3>
            <p>Extra Tough Rugged Case</p>
            <p>€99,99</p>
            <button>Buy</button>
          </div>

          <div className="product-card">
            <img src={require(".//images/plastic.png")} alt="img" />
            <h3>SLIM</h3>
            <p>Slim Fit Transparent Case</p>
            <p>€39,99</p>
            <button>Buy</button>
          </div>
        </section>
      </div>
    </div>
  );
}

export default App;
