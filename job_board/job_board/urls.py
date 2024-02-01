from django.urls import path

from job_board.views import index, job_detail

urlpatterns = [
    path('', index, name='home'),
    path('/job/<int:pk>/', job_detail, name='detail')
]