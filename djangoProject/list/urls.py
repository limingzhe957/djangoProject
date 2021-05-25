from django.urls import path
from list import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path(r'add_good', views.AddView.as_view(), name='add_good'),  # 商品增加
    path(r'list', views.ListView.as_view(), name='list'), #商品列表
]+static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
