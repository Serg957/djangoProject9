from django.shortcuts import render
from django.views.generic import TemplateView


def func_temp(reguest):
    return render(reguest, 'second_task/funk_template.html')

class Class_temp(TemplateView):
    template_name = 'second_task/class_template.html'