from django.urls import path
from quotes.views import LanguageApiView, QuotesApiView, QuotesUpdateApiView, RandomQuoteApiView, RandomLangQuoteApiView, LangQuoteApiview
urlpatterns = [
    path("quotes", QuotesApiView.as_view()),
    path("quotes/<int:id>", QuotesUpdateApiView.as_view()),
    path("quotes/random", RandomQuoteApiView.as_view()),
    path("quotes/random/<str:lang>", RandomLangQuoteApiView.as_view()),
    path("quotes/lang/<str:lang>", LangQuoteApiview.as_view() )
    ]