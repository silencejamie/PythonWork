from django.db import models


# Publisher對Book：一對多關係
class Publisher(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):  # 必須要繼承models.Model，python才會知道他是表
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    # 一對多操作：ORM會自動抓publish的id進行連結，並自動建立publish_id
    publish = models.ForeignKey('Publisher')  # 外鍵要建在【多】那方
    # 多對多操作：自動創造book_authors的表，另一種方法是自己建一個表且有兩個ForeignKey
    authors = models.ManyToManyField('Author')  # Good

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
