from django.shortcuts import render
from .models import Team,Projects,Services,References

def http_post(request):    
    team = Team.objects.all()
    projects = Projects.objects.all()
    services = Services.objects.all()
    references = References.objects.all()
    print(references)
    context={
        "team":team,
        "projects":projects,
        "services":services,
        "references" : references,
    }
    return render(request,"index.html",context=context)
