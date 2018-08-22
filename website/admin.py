from django.contrib import admin

from .models import Company, Service, ProductCatagory, Product, Subscriber, \
    Message


# Set Admin Site Header and Title
admin.site.site_header = 'Michael Tesfaye Importer'
admin.site.site_title = 'Michael Tesfaye Importer'
admin.site.index_title = 'Welcome To Michael Tesfaye Website Administration'


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'modified']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'modified']


@admin.register(ProductCatagory)
class ProductCatagoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_product_count', 'modified']

    def get_product_count(self, obj):
        return obj.products.count()
    get_product_count.short_description = 'Product Count'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'catagory', 'modified']
    list_filter = ['catagory']
    search_fields = ['title']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_date']
    search_fields = ['email']

    def subscribed_date(self, obj):
        return obj.created


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'sent_date', 'is_seen']
    readonly_fields = ['name', 'email', 'message', 'sent_date']
    exclude = ['is_seen']
    search_fields = ['name', 'email', 'message']
    ordering = ['-created', 'is_seen']

    def sent_date(self, obj):
        return obj.created.strftime('%I:%M %p - %b %d, %Y')
    sent_date.short_description = 'sent date'

    def change_view(self, request, object_id):
        message = Message.objects.get(pk=object_id)
        message.is_seen = True
        message.save()
        return super().change_view(request, object_id)
