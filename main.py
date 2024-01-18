import requests
from bs4 import BeautifulSoup

def get_google_flights_prices(origin, destination, departure_date, return_date):
    # Configurações da requisição
    url = f'https://www.google.com/travel/flights/search?tfsid=I2lodHRwczovL2ZvcmN0cy5jb20vdHJhY2tpbmdzL2F1Z3VzL2FuZHJvaWQvZ2l0aHViL2F1Z3VzLWluZGlhbC8yMDIyLTAxLTIyJnJvbw&as_oq={origin}+to+{destination}+{departure_date}+{return_date}&as_occt=any&as_flt=m&as_sli=OW1lZGlhbC8yMDIyLTAxLTIy&as_tsc=1&as_qdr=y&as_prmd=imvns&as_dor=j&as_sd=lg'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    # Faz a requisição
    response = requests.get(url, headers=headers)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Faz o parse da página HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontra os elementos com as informações de preço
        price_elements = soup.find_all('span', {'class': 'JQXeW'})

        # Extrai e retorna os preços
        prices = [int(''.join(pe.findAll(text=True))) for pe in price_elements]
        return prices
    else:
        print(f'Requisição falhou com status code {response.status_code}')
        return []

# Exemplo de uso
origin = 'NYC'
destination = 'LAX'
departure_date = '2023-06-01'
return_date = '2023-06-05'

prices = get_google_flights_prices(origin, destination, departure_date, return_date)
print(f'Preços encontrados: {prices}')