from django.shortcuts import render
from posts.models import Team,Services,Projects,References

def http_index(request):
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
