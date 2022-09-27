
# from .views import dept
# from django.urls import path
# app_name='departments'

# urlpatterns = [
#     path("details/",dept,name='dept')
# ]



from django.urls import path
from departments.views import details,sample,dept_det,add_dept,update_dept,delete_dept
app_name='departments'

urlpatterns = [
     path("sample/",sample,name='sample' ),
     path("details/",details,name='details' ),
     path('details/<int:id>',dept_det,name='departmentdet'),
     path('details/add/',add_dept,name='add_dept'),
     path('details/update/<int:id>',update_dept,name='update_dept'),
     path('details/delete/<int:id>',delete_dept,name='delete_dept'),
]
