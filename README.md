# 📰 Python Web Information Harvester

[![Project Status](https://img.shields.io/badge/Status-Functional%20%7C%20Automated-28a745?style=for-the-badge)](./news_scraper.py)
[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python)](./news_scraper.py)
[![Focus](https://img.shields.io/badge/Focus-Data%20Extraction%20%7C%20Web%20Parsing-E62C00?style=for-the-badge)]()

---

## 💡 Project Overview: The Data Harvesting Utility

This repository contains a concise, production-ready Python script designed for **automated, targeted information harvesting** from web sources. It serves as a foundational component for various applications, including market monitoring, competitive intelligence, or personalized news dashboards.

The utility's primary focus is demonstrating robust **HTML parsing, intelligent data filtration, and structured output management**—essential skills for any data-intensive project.

## 🛠️ Core Engineering & Data Pipeline

This project is a complete, self-contained data pipeline showcasing the following technical mastery:

### 1. **Robust HTML Parsing (BeautifulSoup)**
* **Intelligent Tag Selection:** Utilizes a multi-tag search (`["h2", "h3"]`) to maximize headline capture rate across different webpage layouts, demonstrating adaptability.
* **Contextual Filtering:** Implements a text length filter (`len(text.split()) > 3`) to automatically exclude short, irrelevant text fragments (e.g., footers, single-word links) that often pollute scraper output.

### 2. **Data Integrity & Deduplication**
* **Efficient Uniqueness Check:** Leverages the speed of a dictionary conversion (`list(dict.fromkeys(headlines))`) to perform in-memory deduplication, guaranteeing that only unique headlines proceed to the output stage.
* **Output Constraint:** Enforces a strict **Top 10** output limit, prioritizing data relevance and managing output verbosity.

### 3. **Structured Persistence & Reporting**
* **Time-Series Tracking:** Integrates the `datetime` library to generate a precise timestamp for the scraping run, turning the output file into a **time-series record** of external data.
* **Readable Output Format:** Stores the final structured data (`news_headlines.txt`) in an ordered, human-readable format, ready for quick consumption or ingestion by other systems.

---

## 🚀 Quick Start & Usage

This application requires Python 3.x and two external libraries.

1.  **Clone the repository:**
    ```bash
    git clone [Your-Repo-Link]
    cd [Your-Repo-Name]
    ```

2.  **Install Dependencies:**
    ```bash
    pip install requests beautifulsoup4
    ```

3.  **Execute the Harvester:**
    ```bash
    python news_scraper.py
    ```

### Output

The script instantly generates a human-readable file named `news_headlines.txt` in the root directory and prints the results directly to the console.

## 🎯 Scalability & Future State

This foundational code is designed to be easily scaled into a more complex **Microservice**, demonstrating its value beyond a simple CLI tool:

* **API Integration:** Replace the file output with an API call to publish data to a central database (e.g., MongoDB, PostgreSQL).
* **Scheduling:** Integrate with workflow tools like **Apache Airflow or cron** to automate harvesting and build a continuous data stream.
* **URL Parameterization:** Convert the hardcoded `URL` into a command-line argument using `argparse` for dynamic source switching.

This project validates my ability to design and implement professional, data-centric Python utilities with a focus on **efficiency, structure, and reliability**.
