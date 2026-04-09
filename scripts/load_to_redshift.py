import os
import pandas as pd
import psycopg2

def load_to_redshift_simulation(file_path):

    # read transformed file (CSV)
    df = pd.read_csv(file_path)

    conn = psycopg2.connect(
        host="localhost",
        database="weather_dw",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        port=5432
    )

    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO weather_data (
                temperature_c,
                windspeed_kmh,
                temperature_f,
                is_hot
            )
            VALUES (%s, %s, %s, %s)
        """, (
            row["temperature_c"],
            row["windspeed_kmh"],
            row["temperature_f"],
            row["is_hot"]
        ))

    conn.commit()
    cur.close()
    conn.close()

    print("Data loaded into PostgreSQL warehouse")
