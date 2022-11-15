from django.contrib import admin
from .models import Question, Quiz, UserResult

# Register your models here.
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(UserResult)