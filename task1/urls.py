from django.urls import path
from task1 import views


urlpatterns = [
    # api_main_url/page_data/set/?url={my url}&waiting={waiting time after page load}&scroll={scrollin page}&validation_key={our-secret-key}
    path('page_data/set/', views.PageDataSetView.as_view()),
    path('page_data/get/', views.PageDataGetView.as_view()),
]