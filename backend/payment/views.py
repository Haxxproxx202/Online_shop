import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from django.conf import settings


# tworzę egzemplarz bramki płatności
gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    print('To jest order:', order)
    total_cost = order.get_total_cost()
    print('Tutaj jest total_cost:', total_cost)

    if request.method == "POST":
        # pobranie tokena nonce
        nonce = request.POST.get('payment_method_nonce', None)
        result = braintree.Transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:cancelled')

    else:
        client_token = braintree.ClientToken.generate()
        return render(request, 'payment/process.html', {'order': order, 'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')


def payment_cancelled(request):
    return render(request, 'payment/cancelled.html')
