import requests
from bs4 import BeautifulSoup
from datetime import date

def get_url_list():
    # Open the file in read mode, reads all line and returns a list with all the urls on the file
    with open("url.txt", "r") as file:
        lines = file.readlines()
        return lines

def get_investing_data():
    data_list = []
    # Loops the urls from the get_url_list()
    for url in get_url_list():

        # Gets the webpage content and parses it using BeautifulSoup
        page = requests.get(str(url.strip()))
        soup = BeautifulSoup(page.content, features="html.parser")

        # Find all elements (company_name) with the class "bold left noWrap elp plusIconTd"
        elements = soup.find_all("td", class_="bold left noWrap elp plusIconTd")

        # Scrapes the Index name
        index = soup.find("h1", class_="float_lang_base_1 relativeAttr").text.strip()

        # Loops each element (company_name) to extract specific values
        for element in elements:

            # Gets the id for each element (company_name)
            span_element = element.find("span", class_="alertBellGrayPlus")
            data_id = span_element.get("data-id")

            # The class name changes with the data_id
            last_price_class = f"pid-{data_id}-last"
            min_price_class = f"pid-{data_id}-low"
            max_price_class = f"pid-{data_id}-high"

            # That is why I had to create a changing class name for each element (company_name)
            min_price = soup.find("td",class_=min_price_class).text
            max_price = soup.find("td",class_=max_price_class).text
            last_price = soup.find("td",class_=last_price_class).text

            # Gets the current date
            event_date = str(date.today())

            # Appends the extracted data to "data_list"
            data_list.append([index, element.text, data_id, last_price, min_price, max_price, event_date])

    return data_list
