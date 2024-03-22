# pricelist/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import PriceListUpdateForm
from .models import PriceList, PriceListUpdateHistory
from django.db.models import Max, Subquery, OuterRef
from django.http import JsonResponse, HttpResponseNotAllowed

def price_list(request):
    items = PriceList.objects.all()
    return render(request, 'pricelist/price_list.html', {'items': items})

def request_update_price_list(request):
    if request.method == 'POST':
        form = PriceListUpdateForm(request.POST)
        if form.is_valid():
            # フォームのデータを取得
            code = form.cleaned_data['code']
            branch = form.cleaned_data['branch']
            product_name = form.cleaned_data['product_name']
            unit_price = form.cleaned_data['unit_price']
            apply_unit_price = form.cleaned_data['apply_unit_price']
            delivery_lot = form.cleaned_data['delivery_lot']
            pre_order_lot = form.cleaned_data['pre_order_lot']
            unit = form.cleaned_data['unit']
            packaging_style = form.cleaned_data['packaging_style']
            supplier_code = form.cleaned_data['supplier_code']
            supplier = form.cleaned_data['supplier']
            delivery_code = form.cleaned_data['delivery_code']
            delivery_location = form.cleaned_data['delivery_location']
            applicable_location = form.cleaned_data['applicable_location']
            note = form.cleaned_data['note']

            # PriceListUpdateHistory モデルに保存
            PriceListUpdateHistory.objects.create(
                code=code,
                branch=branch,
                product_name=product_name,
                unit_price=unit_price,
                apply_unit_price=apply_unit_price,
                delivery_lot=delivery_lot,
                pre_order_lot=pre_order_lot,
                unit=unit,
                packaging_style=packaging_style,
                supplier_code=supplier_code,
                supplier=supplier,
                delivery_code=delivery_code,
                delivery_location=delivery_location,
                applicable_location=applicable_location,
                note=note
            )
            
            # リダイレクト先を設定
            return redirect('request_update_price_list')
    else:
        form = PriceListUpdateForm()

    return render(request, 'pricelist/request_update_price_list.html', {'form': form})




    
def update_history_list(request):
    if request.method == 'POST':  
        history_list = PriceListUpdateHistory.objects.all()
        return render(request, 'pricelist/update_history_list.html', {'history_list': history_list})
    elif request.method == 'GET':
        history_list = PriceListUpdateHistory.objects.all()
        return render(request, 'pricelist/update_history_list.html', {'history_list': history_list})
    else:
        return HttpResponseNotAllowed(['GET'])




def update_price_list(request):
    if request.method == 'POST':  
        id = request.POST.get('id')
        
        # IDに基づいてPriceListUpdateHistoryオブジェクトを取得
        history_record = get_object_or_404(PriceListUpdateHistory, id=id)

        try:
            # PriceListを取得する
            pricelist_record = PriceList.objects.get(code=history_record.code, branch=history_record.branch)
            # レコードが存在する場合は更新
            pricelist_record.product_name = history_record.product_name
            pricelist_record.unit_price = history_record.unit_price
            pricelist_record.apply_unit_price = history_record.apply_unit_price
            pricelist_record.delivery_lot = history_record.delivery_lot
            pricelist_record.pre_order_lot = history_record.pre_order_lot
            pricelist_record.unit = history_record.unit
            pricelist_record.packaging_style = history_record.packaging_style
            pricelist_record.supplier_code = history_record.supplier_code
            pricelist_record.supplier = history_record.supplier
            pricelist_record.delivery_code = history_record.delivery_code
            pricelist_record.delivery_location = history_record.delivery_location
            pricelist_record.applicable_location = history_record.applicable_location
            pricelist_record.note = history_record.note
            pricelist_record.save()

            return HttpResponse("Price List Record Updated Successfully!")

        except PriceList.DoesNotExist:
            # レコードが存在しない場合は新規追加
            PriceList.objects.create(
                code=history_record.code,
                branch=history_record.branch,
                product_name=history_record.product_name,
                unit_price=history_record.unit_price,
                apply_unit_price=history_record.apply_unit_price,
                delivery_lot=history_record.delivery_lot,
                pre_order_lot=history_record.pre_order_lot,
                unit=history_record.unit,
                packaging_style=history_record.packaging_style,
                supplier_code=history_record.supplier_code,
                supplier=history_record.supplier,
                delivery_code=history_record.delivery_code,
                delivery_location=history_record.delivery_location,
                applicable_location=history_record.applicable_location,
                note=history_record.note
            )

            return HttpResponse("New Price List Record Created Successfully!")

    else:
        return HttpResponseNotAllowed(['POST'])


def get_default_values(request):
    code = request.GET.get('code')
    branch = request.GET.get('branch')
    
    try:
        pricelist_record = PriceList.objects.get(code=code, branch=branch)
        data = {
            'code': pricelist_record.code,
            'branch': pricelist_record.branch,
            'product_name': pricelist_record.product_name,
            'unit_price': pricelist_record.unit_price,
            'apply_unit_price': pricelist_record.apply_unit_price,
            'delivery_lot': pricelist_record.delivery_lot,
            'pre_order_lot': pricelist_record.pre_order_lot,
            'unit': pricelist_record.unit,
            'packaging_style': pricelist_record.packaging_style,
            'supplier_code': pricelist_record.supplier_code,
            'supplier': pricelist_record.supplier,
            'delivery_code': pricelist_record.delivery_code,
            'delivery_location': pricelist_record.delivery_location,
            'applicable_location': pricelist_record.applicable_location,
            'note': pricelist_record.note,
            'created_at': pricelist_record.created_at,
        }
        return JsonResponse(data)
    except PriceList.DoesNotExist:
        return JsonResponse({'error': 'Code not found'}, status=404)

from django.shortcuts import render
from .models import PriceList

def detail_view(request, id):
    pricelist_update_history = get_object_or_404(PriceListUpdateHistory, id=id)
    context = {
        'pricelist_update_history': pricelist_update_history,
    }
    return render(request, 'pricelist/detail.html', context)


