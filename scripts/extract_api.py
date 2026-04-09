

import requests
import json
import pandas as pd
from datetime import datetime
import boto3


# -----------------------------
# DATA QUALITY CHECK
# -----------------------------
def validate_data(data):
    try:
        weather = data["current_weather"]

        if weather["temperature"] is None:
            print("❌ Missing temperature")
            return False

        if weather["windspeed"] < 0:
            print("❌ Invalid windspeed")
            return False

        print("✅ Data validation passed")
        return True

    except Exception as e:
        print("❌ Data structure broken:", e)
        return False


# -----------------------------
# MAIN EXTRACTION FUNCTION
# -----------------------------
def extract_weather_data():

    url = "https://api.open-meteo.com/v1/forecast?latitude=4.14&longitude=-73.63&current_weather=true"

    response = requests.get(url)
    data = response.json()

    # Validate data BEFORE processing
    if not validate_data(data):
        print("Pipeline stopped due to bad data")
        return None, None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"weather_{timestamp}"

    # -----------------------------
    # RAW DATA (JSON)
    # -----------------------------
    raw_path = f"raw/{file_name}.json"
    with open(raw_path, "w") as f:
        json.dump(data, f, indent=4)

    # -----------------------------
    # TRANSFORM DATA (CLEAN TABLE)
    # -----------------------------
    weather = data["current_weather"]

    df = pd.DataFrame([{
        "temperature_c": weather["temperature"],
        "windspeed_kmh": weather["windspeed"],
        "weather_time": weather["time"],
        "source": "open-meteo-api"
    }])

    processed_path = f"processed/{file_name}.csv"
    df.to_csv(processed_path, index=False)

    # -----------------------------
    # UPLOAD TO S3
    # -----------------------------
    s3 = boto3.client("s3")
    bucket = "linam-dataops-project"

    s3.upload_file(raw_path, bucket, f"raw/{file_name}.json")
    s3.upload_file(processed_path, bucket, f"processed/{file_name}.csv")

    print("🚀 Pipeline completed successfully!")
    print("Uploaded RAW + PROCESSED data to S3")

    return raw_path, processed_path