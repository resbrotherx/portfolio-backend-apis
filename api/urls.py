from django.urls import path
from .views import *

urlpatterns = [
    path('portfolio/', portfolio_list_create),
    path('portfolio/<str:name>/', portfolio_detail),
    path('portfolio/id/<int:id>/', portfolio_update_delete),

    path('skills/', skills_api),

    path('experience/', experience_list_create),
    path('experience/<int:id>/', experience_update_delete),

    path('education/', education_list_create),
    path('education/<int:id>/', education_update_delete),

    path('feedback/', feedback_list_create),
    path('feedback/<int:id>/', feedback_update_delete),

    path('contact/', contact_api),
]
