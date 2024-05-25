from django.shortcuts import render
from django.views.generic import TemplateView, FormView,ListView,CreateView,DetailView
from .forms import ContactForm
from django.urls import reverse_lazy
from .models import Teacher

class Home_view(TemplateView):
    template_name = 'classroom/home.html'

class Thankyou(TemplateView):
    template_name = 'classroom/thankyou.html'

class ContactFormViews(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    
    success_url = reverse_lazy('classroom:thankyou') 

class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__" 
    success_url = reverse_lazy('classroom:thankyou') 

   
class TeacherListView(ListView):
    model =Teacher
    template_name = "teacher_list.html"
    queryset = Teacher.objects.order_by('first_name')
    context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    model = Teacher 
    context_object_name = 'teacher'
