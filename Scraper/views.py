from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link


# Create your views here.

def Scraper(request):

    url = 'https://www.google.com'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    for link in soup.find_all('a'):

        link_address = link.get('href')
        link_text = link.string

        Link.objects.create(address=link_address, name=link_text)

    data = Link.objects.all()

    context = {
        'data': data
    }


    return render(request, 'scraper/result.html', context)
