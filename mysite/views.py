from django.shortcuts import render

def http_base(request):    
    return render(request,"index.html")
def http_base2(request):    
    return render(request,"index2.html")