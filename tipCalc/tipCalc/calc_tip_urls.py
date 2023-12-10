from django.urls import path
from .views import calculate_tip

app_name = 'tipCalc'

urlpatterns = [
    path('', calculate_tip, name='calculate_tip'),
]
