from rest_framework import serializers
from app import models


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Articles
        fields = ("id", "category", "title", "summary", "author")


def list(category: str | None) -> serializers.Serializer:
    if category is None:
        res = models.Articles.objects.select_related()
    else:
        res = models.Articles.objects.filter(category=category).all()
    return Serializer(res, many=True)


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
