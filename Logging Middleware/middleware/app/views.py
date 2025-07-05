from django.shortcuts import render

import requests
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin


def registration(request):
    url = "http://20.244.56.144/evaluation-service/register"

    data = {
        "email": "220701508@rajalakshmi.edu.in",
        "name": "Shyam Srinivasan",
        "mobileNo": "9025238389",
        "githubUsername": "ShyamSrinivasan10",
        "rollNo": "220701508",
        "accessCode": "cWyaXW"
    }
    header = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiIyMjA3MDE1MDhAcmFqYWxha3NobWkuZWR1LmluIiwiZXhwIjoxNzUxNjk0NjA3LCJpYXQiOjE3NTE2OTM3MDcsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiI0YzJlMWI5Ny1lYjFlLTQ1NTQtOTQzZC1mNGRmYjdkZTIxMjgiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJzaHlhbSBzcmluaXZhc2FuIiwic3ViIjoiNGJkNTA3NDMtNTZlYi00NmM3LWJhY2QtNjZjZDAyYjcxMjA2In0sImVtYWlsIjoiMjIwNzAxNTA4QHJhamFsYWtzaG1pLmVkdS5pbiIsIm5hbWUiOiJzaHlhbSBzcmluaXZhc2FuIiwicm9sbE5vIjoiMjIwNzAxNTA4IiwiYWNjZXNzQ29kZSI6ImNXeWFYVyIsImNsaWVudElEIjoiNGJkNTA3NDMtNTZlYi00NmM3LWJhY2QtNjZjZDAyYjcxMjA2IiwiY2xpZW50U2VjcmV0IjoiR3NLV1BHUXZHbVBUd3NzRCJ9.9GExOxPVGb2GHnUKzojCElHnc4QNNsqESI4YijAQG4Q"
    }

    try:
        response = requests.post(url, json=data, headers=header)
        response.raise_for_status()
        return JsonResponse({"status": "success", "response": response.json()})
    except requests.exceptions.RequestException as e:
        return JsonResponse({"status": "error", "message": str(e)})


def authentication(request):
    url = "http://20.244.56.144/evaluation-service/auth"

    data = {
        "email": "220701508@rajalakshmi.edu.in",
        "name": "shyam srinivasan",
        "rollNo": "220701508",
        "accessCode": "cWyaXW",
        "clientID": "4bd50743-56eb-46c7-bacd-66cd02b71206",
        "clientSecret": "GsKWPGQvGmPTwssD"
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return JsonResponse({"status": "success", "response": response.json()})
    except requests.exceptions.RequestException as e:
        return JsonResponse({"status": "error", "message": str(e)})


def logs(request):
    url = "http://20.244.56.144/evaluation-service/logs"

    data = {
        "stack": "backend",
        "level": "error",
        "package": "handler",
        "message": "received string, expected bool"
    }

    header = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiIyMjA3MDE1MDhAcmFqYWxha3NobWkuZWR1LmluIiwiZXhwIjoxNzUxNjk0NjA3LCJpYXQiOjE3NTE2OTM3MDcsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiI0YzJlMWI5Ny1lYjFlLTQ1NTQtOTQzZC1mNGRmYjdkZTIxMjgiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJzaHlhbSBzcmluaXZhc2FuIiwic3ViIjoiNGJkNTA3NDMtNTZlYi00NmM3LWJhY2QtNjZjZDAyYjcxMjA2In0sImVtYWlsIjoiMjIwNzAxNTA4QHJhamFsYWtzaG1pLmVkdS5pbiIsIm5hbWUiOiJzaHlhbSBzcmluaXZhc2FuIiwicm9sbE5vIjoiMjIwNzAxNTA4IiwiYWNjZXNzQ29kZSI6ImNXeWFYVyIsImNsaWVudElEIjoiNGJkNTA3NDMtNTZlYi00NmM3LWJhY2QtNjZjZDAyYjcxMjA2IiwiY2xpZW50U2VjcmV0IjoiR3NLV1BHUXZHbVBUd3NzRCJ9.9GExOxPVGb2GHnUKzojCElHnc4QNNsqESI4YijAQG4Q"
    }

    try:
        response = requests.post(url, json=data, headers=header)
        response.raise_for_status()
        return JsonResponse({"status": "success", "response": response.json()})
    except requests.exceptions.RequestException as e:
        return JsonResponse({"status": "error", "message": str(e)})
