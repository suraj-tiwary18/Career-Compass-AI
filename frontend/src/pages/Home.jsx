import { Link } from "react-router-dom";

function Home() {
  return (
    <main className="home">

      <section className="hero">

        <h1>Career Compass AI</h1>

        <p>
          Discover the best career path based on your academic
          performance, skills, and achievements using Machine Learning.
        </p>

        <Link to="/predict">
          <button>Predict Career</button>
        </Link>

      </section>

      <section className="features">

        <div className="card">
          <h2>🤖</h2>
          <h3>AI Powered</h3>
          <p>
            Predict the most suitable career using a trained Machine Learning model.
          </p>
        </div>

        <div className="card">
          <h2>⚡</h2>
          <h3>Fast Prediction</h3>
          <p>
            Get instant career recommendations with confidence score.
          </p>
        </div>

        <div className="card">
          <h2>📊</h2>
          <h3>Prediction History</h3>
          <p>
            View all previous predictions stored in the database.
          </p>
        </div>

      </section>

    </main>
  );
}

export default Home;