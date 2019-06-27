from rest_framework import serializers

from charts.models import Stock


# Stock Serializer
class StockSerializer(serializers.Serializer):
    close_price = serializers.FloatField()
    date = serializers.DateField()

    def create(self, validated_data):
        return Stock.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.data = validated_data.get('close_price', instance.data)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
