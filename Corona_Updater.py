import time
import requests
from bs4 import BeautifulSoup

# Function for Finding World Data.
def world_data(base_url):
    res = requests.get(base_url).text
    soup = BeautifulSoup(res, 'html.parser')
    soup.encode('utf-8')

    # Total Case.
    Data = soup.find_all("div", {"class" : "maincounter-number"})
 
    return  [Data[0].text.strip(), Data[1].text.strip(),Data[2].text.strip()]

def india_data(url):
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    soup.encode('utf-8')
    data = soup.find_all("div", {"class" : "maincounter-number"})

    return [data[0].text.strip(), data[1].text.strip(), data[2].text.strip()]

# Main Funtion.
def main():
    main_url = "https://www.worldometers.info/coronavirus/"
    india_url = "https://www.worldometers.info/coronavirus/country/india/"
    print(world_data(main_url))
    print(india_data(india_url))

if __name__ == "__main__":
    main()