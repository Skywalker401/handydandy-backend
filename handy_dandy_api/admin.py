from django.contrib import admin
from .models import User, Task, Appliance

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Appliance)
# Register your models here.
