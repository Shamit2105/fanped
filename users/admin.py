from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser  
    list_display = ['email', 'username', 'country', 'phno', 'sec_questions', 'sec_answer']

admin.site.register(CustomUser, CustomUserAdmin)