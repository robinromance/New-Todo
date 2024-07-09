from django.urls import path
from New_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_view/', views.add_view, name="add_view"),
    path('delete_page/<int:id>', views.delete_page, name="delete_page"),
    path('delete_view/<int:id>', views.delete_view, name="delete_view"),
    path('update_view/<int:id>', views.update_view, name="update_view"),
    path('update_record/<int:id>', views.update_record, name="update_record"),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout')
]
