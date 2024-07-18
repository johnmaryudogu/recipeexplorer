from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Ensure you have an index.html template

# Initialize the OpenAI client
#openai.api_key = 'sk-proj-Zz2X360jEA0tXRiMCkcnT3BlbkFJbDrCiAtwAGYWx8o9M3BI'
import json
import logging
from openai import OpenAI
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import Recipe

# Set up logging
logger = logging.getLogger(__name__)

# Initialize the OpenAI client
client = OpenAI(api_key=settings.OPENAI_API_KEY)

@api_view(['POST'])
@permission_classes([AllowAny])
def generate_steps(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        logger.error(f'Recipe with ID {recipe_id} not found.')
        return JsonResponse({'error': 'Recipe not found'}, status=404)

    prompt = f"Generate step-by-step instructions to prepare the following recipe:\n\nName: {recipe.name}\n\nIngredients:\n{recipe.ingredients}\n\nSteps:"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        steps = response.choices[0].message.content.strip()
        return JsonResponse({'steps': steps}, status=200)
    except Exception as e:
        logger.error(f"Error generating steps: {str(e)}")
        return JsonResponse({'error': 'Failed to generate steps'}, status=500)
