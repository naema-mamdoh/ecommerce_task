from django.contrib import admin
from .models import cart, category,product,card
# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(card)
admin.site.register(cart)