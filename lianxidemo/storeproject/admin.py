from django.contrib import admin
from .models import Users, Labels, Classify, Big_Class, Brands, Sizes, Ad, Goods


# Register your models here.
admin.site.register(Users)
admin.site.register(Labels)
admin.site.register(Classify)
admin.site.register(Big_Class)
admin.site.register(Brands)
admin.site.register(Sizes)
admin.site.register(Ad)
admin.site.register(Goods)

