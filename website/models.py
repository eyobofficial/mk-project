from django.db import models

from core.models import BaseModel


class Company(BaseModel):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, blank=True)
    motto = models.TextField('company motto', blank=True)
    short_description = models.TextField('short company description')
    business_description = models.TextField()
    about_description = models.TextField('about us')
    service_description = models.TextField('short service description')
    product_description = models.TextField('short product description')
    contact_description = models.TextField('short contact description')
    address = models.TextField(help_text='Use comman to separate address')
    phone1 = models.CharField('phone line 1', max_length=30)
    phone2 = models.CharField('phone line 2', max_length=30, blank=True)
    fax = models.CharField('FAX', max_length=30, blank=True)
    pobox = models.CharField('P.O.Box', max_length=10, blank=True)
    email = models.CharField(max_length=50)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    logo = models.ImageField(
        upload_to='logo/',
        null=True, blank=True,
        help_text='Recommended size is 220x220 pixels'
    )
    fevicon = models.ImageField(upload_to='fevicon/', null=True, blank=True)
    wallpaper = models.ImageField(
        upload_to='wallpaper/',
        null=True, blank=True,
        help_text='Recommended size is 1080x960 pixels'
    )

    class Meta:
        verbose_name = 'Company Detail'
        verbose_name_plural = 'Company Details'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        company = Company.objects.first()
        if not company or self.pk:
            return super().save(*args, **kwargs)
        return

    def splitted_title(self):
        splitted_title = self.title.split()
        first_part = str(splitted_title[0])
        rest_part = ' '.join(splitted_title[1:])
        return (first_part, rest_part)

    def formatted_address(self):
        address_list = self.address.split(',')
        return '<br>'.join(address_list)


class Service(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class ProductCatagory(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Product Catagory'
        verbose_name_plural = 'Product Catagories'

    def __str__(self):
        return self.title


class Product(BaseModel):
    catagory = models.ForeignKey(
        ProductCatagory,
        related_name='products',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_featured = models.BooleanField('Featured', default=False)
    image = models.ImageField(
        upload_to='products/',
        null=True, blank=True,
        help_text='Recommended size is 1080x720 pixels'
    )

    class Meta:
        order_with_respect_to = 'catagory'

    def __str__(self):
        return self.title


class Subscriber(BaseModel):
    email = models.EmailField(max_length=50, unique=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.email


class Message(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    is_seen = models.BooleanField('seen', default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.name
