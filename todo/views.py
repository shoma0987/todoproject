from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = "list.html"
    model = TodoModel

class TodoDetail(DetailView):
    # pk指定が必要になる
    template_name = "detail.html"
    model = TodoModel

class TodoCreate(CreateView):
    template_name = "create.html"
    model = TodoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("list")
    # createを起動した後に、どこのurlに繋がっていくかを示す
    # classの中でreverse関数を使うときは、reverse_lazyでdefの中ではreverseを使うルール
    # reverseの由来はviewsがurlsを引用してくるため(通常とは逆)
class TodoDelete(DeleteView):
    template_name = "delete.html"
    model = TodoModel
    success_url = reverse_lazy("list")
    #上記の”list”はurls.pyのpathでつけたニックネームを参照
class TodoUpdate(UpdateView):
    template_name = "update.html"
    model = TodoModel
    fields = ("title","memo","priority","duedate")
    success_url = reverse_lazy("list")


