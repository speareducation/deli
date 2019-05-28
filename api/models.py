from django.db import models


# Create your models here.
class Sandwich(models.Model):
    TURKEY = 1
    ROAST_BEEF = 2
    VEGGIE = 3
    BASE_CHOICES = (
        (TURKEY, 'Turkey'),
        (ROAST_BEEF, 'Roast Beef'),
        (VEGGIE, 'Veggie'),
    )
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    base = models.IntegerField(choices=BASE_CHOICES, default=1)
    price = models.DecimalField(default=0.00,max_digits=14,decimal_places=2)
    toppings = models.ManyToManyField('Topping')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name_plural = "sandwiches"

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    extra = models.DecimalField(default=0.00, max_digits=14, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name
