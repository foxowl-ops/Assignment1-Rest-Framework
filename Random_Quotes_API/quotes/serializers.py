from quotes.models import Language, Quotes
from rest_framework import serializers

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('language_name',)

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ('lang','content','author','source','rating')