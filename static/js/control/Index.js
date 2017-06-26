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

    var ingredients = $('.Dishes-add .Ingredients-add .name').html();

    $('.Dishes-addButton').click(function () {
        console.log('Add dish');

        var ingredients = [], data;

        $('.Dishes-add .Ingredients-item').each(function () {
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
            name: $('.Dishes-add .Dishes-name').val(),
            ingredients: ingredients
        };

        $.post({
            url: '/control/api/dish/',
            data: JSON.stringify(data),
            complete: function () {
                window.location.reload();
            }
        });
    });

    $('.Ingredients-addButton').click(function () {
        console.log('Add ingredient');

        var $ingrAdd, name, count;
        $ingrAdd = $(this).closest('.Ingredients-add');
        name = $ingrAdd.children('.name').val();
        count = $ingrAdd.children('.count').val();
        addIngr($(this).closest('.Ingredients'), name, count);
    })

    $('.Ingredients-delete').click(function () {
        $(this).closest('.Ingredients-item').remove();
    });

    $('.Dishes-delete').click(function () {
        $.ajax({
            url: '/control/api/dish/' + $(this).closest('.Dishes-item').children('.name').data('id') + '/',
            method: 'delete',
            complete: function () {
                window.location.reload();
            }
        });
    });
});