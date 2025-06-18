from django.urls import path
from .views import JobCreateView, JobStatusView

urlpatterns = [
    path('jobs/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<str:job_id>/', JobStatusView.as_view(), name='job-status'),
]
