from django.shortcuts import render,HttpResponse
from django.views import View
from user.models import Goods

# Create your views here.

#商品添加
class AddView(View):
    """添加功能"""
    def get(self,request):
        '''页面显示'''
        return render(request,'add_shangpin.html')
    def post(self,request):
        #接收数据
        good_name = request.POST.get('name')
        good_introduce = request.POST.get('introduce')
        good_num = request.POST.get('num')
        good_price = request.POST.get('price')
        good_picture = request.POST.get('img')


        #处理数据
        # 判断数据是否全
        if not all([good_name, good_introduce, good_num, good_price, good_picture]):
            return render(request, 'register.html', {'errmsg': '数据不完整'})


        #存入数据库
        Goods.objects.create(good_name=good_name, good_introduce=good_introduce, good_num=good_num,
                             good_price=good_price, good_picture=good_picture)

        return HttpResponse('存入成功')


#商品列表页
class ListView(View):
    def get(self, request):
        uid = request.session.get('uid')
        GOOD = Goods.objects.all()

        return render(request, 'list.html', locals())






