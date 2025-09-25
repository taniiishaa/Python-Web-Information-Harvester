📌 Task Summary
- This repository contains a Python-based Command-Line Interface (CLI) application to scrape top news headlines from popular news websites (e.g., BBC, NDTV, The Hindu).
- The project was part of my internship tasks and demonstrates web scraping, data cleaning, file handling, and user-friendly CLI output.

🚀 My Development Process

1. Project Planning & Breakdown
   
- Defined the objective: Fetch top news headlines and save them neatly in a text file with timestamps.
- Chose Python for its powerful web scraping libraries (requests and BeautifulSoup).
- Planned to include:
  a. Deduplication of headlines
  b. Limiting output to top 10 headlines
  c. User-friendly console output

2. Core Implementation

- Fetched HTML content of the website using requests.
- Parsed and extracted headlines using BeautifulSoup.
- Filtered irrelevant text and removed duplicates.
- Saved cleaned headlines to a .txt file with a timestamp.
- Displayed headlines in the terminal in a readable format.

3. Extra Touches for Professional Look

- Optional: Colored console output using colorama to highlight success messages.
- Planned CSV/JSON export for future analysis.
- Potential to schedule daily scraping using Task Scheduler (Windows) or cron (Linux/Mac).

📖 Application Description
- This CLI application scrapes, filters, and saves the top news headlines from a website. It helps users quickly access current news in a structured and readable format.
- It demonstrates:
   a. Web scraping with Python
   b. Data cleaning and filtering
   c. File handling and timestamping
   d. CLI user interaction

✨ Key Features
- Top 10 Headlines : Only the most relevant headlines are saved.
- Timestamped Records : Each file records the date and time of scraping.
- Duplicate Removal : Ensures unique headlines are stored.
- User-Friendly CLI : Clear messages and easy-to-read output.
- Optional Enhancements : Color-coded terminal messages and CSV/JSON export.

⚙️ Technologies Used
- Language: Python 3.13
- Libraries: requests, beautifulsoup4, datetime, colorama (optional)
- Tools: VS Code / Terminal

🎯 Outcome
- This project resulted in a polished, interactive, and user-friendly CLI News Scraper. It showcases my ability to:
- Implement web scraping and parsing logic
- Handle files and save structured data
- Present data in a clear and engaging way
- Apply professional touches to make a project stand out on GitHub
