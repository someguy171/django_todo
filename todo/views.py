from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse
from django.utils import timezone

from .models import Lesson, Homework
from .forms import HomeworkForm, LessonForm, FetchForm

class IndexView(generic.ListView):
    template_name = "todo/index.html"
    context_object_name = "homework_list"
    
    def get_queryset(self):
        return Homework.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['hw_form'] = HomeworkForm()
        context['lesson_form'] = LessonForm()
        # context['fetch_form']
        return context
    
    def post(self, request):
        if 'homework_submit' in request.POST:
            form = HomeworkForm(request.POST)
            if form.is_valid():
                formInfo = form.cleaned_data
                print(formInfo)
                h = Homework(
                    title=formInfo['title'],
                    lesson=formInfo['lesson'],
                    due_date=formInfo['due_date'],
                    description=formInfo['description'],
                    attachment=formInfo['attachment'],
                    link=formInfo['link'],
                    reminder=formInfo['reminder']
                )
                h.save()
        elif 'class_submit' in request.POST:
            form = LessonForm(request.POST)
            if form.is_valid():
                formInfo = form.cleaned_data
                l = Lesson(
                    name=formInfo['name'],
                    teacher=formInfo['teacher'],
                    color=formInfo['color']
                )
                l.save()
        """
        elif 'fetch_submit' in request.POST:
            form = FetchForm(request.POST)
            if form.is_valid():
                formInfo = form.cleaned_data
        """
        
        return HttpResponseRedirect(reverse("todo:index"))


class DetailView(generic.DetailView):
    model = Homework
    template_name = "todo/detail.html"
    
    def post(self, request, pk):
        Homework.objects.filter(id=pk).delete()
        return HttpResponseRedirect(reverse('todo:index'))