from django.urls import path
from user import views
urlpatterns = [
    path(r'login/', views.LoginView.as_view(), name='login'),  # 登录
    path(r'register/', views.RegisterView.as_view(), name='register'),  # 注册
]
