from django.contrib import admin
from .models import (
    User,
    Patient,
    Doctor,
    Questionnaire,
    QuestionnaireResponse,
    Question,
    Alert,
    Message,
    UsageStatistic,
)

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Questionnaire)
admin.site.register(QuestionnaireResponse)
admin.site.register(Question)
admin.site.register(Alert)
admin.site.register(Message)
admin.site.register(UsageStatistic)
