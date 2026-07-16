import { useState } from "react";
import api from "../services/api";
import ResultCard from "./ResultCard";

function PredictionForm() {

    const [result, setResult] = useState(null);

    const [formData, setFormData] = useState({

        Age: "",
        Gender: "",
        Degree: "",
        Branch: "",
        CGPA: "",
        Internships: "",
        Projects: "",
        Coding_Skills: "",
        Communication_Skills: "",
        Aptitude_Test_Score: "",
        Soft_Skills_Rating: "",
        Certifications: "",
        Backlogs: ""
    });


    function handleChange(event) {

        setFormData({
            ...formData,
            [event.target.name]: event.target.value
        });

    }


    
    async function handleSubmit(event) {

        event.preventDefault();

        console.log(formData);

        try {

            const response = await api.post("/predict", formData);

            setResult(response.data);

        } catch (error) {

            console.log(error);

            alert("Prediction Failed");

        }

    }

    return (

        <div>

            <form className="prediction-form" onSubmit={handleSubmit}>

                <input
                    type="number"
                    name="Age"
                    placeholder="Age"
                    value={formData.Age}
                    onChange={handleChange}
                />

                <select
                    name="Gender"
                    value={formData.Gender}
                    onChange={handleChange}
                >
                    <option value="">Select Gender</option>
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                </select>

                <select
                    name="Degree"
                    value={formData.Degree}
                    onChange={handleChange}
                >
                    <option value="">Select Degree</option>
                    <option value="B.Tech">B.Tech</option>
                    <option value="BCA">BCA</option>
                    <option value="MCA">MCA</option>
                    <option value="B.Sc">B.Sc</option>
                </select>

                <select
                    name="Branch"
                    value={formData.Branch}
                    onChange={handleChange}
                >
                    <option value="">Select Branch</option>
                    <option value="CSE">CSE</option>
                    <option value="IT">IT</option>
                    <option value="ECE">ECE</option>
                    <option value="ME">ME</option>
                    <option value="Civil">Civil</option>
                </select>

                <input type="number" name="CGPA" placeholder="CGPA" value={formData.CGPA} onChange={handleChange}/>
                <input type="number" name="Internships" placeholder="Internships" value={formData.Internships} onChange={handleChange}/>
                <input type="number" name="Projects" placeholder="Projects" value={formData.Projects} onChange={handleChange}/>
                <input type="number" name="Coding_Skills" placeholder="Coding Skills (1-10)" value={formData.Coding_Skills} onChange={handleChange}/>
                <input type="number" name="Communication_Skills" placeholder="Communication Skills (1-10)" value={formData.Communication_Skills} onChange={handleChange}/>
                <input type="number" name="Aptitude_Test_Score" placeholder="Aptitude Test Score" value={formData.Aptitude_Test_Score} onChange={handleChange}/>
                <input type="number" name="Soft_Skills_Rating" placeholder="Soft Skills Rating" value={formData.Soft_Skills_Rating} onChange={handleChange}/>
                <input type="number" name="Certifications" placeholder="Certifications" value={formData.Certifications} onChange={handleChange}/>
                <input type="number" name="Backlogs" placeholder="Backlogs" value={formData.Backlogs} onChange={handleChange}/>

                <button type="submit">
                    Predict Career
                </button>

            </form>
            
            <ResultCard result={result} />

        </div>    
    );
}

export default PredictionForm;