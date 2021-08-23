from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from django.http import JsonResponse

from requests import get


def dataJson(requests):

#Method one with our defined Data
    response = [
        {
            
    'ip': '8.8.8.8',
    'version': 'IPv4',
    'city': 'Mountain View',
    'region': 'California',
    'region_code': 'CA',
    'country_code': 'US',
    'country_code_iso3': 'USA',
    'country_name': 'United States',
    'country_capital': 'Washington',
    'country_tld': '.us',
    'continent_code': 'NA',
    'in_eu': 'false',
    'postal': '94035',
    'latitude': 37.386,
    'longitude': -122.0838,
    'timezone': 'America/Los_Angeles',
    'utc_offset': '-0700',
    'country_calling_code': '+1',
    'currency': 'USD',
    'currency_name': 'Dollar',
    'languages': 'en-US,es-US,haw,fr',
    'country_area': 9629091.0,
    'country_population': 310232863.0,
    'asn': 'AS15169',
    'org': 'Google LLC',
}]


#Method Two
    # response = requests.GET.get('https://ipapi.co/8.8.8.8/json')
    # # return render(requests,'dataJson.html',{'response':response})
    # return JsonResponse({'response':response})

    context = {'response' :response}

    return render(requests,'dataJson.html',{'response':response})


#Simple Function
    # res  = get('https://ipapi.co/8.8.8.8/json/')
    # return  HttpResponse({res.json()})