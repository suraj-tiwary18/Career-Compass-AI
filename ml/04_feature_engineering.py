import pandas as pd

# Loand Dataset
df = pd.read_csv("../dataset/processed/cleaned_data.csv")


def assign_career(row):

    degree = row["Degree"]
    branch = row["Branch"]
    cgpa = row["CGPA"]
    coding = row["Coding_Skills"]
    communication = row["Communication_Skills"]
    aptitude = row["Aptitude_Test_Score"]
    projects = row["Projects"]
    internships = row["Internships"]
    certifications = row["Certifications"]
    backlogs = row["Backlogs"]

    # 1. Machine Learning Engineer
    if (
        degree in ["B.Tech", "MCA", "BCA"]
        and branch in ["CSE", "IT", "ECE"]
        and cgpa >= 8.0
        and coding >= 8
        and projects >= 2
        and certifications >= 1
        and internships >= 1
    ):
        return "Machine Learning Engineer"

    # 2. Full Stack Developer
    elif (
        branch in ["CSE", "IT"]
        and coding >= 8
        and communication >= 7
        and projects >= 2
    ):
        return "Full Stack Developer"

    # 3. Backend Developer
    elif (
        branch in ["CSE", "IT", "ECE"]
        and coding >= 7
        and communication >= 5
    ):
        return "Backend Developer"

    # 4. Frontend Developer
    elif (
        communication >= 7
        and coding >= 5
        and projects >= 1
        and internships >= 1
    ):
        return "Frontend Developer"

    # 5. Data Analyst
    elif (
        aptitude >= 75
        and communication >= 7
        and cgpa >= 7
    ):
        return "Data Analyst"

    # 6. Software Engineer
    elif (
        coding >= 6
        and cgpa >= 6.5
    ):
        return "Software Engineer"

    # 7. Degree/Branch Based Fallback
    elif branch in ["CSE", "IT"]:
        return "Software Engineer"

    elif branch == "ECE":
        return "Backend Developer"

    elif degree in ["BCA", "MCA"]:
        return "Full Stack Developer"

    elif branch in ["ME", "Civil"]:
        return "Data Analyst"

    # Final fallback
    else:
        return "Software Engineer"




# Main Function
def main():
    # Creating Career Column
    df["Career"] = df.apply(assign_career, axis=1)

    # Removeing Placement Status
    df.drop(columns=["Placement_Status"], inplace=True)

    #Checking Cereer Distribution
    print("\nCareer Distribution")
    print(df["Career"].value_counts())

    df.to_csv("../dataset/processed/career_dataset.csv", index=False)

    print("\ncareer_dataset.csv saved successfully")

if __name__=="__main__":
    main()