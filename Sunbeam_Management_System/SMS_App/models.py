from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class admin(AbstractUser):
    employee_num = models.CharField(max_length=20)


class rooms(models.Model):
    room_name = models.CharField(max_length=15, unique=True, primary_key=True)
    room_price = models.PositiveSmallIntegerField()
    room_status = models.CharField(max_length=10)


class customers(models.Model):
    customer_num = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    contact_num = models.CharField(max_length=11)
    email = models.EmailField(max_length=30)
    room_name = models.ForeignKey(rooms, on_delete=models.CASCADE)
    guest = models.PositiveSmallIntegerField()
    checkin_date = models.CharField(max_length=20)
    checkout_date = models.CharField(max_length=20)
    num_of_days = models.PositiveSmallIntegerField()
    activity = models.CharField(max_length=30)
    status = models.CharField(max_length=100)
    price = models.IntegerField()
    code = models.IntegerField()


class items(models.Model):
    item_name = models.CharField(max_length=30, unique=True, primary_key=True)
    item_quantity = models.PositiveSmallIntegerField()
    item_inuse = models.PositiveSmallIntegerField()


class feedbacks(models.Model):
    feedback_num = models.AutoField(unique=True, primary_key=True)
    feed = models.CharField(max_length=100)
