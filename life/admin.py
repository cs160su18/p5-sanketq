from django.contrib import admin
from life.models import *

# SuperUser: 
# 
# User: admin
# Email: admin@admin.com 
# Password: passwordpasswordpassword
# 
# Regular User:

# User: joe
# Password: bizarreadventure

# Register your models here.
admin.site.register(Item)
admin.site.register(Deal)
admin.site.register(Shopper)