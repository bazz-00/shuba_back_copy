from user.models import User
from django.db import models
from django.core.validators import RegexValidator


phoneNumberRegex = RegexValidator(regex=r"^\+375\d{9}$")


class SpecialityOrder(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        db_table = 'specialityorder'

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16)
    # photo = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    speciality = models.ManyToManyField(SpecialityOrder)


    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.title


class OrderComments(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        db_table = 'order_comments'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user, self.order)


class OrderPhotos(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    photo = models.URLField()

    class Meta:
        db_table = 'orderphotos'

    def __str__(self):
        return str(self.order)
