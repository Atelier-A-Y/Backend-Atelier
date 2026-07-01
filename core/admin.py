"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import (
    Favorito,
    User,
)
from core import models

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']
    search_fields = ['email', 'name', 'groups__name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'foto', 'tipo_usuario')}),
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
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'nota', 'data_atualizacao')
    search_fields = ('usuario__email', 'livro__titulo', 'comentario')
    list_filter = ('nota', 'data_atualizacao')
    ordering = ('-data_atualizacao',)
    list_per_page = 25
    readonly_fields = ('data_atualizacao',)


class CompraAdmin(admin.ModelAdmin):

    def get_exclude(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return ("user",)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Roupa)
admin.site.register(models.Continente)
admin.site.register(models.Categoria)
admin.site.register(models.Compra, CompraAdmin)
admin.site.register(models.Venda)
admin.site.register(models.Tamanho)
admin.site.register(models.TipoPagamento)
