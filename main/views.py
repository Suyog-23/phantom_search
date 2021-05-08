from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs
# Create your views here.

# homepage
def homepage(request):
    if request.method=='POST':
        search_query=request.POST['user_search']
        url = 'https://www.ask.com/web?q='+search_query
        res = requests.get(url)
        edited = bs(res.text, 'lxml')
        
        filtered = edited.find_all('div', {'class':'PartialRelatedSearch'})

        final_results = []

        for result in filtered:
            search_title = result.find(class_='PartialSearchResults-item-title').text
            search_url = result.find('a').find('href')
            search_description = result.find(class_='PartialSearchResults-item-abstract')

            filtered.append((search_title, search_url, search_description))

        context = {
            'final_results':final_results
        }
        return render(request, 'main/home.html', context)

    else:
        return render(request, 'main/home.html')
