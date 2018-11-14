from django.contrib import admin
from .models import Usuario, Medicamento, MedicamentoUsuario

admin.site.register(Usuario)
admin.site.register(Medicamento)
admin.site.register(MedicamentoUsuario)

# Register your models here.
