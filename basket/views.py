from django.shortcuts import (
    render, redirect, reverse,
        HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_basket(request):
    """ A view that renders the basket's contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if quantity:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    messages.success(request, f'Added {product.name} to your basket')
    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjusts the quantity of a product to a new amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.name}\
                quantity to {basket[item_id]}')
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name}\
                from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping basket"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        quantity = None
        if 'product_quantity' in request.POST:
            quantity = request.POST['product_quantity']
        basket = request.session.get('basket', {})

        if quantity:
            del basket[item_id]['items_by_quantity'][quantity]
            if not basket[item_id]['items_by_quantity']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name}\
                from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
