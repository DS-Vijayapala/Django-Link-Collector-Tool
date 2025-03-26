from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.

def Scrape(request):

    url = 'https://www.google.com'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    link_address = []

    for link in soup.find_all('a'):
        link_address.append(link.get('href'))

    context = {
        'link_address': link_address
    }


    return render(request, 'scraper/result.html', context)
