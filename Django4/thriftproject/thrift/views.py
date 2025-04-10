from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView,DetailView
from django.urls import reverse_lazy
from .models import ThriftRegister,Purchased
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'thrifts'
    paginate_by = 6

    def get_queryset(self):
        sort_by = self.request.GET.get('sort_by','posted_at')

        order = self.request.GET.get('order','asc')

        if order == 'desc':
            sort_by = f'-{sort_by}'


        return ThriftRegister.objects.all().order_by(sort_by)

class ProductDetail(DetailView):
    template_name = 'detail.html'

    model = ThriftRegister

    def post(self,request,*args, **kwargs):
        product = self.get_object()

        user_email = request.user.email
        
        if user_email:
            send_mail(
                subject=f'商品購入のお知らせ：{product.title}',
                message=f'{product.title}を購入いただきありがとうございます！',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user_email],
            )

        purchased = Purchased.objects.create(
            user=request.user,
            product=product,
        )
        
        product.is_purchased = True
        product.save()

        return render(request, 'purchase_success.html',{'product':product})
    
class CategoryView(ListView):
    '''カテゴリページのビュー
    
    Attributes:
      template_name: レンダリングするテンプレート
      paginate_by: 1ページに表示するレコードの件数
    '''
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 3

    def get_queryset(self):
      '''クエリを実行する
      
      self.kwargsの取得が必要なため、クラス変数querysetではなく、
      get_queryset（）のオーバーライドによりクエリを実行する
      
      Returns:
        クエリによって取得されたレコード
      '''     
      # self.kwargsでキーワードの辞書を取得し、
      # categoryキーの値(Categorysテーブルのid)を取得
      category_id = self.kwargs['category']
      # filter(フィールド名=id)で絞り込む
      categories = ThriftRegister.objects.filter(
        category=category_id).order_by('-posted_at')
      # クエリによって取得されたレコードを返す
      return categories
    
def user_orders(request):
    orders = Purchased.objects.filter(user=request.user).order_by('-purchase_date')
    return render(request, 'mypage.html',{'orders':orders})