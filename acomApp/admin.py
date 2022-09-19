from django.contrib import admin
from .models.user import User, Userpage, bossAdmin, Supervisorpsm    


# Register your models here.

admin.site.register(Supervisorpsm)
admin.site.register(User)
admin.site.register(Userpage)
