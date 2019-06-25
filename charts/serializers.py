from rest_framework import serializers

from charts.models import Stock


class StockSerializer(serializers.Serializer):
    data = serializers.FloatField()
    date = serializers.DateField()

    def create(self, validated_data):
        return Stock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.data = validated_data.get('data', instance.data)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance