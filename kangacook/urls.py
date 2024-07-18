# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
 #   path('generate-steps/', views.generate_steps, name='generate-steps'),
  path('generate-steps/<int:recipe_id>/', views.generate_steps, name='generate-steps'),

]
