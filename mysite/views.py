from django.shortcuts import render

def http_base(request):    
    return render(request,"index.html")