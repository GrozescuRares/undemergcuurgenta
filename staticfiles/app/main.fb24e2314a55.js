$( document ).ready(function() {
  $('#clear_filters').on('click', function (event) {
    event.preventDefault();

    $('#id_tags__contains').val('');
    $("#id_category").val($("#target option:first").val());
    $("#id_location").val($("#target option:first").val());
  });

  let btn = $('#backToTop');

  $(window).scroll(function() {
    if ($(window).scrollTop() > 300) {
      btn.addClass('show');
    } else {
      btn.removeClass('show');
    }
  });

  btn.on('click', function(event) {
    event.preventDefault();

    $('html, body').animate({scrollTop:0}, '300');
  });

  $('#backToPrevious').on('click', function (event) {
    event.preventDefault();

    window.location.href = this.data('previous');
  })
});

$(window).on('load',function(){
  if($('#exampleModal').length) {
    $('#exampleModal').modal('show');
  }
});


