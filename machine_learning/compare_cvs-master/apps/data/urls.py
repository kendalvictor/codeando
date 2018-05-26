from django.conf.urls import url

from .views import home, clean, generate_tokenized_words, generate_new_text

app_name = 'data'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^clean/$', clean, name='clean'),
    url(r'^generate_tokenized_words/$', generate_tokenized_words, name='generate_tokenized_words'),
    url(r'^generate_new_text/$', generate_new_text, name='generate_new_text'),


]
