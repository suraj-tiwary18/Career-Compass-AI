import pandas as pd

#Load Dataset
df = pd.read_csv("../dataset/raw/test.csv")

def main():
    print("Career Compass AI")
    print("Dataset Understanding")

    # Shape of dataset
    print("\nDataset Shape")
    print(df.shape)

    #Number of rows and columns
    print(f"\nNumber of Rows: {df.shape[0]}") # 0 for rows
    print(f"Number of Columns: {df.shape[1]}") # 1 for columns

    # Display all column names
    print("\nColumn Names:")
    for column in df.columns:
        print(column)

    # Dataset Information
    print("\nDataset Information")
    print(df.info())

    # First 5 rows
    print("\nFirst 5 rows")
    print(df.head())

    # Last 5 rows
    print("\nLast 5 rows")
    print(df.tail())

    # Missing Values
    print("\nMissing Values: ")
    print(df.isnull().sum())

    # Duplicate Values
    print("\nDuplicate Values")
    print(df.duplicated().sum())

    # Statical Summary
    print("\nStatical Summary")
    print(df.describe())

if __name__=="__main__":
    main()