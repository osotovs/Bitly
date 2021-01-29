from dotenv import load_dotenv
load_dotenv()

import argparse
import os
import requests
from urllib.parse import urlparse

TOKEN= os.getenv('BITLY_TOKEN')

URLS= {
    'base_url': 'https://api-ssl.bitly.com/v4/',
    'short_url': 'bitlinks/',
    'count_clicks': '/clicks/summary'
}
HEADER= {'Authorization': TOKEN}

def shorten_link(url):
    payload= {'long_url': url}
    response= requests.post(
        f"{URLS['base_url']}{URLS['short_url']}",
        headers= HEADER,
        json= payload
    )
    response.raise_for_status()
    bitlink= response.json()    
    return bitlink['id']

def get_arguments():
    parser= argparse.ArgumentParser('программа выведет короткую ссылку')
    parser.add_argument('link', help='link')
    args= parser.parse_args()
    return args.link

def summary_clicks(bitly_link):    
    payload= {'units': -1}
    response= requests.get(
        f"{URLS['base_url']}{URLS['short_url']}{bitly_link}{URLS['count_clicks']}",
        params= payload,
        headers= HEADER
    )
    response.raise_for_status()
    bitlink= response.json()
    return bitlink['total_clicks']

def check_link(url,bitly_link):
    if not check_bitly(bitly_link):
        try:            
            bitlink= shorten_link(url)            
            print('сокращенная ссылка: ',bitlink)
            print('количество кликов: ', summary_clicks(bitlink))
        except requests.exceptions.HTTPError:            
            print('неверная ссылка1')
            exit()
    else:
        try:
            bitlink= summary_clicks(bitly_link)
            print('количество кликов: ',bitlink)
        except requests.exceptions.HTTPError:
            print('1неверная ссылка')
            exit()

def check_bitly(url):
    response= requests.get(
        f"{URLS['base_url']}{URLS['short_url']}{url}",
        headers= HEADER
        )    
    return response.ok

def main():
    # url= input('введите ссылку:\n')
    url= get_arguments()
    parsed_url= urlparse(url)
    bitly_link= parsed_url.netloc+ parsed_url.path 
    check_link(url, bitly_link)

if __name__ == '__main__':   
    main()
