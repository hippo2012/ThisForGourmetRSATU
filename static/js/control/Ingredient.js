$(document).ready(function () {
    $('.Ingredients-addButton, .save').click(function () {
        var data, url, id;

        data = {
            name: $(this).closest('.Ingredients-item').find('.name').val(),
        };

        url = '/control/api/ingredient/';
        id = $(this).closest('.Ingredients-item').data('id');
        if (id && id != '') {
            url += id + '/';
        }

        $.post({
            url: url,
            data: JSON.stringify(data),
            complete: function () {
                window.location.reload();
            }
        });
    });

    $('.delete').click(function() {
        if (!confirm('Вы уверены?')) return false;
        $.ajax({
            url: '/control/api/ingredient/' + $(this).closest('.Ingredients-item').data('id') + '/',
            method: 'delete',
            complete: function () {
                window.location.reload();
            }
        });
    })
});