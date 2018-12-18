from django.db import models


# Create your models here.
class Item(models.Model):
    # 県名
    pref_name = models.CharField(
        verbose_name='県名',
        max_length=4,
    )

    # 市町村名
    name = models.CharField(
        verbose_name='市町村名',
        max_length=15,
    )

    # ふりがな
    furigana = models.CharField(
        verbose_name='ふりがな',
        max_length=30,
    )

    # 郵便番号
    zipcode = models.CharField(
        verbose_name='郵便番号',
        max_length=8,
    )

    # 住所
    address = models.CharField(
        verbose_name='住所',
        max_length=100,
    )

    # 電話番号
    tel = models.CharField(
        verbose_name='電話番号',
        max_length=13,
    )

    # 自治体コード
    code = models.CharField(
        verbose_name='自治体コード',
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
        verbose_name = '自治体データ'
        verbose_name_plural = '自治体データ'
