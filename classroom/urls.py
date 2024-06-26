from django.urls import path
from .views import Thankyou,ContactFormViews,Home_view,TeacherCreateView,TeacherListView,TeacherDetailView,TeacherUpdateView,TeacherDeleteView

app_name = 'classroom'

urlpatterns = [
     path('', Home_view.as_view(), name='home'),
    path('thankyou/', Thankyou.as_view(), name='thankyou'),
    path('contact/', ContactFormViews.as_view(), name='contact'),
     path('create_teacher/', TeacherCreateView.as_view(), name='create_teacher'),
    path('teacher_list', TeacherListView.as_view(), name='teacher_list'),
   path('teacher_detail/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
   path('delete_teacher/<int:pk>/', TeacherDeleteView.as_view(), name='delete_teacher'),
   path('update_teacher/<int:pk>/', TeacherUpdateView.as_view(), name='update_teacher')

   

  
]
    
