# pricelist/views.py

from django.shortcuts import render, redirect
from .forms import PriceListUpdateForm
from .models import PriceList, PriceListUpdateHistory

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

from django.db.models import Max, F
from django.shortcuts import render
from .models import PriceList, PriceListUpdateHistory

def update_price_list(request):
    if request.method == 'POST':
        # 各Codeごとに最新の更新履歴を取得
        latest_update_history_per_code = PriceListUpdateHistory.objects.values('code').annotate(
            max_created_at=Max('created_at')
        )

        for update_history in latest_update_history_per_code:
            code = update_history['code']
            max_created_at = update_history['max_created_at']

            # 対応するPriceListレコードが存在するか確認
            try:
                latest_update_history = PriceListUpdateHistory.objects.get(code=code, created_at=max_created_at)
                price_list_record = PriceList.objects.get(code=code)
                
                # 存在する場合は更新
                price_list_record.product_name = latest_update_history.product_name
                price_list_record.unit_price = latest_update_history.unit_price
                price_list_record.save()

            except (PriceList.DoesNotExist, PriceListUpdateHistory.DoesNotExist):
                # 存在しない場合は新しいレコードを作成
                PriceList.objects.create(
                    code=code,
                    product_name=latest_update_history.product_name,
                    unit_price=latest_update_history.unit_price
                )

    return render(request, 'pricelist/price_list.html')
