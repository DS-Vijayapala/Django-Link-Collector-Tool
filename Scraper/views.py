from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

# Create your views here.

def Scraper(request):

    if request.method == 'POST':

        url = request.POST.get('site','')

        response = requests.get("http://"+url)
        soup = BeautifulSoup(response.text, 'html.parser')


        for link in soup.find_all('a'):

            link_address = link.get('href')
            link_text = link.string

            Link.objects.create(address=link_address, name=link_text)

            return HttpResponseRedirect('/')

    else:

        data = Link.objects.all()



    return render(request, 'scraper/result.html', context={'data': data})


def delete(request):

    Link.objects.all().delete()

    return render(request, 'scraper/result.html')
