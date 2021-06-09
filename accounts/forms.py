from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserAdminCreationForm(UserCreationForm):
	'''a Custom form for getting new users'''
	class Meta:
		model=get_user_model()
		fields=['email']
