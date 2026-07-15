# Exploratory Data Analysis

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset 
df = pd.read_csv("../dataset/processed/cleaned_data.csv")





# Gender Distribution
def gender_distribution():

    gender_count = df['Gender'].value_counts()

    print("\nGender Distribution")
    print(gender_count)

    plt.figure(figsize=(6, 5))

    gender_count.plot(kind="bar")

    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.savefig("../graphs/gender_distribution.png")
    plt.show()


def degree_distribution():

    degree_count = df['Degree'].value_counts()

    print("\nDegree Distribution")
    print(degree_count)

    plt.figure(figsize=(7, 5))

    degree_count.plot(kind="bar")

    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.savefig("../graphs/degree_distribution.png")
    plt.show()


def branch_distribution():

    branch_count = df["Branch"].value_counts()

    print("\nBranch Distribution")
    print(branch_count)

    plt.figure(figsize=(8,5))

    branch_count.plot(kind="bar")

    plt.title("Branch Distribution")
    plt.xlabel("Branch")
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.savefig("../graphs/branch_distribution.png")
    plt.show()


# This is know as Reusable code , modular programmig, clean code :-

def numerical_distribution(column_name):
    
    print("\n(clumn_name) Summary")
    print(df[column_name].describe())

    plt.figure(figsize=(8, 5))

    plt.hist(df[column_name], bins=15)

    plt.title(f"{column_name} Distribution")
    plt.xlabel(column_name)
    plt.ylabel("Number of Students")

    plt.tight_layout()
    plt.savefig(f"../graphs/{column_name.lower()}_Distribution")
    plt.show()


def cgpa_vs_placement():

    cgpa_placement = df.groupby("Placement_Status")["CGPA"].mean()

    print("\nAverage CGPA by Placement Status")
    print(cgpa_placement)

    plt.figure(figsize=(6, 5))

    cgpa_placement.plot(kind="bar")

    plt.title("Average CGPA by Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel("Average CGPA")

    plt.tight_layout()
    plt.savefig("../graphs/cgpa_vs_placement.png")
    plt.show()

def feature_vs_placement(feature_name):

    result = df.groupby("Placement_Status")[feature_name].mean()

    print("\nAverage Coding Skills by Placement Status")
    print(result)

    plt.figure(figsize=(6,5))

    result.plot(kind="bar")

    plt.title(f"{feature_name} vs Placement Status")
    plt.xlabel("Placement Status")
    plt.ylabel(f"Average {feature_name}")

    plt.tight_layout()
    plt.savefig(f"../graphs/{feature_name.lower()}_vs_placement.png")
    plt.show()

def main():

    print("\nCareer Compass AI")

    # Categorical Analysis
    gender_distribution()
    degree_distribution()
    branch_distribution()

    #Numerical Analysis
    numerical_distribution("Age")
    numerical_distribution("CGPA")
    numerical_distribution("Internships")
    numerical_distribution("Projects")
    numerical_distribution("Coding_Skills")
    numerical_distribution("Communication_Skills")
    numerical_distribution("Aptitude_Test_Score")
    numerical_distribution("Soft_Skills_Rating")
    numerical_distribution("Certifications")
    numerical_distribution("Backlogs")
    
    # Relationship Analysis
    feature_vs_placement("CGPA")
    feature_vs_placement("Coding_Skills")
    feature_vs_placement("Projects")
    feature_vs_placement("Internships")
    feature_vs_placement("Communication_Skills")
    feature_vs_placement("Aptitude_Test_Score")
    feature_vs_placement("Soft_Skills_Rating")
    feature_vs_placement("Certifications")
    feature_vs_placement("Backlogs")

if __name__=="__main__":
    main()