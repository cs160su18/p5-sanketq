from django.contrib import admin
from life.models import *

# SuperUser: 
# 
# User: admin
# Email: admin@admin.com 
# Password: passwordpasswordpassword
# 

# Register your models here.
admin.site.register(Item)
admin.site.register(Deal)