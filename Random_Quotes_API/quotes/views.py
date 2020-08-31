from django.shortcuts import render
from quotes.models import Quotes, Language
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quotes.serializers import LanguageSerializer, QuoteSerializer
import random
# Create your views here.

class LanguageApiView(APIView):
    def get(self,request,*args,**kwargs):
        lang_all_obj = Language.objects.all()
        lang_ser_all_obj = LanguageSerializer(lang_all_obj, many = True)
        return Response(lang_ser_all_obj.data)

class QuotesApiView(APIView):
    def get(self, request, *args, **kwargs):
        quote_all_obj = Quotes.objects.all()
        quote_ser_all_obj = QuoteSerializer(quote_all_obj, many = True)
        return Response(quote_ser_all_obj.data)
    def post(self, request, *args, **kwargs):
        quotes_all_obj = QuoteSerializer(data = request.data)
        if quotes_all_obj.is_valid():
            new_obj = quotes_all_obj.save()
            new_ser_obj = QuoteSerializer(new_obj)
            return Response(new_ser_obj.data)
        else:
            return Response(new_ser_obj.errors)

class QuotesUpdateApiView(APIView):
    def put(self, request, id, *args, **kwargs):
        quote_obj = Quotes.objects.get(id = id)
        quote_ser_obj = QuoteSerializer(instance= quote_obj, data = request.data, partial = True)
        if quote_ser_obj.is_valid():
            updated_obj = quote_ser_obj.save()
            updated_ser_obj = QuoteSerializer(updated_obj)
            return Response(updated_ser_obj.data)
        else:
            return Response(updated_ser_obj.errors)


class RandomQuoteApiView(APIView):
    def get(self, request, *args, **kwargs):
        r = []
        all_obj = Quotes.objects.all()
        for i in all_obj:
            r.append(i.id)
        n = random.choice(r)
        the_obj = Quotes.objects.get(id = n)
        the_ser_obj = QuoteSerializer(the_obj)
        return Response(the_ser_obj.data)

class RandomLangQuoteApiView(APIView):
    def get(self, request,lang, *args, **kwargs):
        lang_obj = Language.objects.filter(language_name = lang)
        print(lang_obj)
        if lang_obj:
            r = []
            all_obj = Quotes.objects.filter(lang = lang_obj[0])
            if all_obj:
                for i in all_obj:
                    r.append(i.id)
                n = random.choice(r)
                the_obj = Quotes.objects.get(id = n)
                the_ser_obj = QuoteSerializer(the_obj)
                return Response(the_ser_obj.data)
            else:
                raise Exception("No quotes with that language")
        else:
            raise Exception("not a valid language")

class LangQuoteApiview(APIView):
    def get(self, request,lang, *args, **kwargs):
        lang_obj = Language.objects.filter(language_name = lang)
        if lang_obj:
            quote_all_obj = Quotes.objects.filter(lang = lang_obj[0])
            if quote_all_obj:
                quote_ser_all_obj = QuoteSerializer(quote_all_obj, many = True)
                return Response(quote_ser_all_obj.data)
            else:
                raise Exception(" no quotes found with that language")
        else:
            raise Exception("not a valid language")