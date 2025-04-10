from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)
    
    def __str__(self):
        return self.title

class Gender(models.Model):
    gender = models.CharField(
        verbose_name='性別',
        max_length=6
    )

    def __str__(self):
        return self.gender
    
class ThriftRegister(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT,
        related_name='category'
    )

    title = models.CharField(
        verbose_name='商品名',
        max_length=100
    )

    gender = models.ForeignKey(
        Gender,
        verbose_name='性別',
        on_delete=models.PROTECT,
        related_name='genders'
    )

    size = models.CharField(
        verbose_name='サイズ',
        max_length=2
    )

    status = models.TextField(
        verbose_name='状態'
    )

    price = models.IntegerField(
        verbose_name='価格'
    )

    comment = models.TextField(
        verbose_name='コメント'
    )

    image1 = models.ImageField(
        verbose_name='イメージ１',
        upload_to="thrifts"
    )

    image2 = models.ImageField(
        verbose_name='イメージ２',
        upload_to='thrifts',
        blank=True,
        null=True
    )
    
    posted_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    is_purchased = models.BooleanField(
        default=False
        )

    def __str__(self):
        return self.title
    
class Purchased(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(ThriftRegister, on_delete=models.CASCADE)  # 購入した商品
    purchase_date = models.DateTimeField(auto_now_add=True)  # 購入日

    def __str__(self):
        return f"{self.user.username} bought {self.product.title} on {self.purchase_date}"