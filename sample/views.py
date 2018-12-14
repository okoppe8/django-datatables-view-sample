from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from excel_response import ExcelMixin

from .models import Item


# DataTablesにデータを提供するWebAPI
# django-datatables-view
# https://pypi.org/project/django-datatables-view/
class ItemsJsonView(BaseDatatableView):
    # モデルの指定
    model = Item
    # フィールドの指定
    columns = ['id', 'pref_name', 'name', 'furigana', 'zipcode', 'address', 'tel', 'code']

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS


# 印刷・Excel・CSV出力の基底クラス
class BaseReportView(generic.ListView):
    model = Item

    # 選択データの取得
    def get_queryset(self):
        id_list = self.request.GET['id_list'].split('_')
        result = Item.objects.filter(id__in=id_list)
        return result


# 印刷画面表示
class PrintView(BaseReportView):
    template_name = 'sample/print.html'


# Excelダウンロード
# django-excel-response
# https://pypi.org/project/django-excel-response/
class ExcelView(ExcelMixin, BaseReportView):

    # 見出し行を日本語にする
    def get_queryset(self):
        header = [['id', '県名', '市町村名', 'ふりがな', '郵便番号', '住所', '電話番号', '自治体コード']]
        body = [list(entry.values()) for entry in super().get_queryset().values()]
        return header + body


# CSVダウンロード
class CsvView(ExcelView):
    force_csv = True
