from django.urls import path
from .views import (
    SkillList,
    QualificationList,
    ProjectList,
    ContactList,
    home,
    download_resume,
)

urlpatterns = [
    path('', home, name='home'),
    path('resume/', download_resume, name='download_resume'),

    path('api/skills/', SkillList.as_view()),
    path('api/qualifications/', QualificationList.as_view()),
    path('api/projects/', ProjectList.as_view()),
    path('api/contact/', ContactList.as_view()),
]