from django.shortcuts import render
from urllib.request import urlopen
import json
from django.core.paginator import Paginator
from django.http import HttpResponse

response = urlopen("https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-languages.json")
database = json.loads(response.read())
id_country = len(database[0]["country"])
lang = []
for p in range(len(database)):
    for x in range(len(database[p]['languages'])):
        lang.append(database[p]['languages'][x])
list_languages = sorted(list(dict.fromkeys(lang)))

id_lang = {}
for i in range(len(list_languages)):
    id_lang[list_languages[i]] = list_languages[i]

for index in range(len(database)):
    database[index]["id"] = index


def index(request):
    return render(request, 'main/index.html')


def ListCountriesPage(request):
    paginator = Paginator(database, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/list_countries.html', {'page_obj': page_obj, 'data': database})


def languages(request):
    return render(request, 'main/languages.html', {'list_languages': list_languages, 'id_lang': id_lang, })


def country(request, id):
    country_name = database[id]["country"]
    country_languages = database[id]["languages"]
    return render(request, 'main/country.html',
                  {'country_name': country_name, 'country_languages': country_languages, })


def languages_index(request, id_language):
    alphabet = 'A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z'
    array3 = []
    a = ''
    if id_language in alphabet:
        for i in database:
            for j in i['languages']:
                if j[0] == id_language:
                    array3.append(j)
        array3 = set(array3)
        array3 = sorted(array3)
        paginator = Paginator(array3, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        array1 = {
            'title': 'languages',
            'array': array3,
            'page_object': page_obj
        }
        return render(request, 'languages.html', array1)
    else:
        for i in database:
            for j in i['languages']:
                if id_language == j:
                    a += i['country'] + ', '
        a = a[:-2]
        array1 = {
            'title': id_language,
            'array': a
        }
        return render(request, 'main/lang_count.html', array1)
