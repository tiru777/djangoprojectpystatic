from django.http import HttpResponse

from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>hellow world</h2>")

def template_home(request):
    return render(request,"home.html")

def template_company(request):
    return render(request,"company.html")

# def template_data(request):
#     data = {"name":"akhil","age":120,"address":"rvp"}
#     return render(request,"index.html",context={"data":data})
