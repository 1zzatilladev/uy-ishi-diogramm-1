from django.contrib import admin
from .models import Answer,User,Question,Quiz,Result
# Register your models here.
admin.site.register(Answer)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Result)