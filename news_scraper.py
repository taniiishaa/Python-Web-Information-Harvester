import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Step 1: Choose the news website
URL = "https://www.bbc.com/news"   # You can replace with NDTV, The Hindu, etc.
response = requests.get(URL)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headlines (BBC uses h3 for headlines)
headlines = []
for h in soup.find_all(["h2", "h3"]):  
    text = h.get_text(strip=True)
    if text and len(text.split()) > 3:  # Filter short/irrelevant text
        headlines.append(text)

# Step 4: Remove duplicates and limit to top 10
unique_headlines = list(dict.fromkeys(headlines))[:10]

# Step 5: Save to file
file_name = "news_headlines.txt"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(f"Top News Headlines - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    for i, headline in enumerate(unique_headlines, 1):
        f.write(f"{i}. {headline}\n")
    f.write("\n--- End of Headlines ---\n")

# Step 6: Print output for user
print("✅ Scraping complete!")
print(f"📂 Headlines saved in {file_name}")
print("\nTop Headlines:")
for i, headline in enumerate(unique_headlines, 1):
    print(f"{i}. {headline}")
