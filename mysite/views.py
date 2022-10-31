from django.shortcuts import render
from posts.models import Team,Services,Projects,References

def http_index(request):
    team = Team.objects.all()[0:4]
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



def http_aboup_us(request):
    team = Team.objects.all()[0:4]
    projects = Projects.objects.all()
    services = Services.objects.all()
    references = References.objects.all()
    context={
        "team":team,
        "projects":projects,
        "services":services,
        "references" : references,
    }
    return render(request,"about_us.html",context=context)


def http_contact_us(request):
    team = Team.objects.all()[0:4]
    projects = Projects.objects.all()
    services = Services.objects.all()
    references = References.objects.all()
    context={
        "team":team,
        "projects":projects,
        "services":services,
        "references" : references,
    }
    return render(request,"contact_us.html",context=context)


def http_qoute(request):
    team = Team.objects.all()[0:4]
    projects = Projects.objects.all()
    services = Services.objects.all()
    references = References.objects.all()
    context={
        "team":team,
        "projects":projects,
        "services":services,
        "references" : references,
    }
    return render(request,"qoute.html",context=context)


def http_projects(request):
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
    return render(request,"projects.html",context=context)


def http_our_team(request):
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
    return render(request,"our_team.html",context=context)