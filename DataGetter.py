import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# List of news sites to scrape
news_sites = ["https://www.aftonbladet.se", "https://www.expressen.se", "https://www.svd.se", "https://omni.se", "https://dn.se", ]

# Initialize sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Dictionaries to store headlines and sentiments
headlines = {}
sentiments = {}

# Scrape headlines and analyze sentiment for each news site
for site in news_sites:
    page = requests.get(site)
    soup = BeautifulSoup(page.content, "html.parser")
    h1_tags = soup.find_all("h1")
    h2_tags = soup.find_all('h2') 
    h3_tags = soup.find_all('h3')
    h4_tags = soup.find_all('h4')
    headlines[site] = [tag.get_text() for tag in h1_tags + h2_tags + h3_tags + h4_tags]
    sentiments[site] = [analyzer.polarity_scores(headline)["compound"] for headline in headlines[site]]
    print(sentiments)

avg_sentiments = {site: sum(sentiments[site])/len(sentiments[site]) for site in sentiments}

# Plot the data
# x = [i for i, _ in enumerate(avg_sentiments)]
# bar_width = 0.2

# plt.bar(x, [avg_sentiments[site] for site in news_sites], width=bar_width)
# plt.xticks([i + bar_width/2 for i in x], news_sites)
# plt.xlabel("News Sites")
# plt.ylabel("Sentiment")
# plt.title("Sentiment Analysis of News Headlines")
# plt.show()

for site in news_sites:
    print(avg_sentiments[site])


import pandas as pd
import datetime

# Create a dataframe from the avg_sentiments dictionary
df = pd.DataFrame.from_dict(avg_sentiments, orient='index', columns=['Sentiment'])
df.reset_index(inplace=True)
df.rename(columns={'index':'Site'}, inplace=True)

# Add a timestamp column to the dataframe
df['Timestamp'] = datetime.datetime.now()

try:
    # Read the existing Excel file
    existing_df = pd.read_excel("sentiments.xlsx")
    # Append the new data to the existing dataframe
    df = existing_df.append(df, ignore_index=True)
except FileNotFoundError:
    pass

# Save the dataframe to an Excel file
df.to_excel("sentiments.xlsx", index=False)
