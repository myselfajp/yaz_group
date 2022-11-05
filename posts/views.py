from django.shortcuts import render,get_object_or_404
from .models import Team,Projects,Services,References,Gallery

def http_post(request):    
    team = Team.objects.all()
    projects = Projects.objects.all()
    services = Services.objects.all()
    references = References.objects.all()
    context={
        "team":team,
        "projects":projects,
        "services":services,
        "references" : references,
    }
    return render(request,"index.html",context=context)


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
