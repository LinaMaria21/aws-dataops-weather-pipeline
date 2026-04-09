\# AWS DataOps Weather Pipeline 🌦️



\## Overview

This project is an end-to-end ETL (Extract, Transform, Load) pipeline that collects weather data from an external API, processes it, and loads it into a PostgreSQL data warehouse.



\## Architecture

API → Raw JSON → Transformation (Python/pandas) → CSV → PostgreSQL



\## Features

\- Extracts real-time weather data from API

\- Stores raw data (JSON)

\- Transforms data using pandas

\- Loads structured data into PostgreSQL

\- Logging for monitoring pipeline execution



\## Tech Stack

\- Python

\- AWS S3 (simulated)

\- PostgreSQL

\- pandas

\- Git/GitHub



\## How to Run

```bash

python main.py

