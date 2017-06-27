$(document).ready(function () {
   $('.Dishes-order').click(function() {
       var id = $(this).closest('.Dishes-item').data('id'),
           url = '/api/dish_order/' + id + '/',
           data = {
               order: false
           };;
       $.post({
            url: url,
            data: JSON.stringify(data)
        });
   });
});