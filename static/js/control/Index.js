$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function sameOrigin(url) {
                // test that a given url is a same-origin URL
                // url could be relative or scheme relative or absolute
                var host = document.location.host, // host + port
                    protocol = document.location.protocol,
                    sr_origin = '//' + host,
                    origin = protocol + sr_origin;
                // Allow absolute or scheme relative URLs to same origin
                return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                        // or any other URL that isn't scheme relative or absolute i.e relative.
                    !(/^(\/\/|http:|https:).*/.test(url));
            }

            if (sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", $('meta[name="csrf-token"]').attr('content'));
            }
        }
    });

    function addIngr($el, name, count) {
        var $name, $count, $obj, $item;
        $item = $('<div>', {class: 'Ingredients-item'}).appendTo($el);
        $obj = $('<span>').html('Название').appendTo($item);
        $name = $('<select>', {class: 'name', value: name}).html(ingredients).appendTo($item);
        $name.children('option[value="' + name + '"]').attr('selected', 'selected');
        $obj = $('<span>').html('Количество').appendTo($item);
        $count = $('<input>', {class: 'count', value: count}).appendTo($item);
        $obj = $('<button>', {class: 'Ingredients-delete'}).html('Удалить').appendTo($item);
    }
    
    function saveDish($el, id) {
        var ingredients = [], data, url, id;

        $el.closest('.Dishes-item').find('.Ingredients-item').each(function () {
            if (!$(this).hasClass('Ingredients-add')) {
                var name = $(this).children('.name').val(),
                    count = $(this).children('.count').val();
                ingredients.push({
                    name: name,
                    count: count
                })
            }
        });

        data = {
            name: $el.closest('.Dishes-item').find('.Dishes-name').val(),
            ingredients: ingredients
        };

        url = '/control/api/dish/';
        id = $el.closest('.Dishes-item').data('id');
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
    }

    var ingredients = $('.Dishes-add .Ingredients-add .name').html();

    $('.Dishes-addButton, .save').click(function () {
        console.log('Add dish');

        saveDish($(this));
    });

    $('.Ingredients-addButton').click(function () {
        console.log('Add ingredient');

        var $ingrAdd, name, count;
        $ingrAdd = $(this).closest('.Ingredients-add');
        name = $ingrAdd.children('.name').val();
        count = $ingrAdd.children('.count').val();
        addIngr($(this).closest('.Ingredients'), name, count);
        //clear ingredients selected value and count value
        $(".Ingredients-item.Ingredients-add")[0].getElementsByClassName("name")[0].value = ""
        $(".Ingredients-item.Ingredients-add")[0].getElementsByClassName("count")[0].value = ""
    })

    $('.Ingredients-delete').click(function () {
        $(this).closest('.Ingredients-item').remove();
    });

    $('.Dishes-delete').click(function () {
        if (!confirm('Вы уверены?')) return false;
        $.ajax({
            url: '/control/api/dish/' + $(this).closest('.Dishes-item').children('.name').data('id') + '/',
            method: 'delete',
            complete: function () {
                window.location.reload();
            }
        });
    });
});