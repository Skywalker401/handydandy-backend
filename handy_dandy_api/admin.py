from django.contrib import admin
from .models import User, Task, Competencies

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Competencies)
# Register your models here.
