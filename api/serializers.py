# api/serializers
from rest_framework import serializers
from .models import Sandwich,Topping


class SandwichSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sandwich
        fields = ('id', 'name', 'base', 'price','created', )


class SandwichDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sandwich
        fields = ('id', 'name', 'description','base', 'price', 'created',
                  'updated', )


class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = ('id', 'name', 'description', 'extra', 'created',
                  'updated', )


class SandwichToppingSerializer(serializers.ModelSerializer):
    toppings = serializers.PrimaryKeyRelatedField(many=True,queryset=Topping.objects.filter())
    #toppings = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Sandwich
        fields = ('id', 'name', 'toppings')

    def create(self, validated_data):
        toppings_data = validated_data.pop('toppings')
        for topping_data in toppings_data:
            sandwich = Sandwich.objects.create(**topping_data)

        return sandwich
