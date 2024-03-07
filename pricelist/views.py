# pricelist/views.py

from django.shortcuts import render, redirect
from .forms import PriceListUpdateForm
from .models import PriceList, PriceListUpdateHistory
from django.db.models import Max

def price_list(request):
    items = PriceList.objects.all()
    return render(request, 'pricelist/price_list.html', {'items': items})

def request_update_price_list(request):
    if request.method == 'POST':
        form = PriceListUpdateForm(request.POST)
        if form.is_valid():
            # フォームの内容を取得
            code = form.cleaned_data['code']
            product_name = form.cleaned_data['product_name']
            unit_price = form.cleaned_data['unit_price']

            # PriceListUpdateHistory モデルに保存
            PriceListUpdateHistory.objects.create(
                code=code,
                product_name=product_name,
                unit_price=unit_price
            )

            return redirect('request_update_price_list')   # 成功した場合のリダイレクト先を設定
    else:
        form = PriceListUpdateForm()

    return render(request, 'pricelist/request_update_price_list.html', {'form': form})

    
def update_history_list(request):
    history_list = PriceListUpdateHistory.objects.all()
    return render(request, 'pricelist/update_history_list.html', {'history_list': history_list})




def update_price_list(request):
    if request.method == 'POST':
        selected_code = request.POST.get('code', None)

        if selected_code:
            # 選択されたコードに対する最新の更新情報を取得
            try:
                latest_update_history = PriceListUpdateHistory.objects.filter(code=selected_code).latest('created_at')

                # 既存のレコードを取得
                price_list_record = PriceList.objects.filter(code=selected_code).first()

                if price_list_record is not None:
                    # 既存のレコードがある場合は更新
                    price_list_record.product_name = latest_update_history.product_name
                    price_list_record.unit_price = latest_update_history.unit_price
                    price_list_record.save()
                else:
                    # 新しいレコードを作成
                    PriceList.objects.create(
                        code=selected_code,
                        product_name=latest_update_history.product_name,
                        unit_price=latest_update_history.unit_price
                    )

            except PriceListUpdateHistory.DoesNotExist:
                # 選択されたコードに対する更新情報が存在しない場合の処理
                pass

    return render(request, 'pricelist/price_list.html')
