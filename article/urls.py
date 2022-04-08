from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name = "article_index"),
    path('detail/<int:aid>',views.articleDetail,name = "article_detail")
]