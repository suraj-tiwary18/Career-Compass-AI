function HistoryTable({ history, handleDelete }) {

    if (history.length === 0) {
        return <h3>No Prediction History Found</h3>;
    }

    return (

        <table className="history-table">

            <thead>

                <tr>
                    <th>ID</th>
                    <th>Age</th>
                    <th>Gender</th>
                    <th>Degree</th>
                    <th>Branch</th>
                    <th>Career</th>
                    <th>Confidence</th>
                    <th>Action</th>
                </tr>

            </thead>

            <tbody>

                {history.map((item) => (

                    <tr key={item.id}>

                        <td>{item.id}</td>
                        <td>{item.age}</td>
                        <td>{item.gender}</td>
                        <td>{item.degree}</td>
                        <td>{item.branch}</td>
                        <td>{item.predicted_career}</td>
                        <td>{item.confidence}%</td>

                        <td>

                            <button
                                className="delete-btn"
                                onClick={() => handleDelete(item.id)}
                            >
                                Delete
                            </button>

                        </td>

                    </tr>

                ))}

            </tbody>

        </table>

    );

}

export default HistoryTable;