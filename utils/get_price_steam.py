import requests
from bs4 import BeautifulSoup



def itensSugestion(name):
    request = requests.get(f'https://store.steampowered.com/search/suggest?term={name}&f=games&cc=BR&realm=1&l=brazilian&v=15653108&excluded_content_descriptors%5B%5D=3&excluded_content_descriptors%5B%5D=4&use_store_query=1').content
    soup = BeautifulSoup(request, 'html.parser')

    name = soup.select('.match_name')

    names = []
    for name in name:
        name = name.text
        names.append(name)
    return names

def getItemSteam(name):
    request = requests.get(f'https://store.steampowered.com/search/suggest?term={name}&f=games&cc=BR&realm=1&l=brazilian&v=15653108&excluded_content_descriptors%5B%5D=3&excluded_content_descriptors%5B%5D=4&use_store_query=1').content
    soup = BeautifulSoup(request, 'html.parser')

    name = soup.select_one('.match_name').text
    image = soup.select_one('.match_img img').get('src')
    price = soup.select_one('.match_price').text
    url = soup.select_one('a').get('href')

    return {'name': name, 'image': image, 'price': price, 'url': url}
