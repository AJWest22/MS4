from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_basket(request):
    """ A view that renders the basket's contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if quantity:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Adjusts the quantity of a product to a new amount"""

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity:
        if quantity > 0:
            basket[item_id] = quantity
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the shopping bag"""

    try:
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

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
