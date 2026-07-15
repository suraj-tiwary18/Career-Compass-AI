import pymysql

from app.config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
)


def get_connection():

    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )

        return connection
    
    except Exception as e:
        print(f"Database Connection Error: {e}")
        return None
    
# I am Using try and except for error handling 




def save_prediction(data: dict, career: str, confidence: float):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO prediction_history
    (
        age,
        gender,
        degree,
        branch,
        cgpa,
        internships,
        projects,
        coding_skills,
        communication_skills,
        aptitude_test_score,
        soft_skills_rating,
        certifications,
        backlogs,
        predicted_career,
        confidence
    )
    VALUES
    (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s
    )
    """

    values = (
        data["Age"],
        data["Gender"].value,
        data["Degree"].value,
        data["Branch"].value,
        data["CGPA"],
        data["Internships"],
        data["Projects"],
        data["Coding_Skills"],
        data["Communication_Skills"],
        data["Aptitude_Test_Score"],
        data["Soft_Skills_Rating"],
        data["Certifications"],
        data["Backlogs"],
        career,
        confidence
    )

    try:
        cursor.execute(query, values)
        connection.commit()

    except Exception as e:
        connection.rollback()
        print(f"Error: {e}")

    finally:
        cursor.close()
        connection.close()




# Histroy
def get_prediction_history():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
    SELECT *
    FROM prediction_history
    ORDER BY id DESC
    """

    try:
        cursor.execute(query)
        history = cursor.fetchall()

    except Exception as e:
        print(f"Error: {e}")
        history = []

    finally:
        cursor.close()
        connection.close()

    return history
