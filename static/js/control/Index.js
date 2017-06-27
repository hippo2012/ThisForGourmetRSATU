$(document).ready(function () {
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
            name: $el.closest('.Dishes-item').find('.name').val(),
            price: $el.closest('.Dishes-item').find('.price').val(),
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

        var $ingrAdd, name, count, $add;
        $ingrAdd = $(this).closest('.Ingredients-add');
        name = $ingrAdd.children('.name').val();
        count = $ingrAdd.children('.count').val();
        addIngr($(this).closest('.Ingredients'), name, count);
        //clear ingredients selected value and count value
        $add = $(this).closest('.Ingredients-add');
        $add.children('.name').val('');
        $add.children('.count').val('');
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