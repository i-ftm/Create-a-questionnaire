from django.urls import path
from .views import FormListCreateView, FormDetailView, SubmitResponseView

urlpatterns = [
    path('forms/', FormListCreateView.as_view(), name='form-list'),
    path('forms/<int:pk>/', FormDetailView.as_view(), name='form-detail'),
    path('forms/<int:form_id>/submit/', SubmitResponseView.as_view(), name='submit-response'),
]