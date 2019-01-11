from django.core.management import call_command
from django.core.management.base import BaseCommand

from todo.models import Task


# Fixtureをインポート後、データの日付を現在に合わせて修正'
class Command(BaseCommand):

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        # データ削除
        Task.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('data cleared'))
        # fixtureをインポート
        call_command('loaddata', 'tasks.json')
        self.stdout.write(self.style.SUCCESS('data reloaded'))
