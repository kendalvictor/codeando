from rest_framework.serializers import ModelSerializer, ValidationError
from ..models import DirectorioAncora, PalabraCorpus, TagCorpus


class DirectorioAncoraSerializer(ModelSerializer):

    def validate(self, attrs):
        print("attrs DirectorioAncoraSerializer", type(attrs), attrs)
        return attrs

    class Meta:
        model = DirectorioAncora
        fields = '__all__'


class PalabraCorpusSerializer(ModelSerializer):

    def validate(self, attrs):
        print("attrs PalabraCorpusSerializer", type(attrs), attrs)
        return attrs

    class Meta:
        model = PalabraCorpus
        fields = '__all__'


class TagCorpusSerializer(ModelSerializer):

    def validate(self, attrs):
        print("attrs TagCorpusSerializer", type(attrs), attrs)
        #raise ValidationError("msje")
        return attrs

    class Meta:
        model = TagCorpus
        fields = '__all__'
