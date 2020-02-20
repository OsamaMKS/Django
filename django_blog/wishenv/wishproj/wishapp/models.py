from django.db import models
from django.contrib.auth.models import User
import uuid


class List(models.Model):
    owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='list_logo', null=True, blank=True)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name


class ListItems(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    logo = models.ImageField(upload_to="item_logo",null=True,blank=True)
    link = models.URLField(max_length=128,db_index=True,null=True,blank=True)

    def __str__(self):
        return self.name

# class List(models.Model):
#     owner = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120)
#     description = models.TextField()
#     logo = models.ImageField(upload_to='list_logo', null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
# class WishList(models.Model):
#     list = models.ForeignKey(List, on_delete=models.CASCADE)
#     name = models.CharField(max_length=120)
#     description = models.TextField()
#     logo = models.ImageField(upload_to='WishList_logo',null=True, blank=True)
#
#     def __str__(self):
#         return self.name

# class ItemsWish(models.Model):
#     name = models.CharField(max_length=120)
#     description = models.TextField()
#     logo = models.ImageField(upload_to='item_logo',null=True, blank=True)
#     wish = models.ManyToManyField(WishList)
#
#     def __str__(self):
#         return self.name
