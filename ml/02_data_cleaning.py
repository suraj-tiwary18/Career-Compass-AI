# Cleaning the raw data befor performing
# EDA and model training.

import pandas as pd

# Load Dataset
df = pd.read_csv("../dataset/raw/test.csv")

# Main Function
def main():

    # Checking Missing Values
    print("\nChecking Missing Values...")
    missing_values = df.isnull().sum().sum()

    if missing_values == 0:
        print("No Missing Values Found")
    else:
        print(f"Total Missing Values: {missing_values}")


    # Verify Duplicate rows
    print("\nChecking Duplicate Rows...")
    duplicate_rows = df.duplicated().sum()

    if duplicate_rows == 0:
        print("No Duplicate Rows Found.")
    else:
        df.duplicated(inplace=True)
        print(f"{duplicate_rows} Duplicate Rows Removed.")    # 

    # Remove Unnecessary Column
    print("\nRemove Unnecessary Columns..")
    df.drop(columns=['Student_ID'], inplace=True)
    print("Student_ID Column removed successfully.")

    # Final Shape
    print("\nCleaned Dataset Shape")
    print(df.shape)

    # Save Cleaned Dataset
    output_path = "../dataset/processed/cleaned_data.csv"

    df.to_csv(output_path, index=False)
    print(f"\nCleand Dataset Location : {output_path}")

if __name__=="__main__":
    main()