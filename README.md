

The project showcases an end-to-end ETL (Extract, Transform, Load) pipeline that:
retrieves weather data from an external API, processes it, and loads it into a PostgreSQL data warehouse for analysis.

Architecture
API → Raw JSON → Transformation (Python / pandas) → CSV → PostgreSQL
Features
Extracts real-time weather data from an external API
Stores raw data in JSON format for traceability
Cleans and transforms data using pandas
Loads structured data into PostgreSQL
Implements logging for monitoring and debugging
Tech Stack
Python
AWS S3 (simulated)
PostgreSQL
pandas
Git & GitHub


\## How to Run

```bash

python main.py

