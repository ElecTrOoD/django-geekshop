window.onload = function () {
    let _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;

    let quantity_arr = [];
    let price_arr = [];

    let TOTAL_FORMS = parseInt($('input[name=orderitems-TOTAL_FORMS]').val());

    let order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    let order_total_cost = parseFloat($('.order_total_cost').text().replace(',', '.')) || 0;

    for (let i = 0; i < TOTAL_FORMS; i++) {
        _quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').text().replace(',', '.'));

        quantity_arr[i] = _quantity;
        if (_price) {
            price_arr[i] = _price;
        } else {
            price_arr[i] = 0;
        }
    }

    if (!order_total_quantity) {
        orderSummaryRecalc();
    }

    $('form[name=order_form]').on('click', 'input[type=number]', function () {
        let target = event.target;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''))
        orderitem_quantity = parseInt(target.value);
        delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
        quantity_arr[orderitem_num] = orderitem_quantity;

        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    });


    function orderSummaryRecalc() {
        order_total_quantity = 0
        order_total_cost = 0
        for (let i = 0; i < TOTAL_FORMS; i++) {
            order_total_quantity += quantity_arr[i]
            order_total_cost += quantity_arr[i] * price_arr[i]
        }
        $('.order_total_quantity').html(order_total_quantity.toString())
        $('.order_total_cost').html(order_total_cost.toFixed(2).replace('.', ','));
    }

    function orderSummaryUpdate(orderitem_price, delta_quantity) {
        delta_cost = orderitem_price * delta_quantity
        order_total_cost = Number((order_total_cost + delta_cost).toFixed(2));
        order_total_quantity = order_total_quantity + delta_quantity;
        $('.order_total_cost').html(order_total_cost.toFixed(2).replace('.', ','))
        $('.order_total_quantity').html(order_total_quantity);
    }

    $('tr[name=formset_row]').formset({
        addText: 'добавить товар',
        deleteText: 'удалить',
        prefix: 'orderitems',
        removed: deleteOrderItem
    });

    function deleteOrderItem(row) {
        let target_name = row[0].querySelector('input[type=number]').name;
        orderitem_num = target_name.replace('orderitems-', '').replace('-quantity', '');
        delta_quantity = -quantity_arr[orderitem_num];
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    }

    $('form[name=order_form]').on('change', 'select', function () {
        let target = event.target;
        let orderitem_product_pk = target.options[target.selectedIndex].value;
        orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-product', ''));

        $.ajax({
            url: '/orders/product/' + orderitem_product_pk + '/price/',
            success: function (data) {
                if (data.price) {
                    price_arr[orderitem_num] = parseFloat(data.price);
                    let price_html = '<span>' + data.price.toString().replace('.', ',') + '</span> руб.';
                    let curr_tr = $('.table').find('tr:eq(' + (orderitem_num + 1) + ')');
                    curr_tr.find('td:eq(2)').html(price_html);
                    curr_tr.find('td:eq(1)').find('input').attr('max', data.quantity);
                    orderSummaryRecalc();
                }
            }
        });
    });
}
