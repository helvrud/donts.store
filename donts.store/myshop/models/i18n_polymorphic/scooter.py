# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from shop.money import Money, MoneyMaker
from djangocms_text_ckeditor.fields import HTMLField
from shop.money.fields import MoneyField
from parler.managers import TranslatableManager
from parler.models import TranslatedFields
from .product import Product
from .smartphone import OperatingSystem

from cms.models.fields import PlaceholderField



class ScooterModel(Product):
    """
    A generic smart phone model, which must be concretized by a model `SmartPhone` - see below.
    """
    BATTERY_TYPES = (
        (1, "LG battery"),
        (2, "Chinese battery"),
    )
    #~ WIFI_CONNECTIVITY = (
        #~ (1, "802.11 b/g/n"),
    #~ )
    #~ BLUETOOTH_CONNECTIVITY = (
        #~ (1, "Bluetooth 4.0"),
        #~ (2, "Bluetooth 3.0"),
        #~ (3, "Bluetooth 2.1"),
    #~ )
    battery_type = models.PositiveSmallIntegerField(
        _("Battery type"),
        choices=BATTERY_TYPES,
    )

    battery_capacity = models.DecimalField(
        _("Battery capacity"),
        max_digits=3,
        decimal_places=1,
        help_text=_("Battery capacity in Ah"),
        null = True,
    )

    #~ ram_storage = models.PositiveIntegerField(
        #~ _("RAM"),
        #~ help_text=_("RAM storage in MB"),
    #~ )

    #~ wifi_connectivity = models.PositiveIntegerField(
        #~ _("WiFi"),
        #~ choices=WIFI_CONNECTIVITY,
        #~ help_text=_("WiFi Connectivity"),
    #~ )

    #~ bluetooth = models.PositiveIntegerField(
        #~ _("Bluetooth"),
        #~ choices=BLUETOOTH_CONNECTIVITY,
        #~ help_text=_("Bluetooth Connectivity"),
    #~ )

    bluetooth = models.BooleanField(
        _("Bluetooth"),
        default=True,
        help_text=_("Bluetooth Connectivity"),
    )

    operating_system = models.ForeignKey(
        OperatingSystem,
        verbose_name=_("Operating System"),
    )

    width = models.DecimalField(
        _("Width"),
        max_digits=5,
        decimal_places=0,
        help_text=_("Width in cm"),
    )

    height = models.DecimalField(
        _("Height"),
        max_digits=5,
        decimal_places=0,
        help_text=_("Height in cm"),
    )
    depth = models.DecimalField(
        _("Depth"),
        max_digits=5,
        decimal_places=0,
        help_text=_("Height in cm"),
    )

    weight = models.DecimalField(
        _("Weight"),
        max_digits=5,
        decimal_places=1,
        help_text=_("Weight in kg"),
    )

    #~ screen_size = models.DecimalField(
        #~ _("Screen size"),
        #~ max_digits=4,
        #~ decimal_places=2,
        #~ help_text=_("Diagonal screen size in inch"),
    #~ )
    max_speed = models.DecimalField(
        _("Maxumum speed"),
        max_digits=4,
        decimal_places=0,
        help_text=_("Maxumum speed in km/h"),
    )
    mileage = models.DecimalField(
        _("Maxumum mileage"),
        max_digits=4,
        decimal_places=0,
        help_text=_("Maxumum mileage per one battery charge in km"),
    )    
    
    power = models.DecimalField(
        _("Motor power"),
        max_digits=4,
        decimal_places=0,
        help_text=_("Motor power in km"),
    )    
    
    
    multilingual = TranslatedFields(
        description=HTMLField(
            verbose_name=_("Description"),
            configuration='CKEDITOR_SETTINGS_DESCRIPTION',
            help_text=_("Full description used in the catalog's detail view of Scooters."),
        ),
    )

    default_manager = TranslatableManager()



    #~ placeholder = PlaceholderField('product_details')
    class Meta:
        verbose_name = _("Electric Scooter")
        verbose_name_plural = _("Electric Scooters")

    def get_price(self, request):
        """
        Return the starting price for instances of this smart phone model.
        """
        if not hasattr(self, '_price'):
            if self.variants.exists():
                currency = self.variants.first().unit_price.currency
                aggr = self.variants.aggregate(models.Min('unit_price'))
                self._price = MoneyMaker(currency)(aggr['unit_price__min'])
            else:
                self._price = Money()
        return self._price

    def is_in_cart(self, cart, watched=False, **kwargs):
        from shop.models.cart import CartItemModel
        try:
            product_code = kwargs['product_code']
        except KeyError:
            return
        cart_item_qs = CartItemModel.objects.filter(cart=cart, product=self)
        for cart_item in cart_item_qs:
            if cart_item.product_code == product_code:
                return cart_item

    def get_product_variant(self, **kwargs):
        try:
            return self.variants.get(**kwargs)
        except ScooterVariant.DoesNotExist as e:
            raise ScooterModel.DoesNotExist(e)


class ScooterVariant(models.Model):
    product = models.ForeignKey(
        ScooterModel,
        verbose_name=_("Scooter Model"),
        related_name='variants',
    )

    product_code = models.CharField(
        _("Product code"),
        max_length=255,
        unique=True,
    )

    unit_price = MoneyField(
        _("Unit price"),
        decimal_places=3,
        help_text=_("Net price for this product"),
    )

    #~ storage = models.PositiveIntegerField(
        #~ _("Internal Storage"),
        #~ help_text=_("Internal storage in MB"),
    #~ )
    
    
    #~ battery_capacity = models.DecimalField(
        #~ _("Battery capacity"),
        #~ max_digits=3,
        #~ decimal_places=1,
        #~ help_text=_("Battery capacity in Ah"),
    #~ )

    
    COLORS = (
        ("white", "white"),
        ("black", "black"),
    )

    color = models.CharField(
        _("Color"),
        max_length=255,
       choices=COLORS,
       default='white',
    )    
    def get_price(self, request):
        return self.unit_price



#~ if __name__ == '__main__':
    #~ import myshop.models as models 
    #~ s = models.ScooterModel.objects.all()[0]
    
    
    
    

