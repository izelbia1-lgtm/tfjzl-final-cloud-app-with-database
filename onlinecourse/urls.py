from django.urls import path

from . import views
urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # User authentication
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

    # Course pages
    path('<int:pk>/', views.course_details, name='course_details'),
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Exam routes (required for Question 7)
    path('<int:course_id>/exam/', views.exam, name='exam'),
    path('<int:course_id>/submit_exam/', views.submit_exam, name='submit_exam'),
]
