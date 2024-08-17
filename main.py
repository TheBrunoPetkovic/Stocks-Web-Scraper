import requests
from bs4 import BeautifulSoup
import sys
import time

# Set the encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.mojedionice.com/dionice"

response = requests.get(url)

if response.status_code == 200:
   print("Request successful")
else:
   print(f"Failed to retrieve the page. Status code: {response.status_code}")
   
site_content = BeautifulSoup(response.content, 'html.parser')

with open('site_content.txt', 'w', encoding='utf-8') as file:
   file.write(site_content.prettify())
   
# Find all <a> tags that contain stock names
stock_names = []
for tag in site_content.find_all('a', href=True):
   href = tag['href']
   if href.startswith('/dionica/'):
      stock_name = tag.text.strip()
      stock_names.append(stock_name)


# Write all found stock names to a text file
with open('stock_names.txt', 'w', encoding='utf-8') as file:
   for stock_name in stock_names:
      file.write(stock_name + '\n')
      
stock_data = []

for stock_name in stock_names:
   stock_url = f"https://www.mojedionice.com/dionica/{stock_name}"
   stock_response = requests.get(stock_url)
    
   if stock_response.status_code == 200:
      stock_content = BeautifulSoup(stock_response.content, 'html.parser')
        
      print(f"uspia accessat {stock_name}")
      
      site_content = BeautifulSoup(response.content, 'html.parser')

      with open(f"site_content_{stock_name}.txt", 'w', encoding='utf-8') as file:
         file.write(site_content.prettify())
         
      # Extract the stock price as an example
      #price = stock_content.find('span', {'id': 'stock-price-id'}).text.strip()
        
      # Store the data
      #stock_data.append({'name': stock_name, 'price': price})
   else:
      print("nisan uspia accessat {stock_name} ")
      
   #time.sleep(15)


   


