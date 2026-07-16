function ResultCard({ result }) {

    if (!result) return null;

    return (

        <div className="result-card">

            <h2>✅ Prediction Successful</h2>

            <h3>{result.career}</h3>

            <p>
                Confidence Score
            </p>

            <h2>{result.confidence}%</h2>

        </div>

    );

}

export default ResultCard;