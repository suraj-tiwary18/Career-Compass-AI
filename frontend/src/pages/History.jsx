import { useEffect, useState } from "react";
import api from "../services/api";
import HistoryTable from "../components/HistoryTable";

function History() {

    const [history, setHistory] = useState([]);

    useEffect(() => {
        fetchHistory();
    }, []);

    async function fetchHistory() {

        try {

            const response = await api.get("/history");

            setHistory(response.data);

        } catch (error) {

            console.log(error);

        }
    }

    async function handleDelete(id) {

        const confirmDelete = window.confirm(
            "Are you sure you want to delete this prediction?"
        );

        if (!confirmDelete) {
            return;
        }

        try {

            await api.delete(`/history/${id}`);

            fetchHistory();

        } catch (error) {

            console.log(error);

        }
    }

    return (

        <div className="history-page">

            <h1>Prediction History</h1>

            <HistoryTable
                history={history}
                handleDelete={handleDelete}
            />

        </div>

    );
}

export default History;