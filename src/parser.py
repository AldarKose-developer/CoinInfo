import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 OPR/79.0.4143.73'
}


class CryptoNews():

    def get_source_html(url):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get(url)
            with open("source.html", "w", encoding="utf-8") as file:
                file.write(driver.page_source)
        except Exception as _ex:
            print(_ex)
        finally:
            driver.close()
            driver.quit()

    def get_urls(url):
        with open("source.html", encoding='utf-8', mode='r') as file:
            news = BS(file, 'html.parser')
        items = news.find_all("div", class_='post-card-inline__header')
        urls = []
        for item in items:
            item_url = item.find('a').get('href')
            urls.append(item_url)
        return urls

    def get_news(coin):
        print('Please be patient, parsing paragraphs will take some time :3')
        url = f'https://cointelegraph.com/tags/{coin}'
        CryptoNews.get_source_html(url)

        news = {}

        for url in CryptoNews.get_urls(url):
            try:
                response = requests.get(url='https://cointelegraph.com' + url, headers=headers)
            except requests.exceptions.ConnectionError as _ex:
                print(_ex)

            soup = BS(response.content, 'html.parser')

            try:
                item_name = soup.find('h1', class_='post__title')
            except Exception as _ex:
                item_name = None

            try:
                item_description = soup.find_all('p')
            except Exception as _ex:
                item_description = None

            text = ' '.join([p.text for p in item_description])
            news.update({item_name.text: text})
        return news
