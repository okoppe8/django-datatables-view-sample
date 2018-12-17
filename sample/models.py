from django.db import models


# Create your models here.
class Item(models.Model):
    # 県名
    pref_name = models.CharField(
        max_length=4,
    )

    # 市町村名
    name = models.CharField(
        max_length=15,
    )

    # ふりがな
    furigana = models.CharField(
        max_length=30,
    )

    # 郵便番号
    zipcode = models.CharField(
        max_length=8,
    )

    # 住所
    address = models.CharField(
        max_length=100,
    )

    # 電話番号
    tel = models.CharField(
        max_length=13,
    )

    # 自治体コード
    code = models.CharField(
        max_length=6,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.name

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'サンプル'
        verbose_name_plural = 'サンプル'
