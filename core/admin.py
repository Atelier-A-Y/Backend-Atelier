"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import (
    Categoria,
    Compra,
    Favorito,
    Roupa,
    User,
)


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


@admin.register(Roupa)
class RoupaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria')
    search_fields = ('nome', 'preco', 'categoria__descricao')
    list_filter = ('categoria',)
    ordering = ('nome', 'preco', 'categoria')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)
    list_filter = ('descricao',)
    ordering = ('descricao',)


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'status', 'total')
    readonly_fields = ('data',)
    search_fields = ('usuario', 'status')
    list_filter = ('usuario', 'status')
    ordering = ('status', 'usuario', 'data', 'total')
    list_per_page = 25


@admin.register(Favorito)
class FavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'livro', 'nota', 'data_atualizacao')
    search_fields = ('usuario__email', 'livro__titulo', 'comentario')
    list_filter = ('nota', 'data_atualizacao')
    ordering = ('-data_atualizacao',)
    list_per_page = 25
    readonly_fields = ('data_atualizacao',)
