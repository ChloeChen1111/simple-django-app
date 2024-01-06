# urls.py
from django.urls import path
from .views import download_notes # Import the view

urlpatterns = [
    # ... other url patterns ...
    path('download/', download_notes, name='download_notes'), # The new URL pattern for downloading notes
]
