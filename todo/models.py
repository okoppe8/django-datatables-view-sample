from django.db import models


# Create your models here.
class Task(models.Model):
    # タイトル
    title = models.CharField(
        verbose_name='タイトル',
        max_length=100,
    )

    # 詳細
    detail = models.TextField(
        verbose_name='詳細',
        blank=True,
        null=True,
        max_length=1000,
    )

    # ステータス値
    # status_choice = (
    #     (0, '未着手'),
    #     (1, '対応中'),
    #     (2, '完了'),
    # )

    # ステータス
    status = models.IntegerField(
        verbose_name='ステータス',
        # choices=status_choice,
        default=0,
    )

    # 論理削除フラグ
    is_deleted = models.BooleanField(
        verbose_name='削除済み',
        default=False,
    )

    created_at = models.DateTimeField(
        verbose_name='登録時間',
        blank=True,
        null=True,
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        verbose_name='登録時間',
        blank=True,
        null=True,
        auto_now=True,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.title

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'ToDoタスク'
        verbose_name_plural = 'ToDoタスク'
