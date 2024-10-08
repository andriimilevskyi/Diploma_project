from django.urls import path
from .views import CaseListCreate, CaseRetrieveUpdateDestroy

urlpatterns = [
    path('cases/', CaseListCreate.as_view(), name='case-list-create'),  # List and create cases
    path('cases/<int:pk>/', CaseRetrieveUpdateDestroy.as_view(), name='case-detail'),
    # Retrieve, update, or delete case
]
