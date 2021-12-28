from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm
from basket.contexts import basket_contents


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))
    
    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkouts/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KBc3HGvmejGyxf3DkIMPk7rZCLYujJsDKhhzOdzYZYwmKzzhJ3FTBbO1ieI7mjiDRlff70cWy4QlyMZbqrODL0100BMZYqbMF',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
