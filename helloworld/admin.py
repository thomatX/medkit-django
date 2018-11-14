from django.contrib import admin
from .models import Usuario, Medicamento, MedicamentoUsuario, TarjetaCredito

admin.site.register(Usuario)
admin.site.register(Medicamento)
admin.site.register(MedicamentoUsuario)
admin.site.register(TarjetaCredito)

# Register your models here.
