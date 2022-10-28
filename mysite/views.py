from django.shortcuts import render
from posts.models import Team,Services,Projects,References

def http_index(request):
    team = Team.objects.all()[0:4]
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


def http_aboup_us(request):
    team = Team.objects.all()
    context={
        "team":team,
    }
    return render(request,"about_us.html",context=context)