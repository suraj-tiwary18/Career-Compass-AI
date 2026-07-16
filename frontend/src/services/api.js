import axios from "axios";

const api = axios.create({
  baseURL: "https://career-compass-ai-ktqf.onrender.com",
});

export default api;