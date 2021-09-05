from django.contrib import admin
from. models import Contact, Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id','product_name','category','subcategory','price','desc','pub_date','image']

# class ProductAdmin(admin.ModelAdmin):
    # list_display=['product_id','product_name','']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['fname','lname','email','mno','message']

