# qa_sessions/admin.py
from django.contrib import admin
from .models import QASession, Question, Answer

admin.site.register(QASession)
admin.site.register(Question)
admin.site.register(Answer)


# Register your models here.
