from django.urls import path
from . import views

urlpatterns= [
    path('',views.endpoints),
    path('advocates/',views.advocates_list,name='advocates'),
    path('advocates/<str:username>/',views.advocate.as_view()),
    path('companies/',views.companies,name='companies'),
    path('companies/<str:name>/',views.company, name='company'),
]