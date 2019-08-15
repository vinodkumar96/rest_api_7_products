from django.conf.urls import url
from .import views
app_name='Rapp_APIView_GET_POST'
urlpatterns = [
    url(r'^$',views.input),
    url(r'^link$',views.link),
    url(r'^display$',views.display),
    url(r'^productapi$',views.ProductList.as_view()),
]