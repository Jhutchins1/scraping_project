from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

def scrape_data(url, driver):
    driver.get(url)
    time.sleep(5) 
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Scraping data
    country_span = soup.find('span', style="font-family: Arial, sans-serif;color: #337ab7;font-weight: bold; font-size: 40px;")
    country_name = country_span.text if country_span else 'Country name not found'

    country_data = soup.find_all("div", class_="ui-grid-col-2")
    population_data = country_data[1].find("span").text
    mva_per_capita_data = country_data[11].find("span").text

    cpi_ranking = None
    cpi_big_number = soup.find_all('span')
    for span in cpi_big_number:
        if 'font-size: 70px' in span.get('style', ''):
            cpi_ranking = span.text
            break

    return {
        'Country Name': country_name,
        'URL': url, 
        'Population Data': population_data,
        'MVA Per Capita Data': mva_per_capita_data,
        'CPI Ranking': cpi_ranking
    }

def get_urls():
    return [
    'https://stat.unido.org/',

    'https://stat.unido.org/country-profile/economics/AFG',

    'https://stat.unido.org/country-profile/economics/BHS',

    'https://stat.unido.org/country-profile/economics/CPV',

    'https://stat.unido.org/country-profile/economics/DNK',

    'https://stat.unido.org/country-profile/economics/EGY',

    'https://stat.unido.org/country-profile/economics/FIN',

    'https://stat.unido.org/country-profile/economics/DEU',

    'https://stat.unido.org/country-profile/economics/HUN',

    'https://stat.unido.org/country-profile/economics/IRL',

    'https://stat.unido.org/country-profile/economics/JPN',

    'https://stat.unido.org/country-profile/economics/KEN',

    'https://stat.unido.org/country-profile/economics/LBN',

    'https://stat.unido.org/country-profile/economics/MDG',

    'https://stat.unido.org/country-profile/economics/NZL',

    'https://stat.unido.org/country-profile/economics/OMN',

    'https://stat.unido.org/country-profile/economics/POL',

    'https://stat.unido.org/country-profile/economics/QAT',

    'https://stat.unido.org/country-profile/economics/RUS',

    'https://stat.unido.org/country-profile/economics/SWE' 
       
    ]

def run_scraping(urls):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    twenty_scrapes = []

    for url in urls:
        data = scrape_data(url, driver)
        if data:
            twenty_scrapes.append(data)
        else:
            print(f"Failed to scrape data for {url}")
        time.sleep(2)  

    driver.quit()

    with open('scraped_data.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Country Name', 'URL', 'Population Data', 'MVA Per Capita Data', 'CPI Ranking']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in twenty_scrapes:
            writer.writerow(data)


urls = get_urls()
run_scraping(urls)