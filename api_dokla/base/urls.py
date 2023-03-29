from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns= [
    path('',views.endpoints),
    path('advocates/',views.advocates_list,name='advocates'),
    path('advocates/<str:username>/',views.advocate.as_view()),
    path('companies/',views.companies,name='companies'),
    path('companies/<str:name>/',views.company, name='company'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]