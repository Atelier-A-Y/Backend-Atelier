"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        (_('Personal Info'), {
            'fields': ('name',)
        }),

        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Roupa)
admin.site.register(models.Continente)
admin.site.register(models.Categoria)
admin.site.register(models.Compra)
admin.site.register(models.Venda)
admin.site.register(models.Tamanho)
admin.site.register(models.TipoPagamento)
admin.site.register(models.Carrinho)
admin.site.register(models.Favorito)

