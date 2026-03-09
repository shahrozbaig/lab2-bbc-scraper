import requests
from bs4 import BeautifulSoup
import pandas as pd

urls = [
    "https://www.bbc.com/sport/cricket/articles/crl433ljkw4o",
    "https://www.bbc.com/sport/cricket/articles/cgr1rv851w1o"
]

headers = {"User-Agent": "Mozilla/5.0"}

data = []

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No Title"

    # Article paragraphs
    paragraphs = soup.find_all("p")
    content = " ".join([p.get_text(strip=True) for p in paragraphs])

    data.append({
        "title": title,
        "content": content,
        "url": url
    })

df = pd.DataFrame(data)

print("\nScraped BBC Cricket Articles\n")
print(df)

# Save file
df.to_csv("bbc_cricket_articles.csv", index=False)

print("\nData saved to bbc_cricket_articles.csv")