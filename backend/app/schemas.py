from enum import Enum
from pydantic import BaseModel, Field

class GenderEnum(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class DegreeEnum(str, Enum):
    BTECH = "B.Tech"
    BCA = "BCA"
    MCA = "MCA"
    BSC = "B.Sc"


class BranchEnum(str, Enum):
    CSE = "CSE"
    IT = "IT"
    ECE = "ECE"
    ME = "ME"
    CIVIL = "Civil"

class StudentData(BaseModel):
    
    Age: int = Field(..., ge=18, le=30)

    Gender: GenderEnum

    Degree: DegreeEnum

    Branch: BranchEnum

    CGPA: float = Field(..., ge=0, le=10)

    Internships: int = Field(..., ge=0)

    Projects: int = Field(..., ge=0)

    Coding_Skills: int = Field(..., ge=1, le=10)

    Communication_Skills: int = Field(..., ge=1, le=10)

    Aptitude_Test_Score: int = Field(..., ge=0, le=100)

    Soft_Skills_Rating: int = Field(..., ge=1, le=10)

    Certifications: int = Field(..., ge=0)

    Backlogs: int = Field(..., ge=0)