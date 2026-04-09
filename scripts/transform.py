import pandas as pd

def transform_weather_data(file_path):

    # Read CSV (NOT JSON)
    df = pd.read_csv(file_path)

    # Simple DataOps transformation
    df["temperature_f"] = df["temperature_c"] * 9/5 + 32
    df["is_hot"] = df["temperature_c"] > 25

    output_path = file_path.replace(".csv", "_final.csv")

    df.to_csv(output_path, index=False)

    print("✅ Transformation complete:", output_path)

    return output_path