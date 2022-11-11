from django.shortcuts import render,get_object_or_404
from .models import Services,Gallery

def http_services_single(request,s_id):
    services = Services.objects.all()
    service=get_object_or_404(Services ,id=s_id)
    context={
        "services":services,
        "service":service,
    }
    return render(request,"service-details.html",context=context)


def http_gallery(request,s_id):
    pictures=Gallery.objects.filter(project__id=s_id)
    services = Services.objects.all()
    context={
        "services":services,
        "pictures" : pictures,
    }
    return render(request,"gallery.html",context=context)
