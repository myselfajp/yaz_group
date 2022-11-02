from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import Team,Services,Projects,References
# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Services)
admin.site.register(Team)
admin.site.register(Projects)
admin.site.register(References)



