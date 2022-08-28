from rest_framework import serializers
from django.forms.models import model_to_dict
from app import models


class SerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Articles
        fields = ("id", "category", "title", "summary")


def list(category: str | None) -> serializers.Serializer:
    if category is None:
        res = models.Articles.objects.all()
    else:
        res = models.Articles.objects.filter(category=category).all()
    return SerializerList(res, many=True)


def create(data: dict) -> models.Articles:
    article = models.Articles()
    article.category = data['category']
    article.summary = data['summary']
    article.title = data['title']
    article.uid = data['uid']
    article.firstParagraph = data['firstParagraph']
    article.body = data['body']
    article.save()
    return article

def update(id: int, data: dict) -> models.Articles:
    article = models.Articles.objects.filter(id=id).update(**data)
    return article

def delete(id: int):
    models.Articles.objects.filter(id=id).delete()

def get(id: int) -> dict:
    res = models.Articles.objects.filter(id=id).first()
    return model_to_dict(res)
