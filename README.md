# 🧭 Career Compass AI

An AI-powered Career Recommendation System that helps students identify the most suitable career path based on their academic performance, technical skills, projects, internships, certifications, and aptitude using Machine Learning.

---

## 🚀 Features

- 🤖 AI-Based Career Recommendation
- 📊 Machine Learning Model (~97% Accuracy)
- ⚡ FastAPI REST API
- ⚛️ React Frontend
- 🗄️ MySQL Database Integration
- 📜 Prediction History
- 🗑️ Delete Individual Prediction History
- 📱 Responsive User Interface

---

## 🛠️ Tech Stack

### Frontend
- React.js
- React Router
- Axios
- CSS
- Lucide React

### Backend
- FastAPI
- Python
- PyMySQL
- Pydantic

### Machine Learning
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Matplotlib

### Database
- MySQL

---

## 📂 Project Structure

```
Career Compass AI
│
├── artifacts/
├── backend/
│   ├── app/
│   ├── main.py
│   └── requirements.txt
│
├── dataset/
├── frontend/
├── graphs/
├── ml/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/suraj-tiwary18/Career-Compass-AI.git
```

### Move into Project

```bash
cd Career-Compass-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Backend

```bash
cd backend

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Home |
| GET | `/health` | Health Check |
| POST | `/predict` | Predict Career |
| GET | `/history` | Prediction History |
| DELETE | `/history/{id}` | Delete Prediction |

---

## 📸 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

### 🎯 Prediction Page

![Prediction Page](screenshots/predict.png)

### 🤖 Prediction Result

![Prediction Result](screenshots/result.png)

### 📜 History Page

![History Page](screenshots/history.png)

### ℹ️ About Page

![About Page](screenshots/about.png)

---

## 🎯 Future Improvements

- Docker Support
- Cloud Deployment
- Authentication
- Career Roadmap Suggestions
- Resume Analyzer
- Multiple ML Models
- PDF Report Generation

---

## 👨‍💻 Author

**Suraj Kumar Tiwari**

- GitHub: https://github.com/suraj-tiwary18
- LinkedIn: https://www.linkedin.com/in/suraj-tiwari-580984332/

---

⭐ If you like this project, don't forget to star the repository.