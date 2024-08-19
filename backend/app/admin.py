from django.contrib import admin
from app.models import Paciente, Cadeira, Agendar
# Register your models here.
admin.site.register(Paciente)
admin.site.register(Cadeira)
admin.site.register(Agendar)