from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

# Register your models here.
class CustomUserAdmin(UserAdmin):
	'''dedine admin model fro custom User Model with no username'''
	fieldsets=(
		(None,{'fields':('email', 'password',)}),
		(_('Personal Info'),{'fields':('first_name','last_name',)}),
		(_('Permissions'),{'fields':('is_active', 'is_staff','is_superuser', 'groups','user_permissions',)}),
		(_('Important Dates'), {'fields':('last_login','date_joined',)}),

	)
	add_fieldsets=(
		(None,{'classes':('wide',),
				'fields':('email','password1', 'password2',),
			}),
		)
	list_display=('email','first_name','last_name', 'is_staff',)
	search_fields=('email','first_name','last_name',)
	ordering = ('email',)

admin.site.register(get_user_model(), CustomUserAdmin)