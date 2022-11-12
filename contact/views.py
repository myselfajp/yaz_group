from django.shortcuts import render
from posts.models import Team,Services,Projects,References
from .models import Message,Quote
# Create your views here.

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
    if request.method == 'POST':
        full_name=request.POST.get("full_name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")

        messageform=Message()

        messageform.full_name=full_name
        messageform.phone=phone
        messageform.mail=email
        messageform.subject=subject
        messageform.message=message
        if full_name and phone and message:
            messageform.save()
            context["message"]="Mesajınız aldık en kısa sürede size dönüş yapacağız"
        else:
            context["error"]="Tüm boşlukları doldurmanız gerekiyor"
            
        

    return render(request,"contact_us.html",context=context)



def http_quote(request):
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
    if request.method == 'POST':
        full_name=request.POST.get("full_name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        message=request.POST.get("message")

        quotemessage=Quote()

        quotemessage.full_name=full_name
        quotemessage.phone=phone
        quotemessage.mail=email
        quotemessage.message=message
        if full_name and phone and message:
            quotemessage.save()
            context["message"]="Mesajınız aldık en kısa sürede size dönüş yapacağız"
        else:
            context["error"]="Tüm boşlukları doldurmanız gerekiyor"

    return render(request,"quote.html",context=context)