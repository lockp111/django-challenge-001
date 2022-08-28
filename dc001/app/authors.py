from rest_framework import serializers
from app import models


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Authors
        fields = ("id", "name", "picture")


def list() -> serializers.Serializer:
    res = models.Authors.objects.all()
    return Serializer(res, many=True)


def create(data: dict) -> models.Authors:
    author = models.Authors.objects.create(**data)
    return author


def update(id: int, data: dict) -> models.Authors:
    author = models.Authors.objects.filter(id=id).update(**data)
    return author

def delete(id: int):
    models.Authors.objects.filter(id=id).delete()