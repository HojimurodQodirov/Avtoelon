import requests
from bs4 import BeautifulSoup
import random

base_url = "https://avtoelon.uz/avto/sedan/chevrolet/gentra/pozitsiya-3/?auto-fuel=1&auto-car-transm=2&car-dwheel=1&auto-run[to]=50000&auto-color=1&price-currency=1&price[from]=1%20111&price[to]=19%20000&year[from]=2020&year[to]=2024"


response = requests.get(base_url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all('div', class_='row list-item a-elem')

random.shuffle(posts)

posts = posts[:10]

for post in posts:
    image = post.find('img')['src'] if post.find('img') else None
    title = post.find('a', class_='a-el-info-title').text.strip() if post.find('a', class_='a-el-info-title') else None
    relative_link = post.find('a', class_='a-el-info-title')['href'] if post.find('a', class_='a-el-info-title') else None
    full_link = f"{base_url}{relative_link}" if relative_link else None
    price = post.find('span', class_='price').text.strip() if post.find('span', class_='price') else None
    description = post.find('div', class_='desc').text.strip() if post.find('div', class_='desc') else None
    region = post.find('a', class_='a-info-text__region').text.strip() if post.find('a', class_='a-info-text__region') else None
    date = post.find('span', class_='date').text.strip() if post.find('span', class_='date') else None
    views = post.find('span', class_='nb-views-int').text.strip() if post.find('span', class_='nb-views-int') else None

    print(f"Название: {title}")
    print(f"Ссылка: {full_link}")
    print(f"Цена: {price}")
    print(f"Описание: {description}")
    print(f"Город: {region}")
    print(f"Дата: {date}")
    print(f"Просмотры: {views}")
    print(f"Изображение: {image}")
    print('-' * 50)




