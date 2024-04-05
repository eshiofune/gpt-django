from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.individual_post, name="individual_post"),
    # path('generate-story/', views.generate_story_from_words, name='generate-story'),
    path(
        "generate-story/",
        views.get_story_from_description,
        name="get_story_from_description",
    ),
]
