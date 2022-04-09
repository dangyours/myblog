from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index,name = "article_index"),
    path('detail/<int:aid>',views.articleDetail,name = "article_detail"),
    path('write/<int:aid>',views.articleWrite,name="article_write"),
    path('write/save/<int:aid>',views.articleSave,name="article_save"),
    path('delete/<int:aid>',views.articleDelete,name="article_delete"),
]