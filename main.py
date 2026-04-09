import logging
import os
from datetime import datetime

from scripts.extract_api import extract_weather_data
from scripts.transform import transform_weather_data
from scripts.load_to_redshift import load_to_redshift_simulation
# -----------------------------
# LOGGING SETUP
# -----------------------------
os.makedirs("logs", exist_ok=True)

log_file = "logs/pipeline.log"

logging.getLogger().handlers.clear()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)
def run_pipeline():

    logging.info("Pipeline started")

    try:
        # 1. Extract
        raw_file, processed_file = extract_weather_data()
        logging.info(f"Extracted: {raw_file}")

        # 2. Transform
        final_file = transform_weather_data(processed_file)
        logging.info(f"Transformed: {final_file}")

        # 3. Load (Redshift simulation)
        load_to_redshift_simulation(final_file)
        logging.info("Loaded into Redshift (simulation)")

        # 4. Success
        logging.info("Pipeline SUCCESS")
        print("DONE")

    except Exception as e:
        logging.error(f"Pipeline FAILED: {str(e)}")
        print("ERROR - check logs")

if __name__ == "__main__":
    run_pipeline()