from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KNDssKJSpMHJ8z1eCo6Je88PG3bk3vjwJmUsawc0TgvsiSgx2Pt2heotogyzHVYiqK2At2cl32Da3VmZPWporJp00dy0tfGVA',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)