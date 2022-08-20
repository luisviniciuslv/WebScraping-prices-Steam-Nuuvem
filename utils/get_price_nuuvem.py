import requests
from bs4 import BeautifulSoup


def get_price_nuuvem(game):
    game = game.replace(' ', '-')
    request = requests.get(f'https://www.nuuvem.com/br-pt/catalog/search/{game}').content
    soup = BeautifulSoup(request, 'html.parser')
    
    integer = soup.select_one('.integer').text
    decimal = soup.select_one('.decimal').text
    url = soup.select_one('.product-card--wrapper').get('href')
    return {'price': f"R$ {integer}{decimal}",
            'url': url}
