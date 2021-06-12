window.onload = function () {
    $('.products-list').on('click', 'button[type="button"]', function () {
        let t_href = event.target;
        $.ajax({
            url: '/baskets/add/' + t_href.name,
            success: function (data) {
                $('.products-list').html(data.result);
            }
        });
        event.preventDefault();
    })
}