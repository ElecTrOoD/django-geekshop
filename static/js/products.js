window.onload = function () {
    $('.products-list').on('click', 'button[type="button"]', function () {
        let t_href = event.target;
        let path
        if (t_href.value === '0') {
            path = '/baskets/add/' + t_href.name + '/';
        } else {
            path = '/baskets/add/' + t_href.name + '/' + t_href.value + '/'
        }
        $.ajax({
            url: path,
            success: function (data) {
                $('.products-list').html(data.result);
            }
        });
        event.preventDefault();
    })
}