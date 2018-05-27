// ===== Scroll to Top ====
$('body,html').scroll(function() {
    if ($(this).scrollTop() >= 300) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
        $('#return-to-top').show();    // Fade in the arrow
        $('#logo').show();

    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
        $('#return-to-top').hide();   // Else fade out the arrow
        $('#logo').hide();
    }
});


$('#return-to-top').click(function() {      // When arrow is clicked
    $('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
});



$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});

$(function(){
$('.carousel').carousel({
      interval: 3000
    });
$('.carousel-control.right').trigger('click');
});



// $('#add-to-card').click(function() {
//   alert("DOne");
// });

$(document).ready(function(){
  $(".add-to-card").click(function(){
      var product_id = $(this).data("product_id");
      var product_name = $(this).data("product_name");
      // alert(product_name);
      var product_price = $(this).data("product_price");
      var data = {};
      var url = '{% url orders:add_to_cart %}';
      data.product_id = product_id;
      console.log(data);
      console.log(url);

      // $.ajax({
      //        type: "GET",
      //        url: url,
      //        data: data,
      //       //  dataType: "html",
      //        cache: false,
      //        success: function(data){
      //            console.log("ok");
      //        },
      //          error: function(){
      //            console.log("error");
      //          }
      //   });

      //
      // $.ajax({
      //   type: "GET";
      //   url: url;
      //   data: data;
      //   cache: false;
      //   success: function(data){
      //     console.log("ok");
      //   },
      //   error: function(){
      //     console.log("error");
      //   }
      //
      // });

      $('#card ul').append('<li>'+ product_name +'<a href="" style="display:inline;" class="right"><span class="delete-item glyphicon glyphicon-trash"> </span></a></li>');
      
      // $('ul.nav li.dropdown').find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
  });
});

$(document).on('click', '.delete-item', function(e){
  e.preventDefault();
  $(this).closest('li').remove();
});
