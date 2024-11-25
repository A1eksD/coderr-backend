from django.contrib import admin
from users.models import CustomUser, PasswordReset


admin.site.register(CustomUser)
admin.site.register(PasswordReset)