import datetime

import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from pyarrow import nulls


def app(request):
    url = request.GET.get('url')
    validity = request.GET.get('validity')
    shortcode = request.GET.get('shortcode')

    if validity is None:
        validity = 0

    data = {
        "shortLink": f"http://127.0.0.1:8000/{shortcode}",
        "expiry": (datetime.datetime.now() + datetime.timedelta(minutes=int(validity))).isoformat()
    }
    return JsonResponse({"status": "success", "data": data})