import os, sys

from django.shortcuts import render

from image_upload.models import upload_image_class
from .recipe_recommendation.Recipe_recom import RecSys

# Create your views here.

def recipe_recommendation_view(request):
    ingredients = upload_image_class.objects.values_list('image_name', flat=True).order_by('uploaded_at')
    
    combined_ingredients = ", ". join(ingredients)
    
    recommendations = RecSys(combined_ingredients, N=5)
    
    context = {
        'recommendations': recommendations,
    }
    
    return render(request, 'recipe_recommendation_app/recommendations.html',context=context)
    