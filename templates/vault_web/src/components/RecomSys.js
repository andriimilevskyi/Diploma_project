import { useParams } from "react-router-dom";
import './RecomSys.css';

const { id } = useParams();

const [recommendations, setRecommendations] = useState([]);

useEffect(() => {
  const fetchRecommendations = async () => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/recommendations/?product_id=${id}`);
      const data = await res.json();
      setRecommendations(data);
    } catch (error) {
      console.error("Recommendation fetch error:", error);
    }
  };

  fetchRecommendations();
}, [id]);

{recommendations.length > 0 && (
  <div className="recommendation-section">
    <h3>Рекомендовані велосипеди</h3>
    <div className="recommendation-list">
      {recommendations.map((bike) => (
        <div key={bike.id} className="recommendation-card">
          <img src={bike.image} alt={bike.series} />
          <p>{bike.series}</p>
          <p>{bike.price}€</p>
          <Link to={`/product/${bike.id}`}>Переглянути</Link>
        </div>
      ))}
    </div>
  </div>
)}
