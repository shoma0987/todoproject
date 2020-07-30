
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("todo.urls")),
    # 何もurlに記載がない時に、todo-appのurls.pyに繋ぎ込みが起こる仕組み
]
