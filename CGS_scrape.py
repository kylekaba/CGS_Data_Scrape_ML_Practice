# This is a script to begin scraping Carnegie-Irvine Galaxy Survey (CGS)
import requests

url = 'https://cgs.obs.carnegiescience.edu/CGS/database_tables/sample1.html'
data = requests.get(url)

print(data.text)