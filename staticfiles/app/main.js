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

    window.location.href = $(this).data('previous');
  });

  let backButton = document.querySelector('.back-button')

  function backAnim() {
    if (backButton.classList.contains('back')) {
      backButton.classList.remove('back');
    } else {
      backButton.classList.add('back');
      setTimeout(backAnim, 1000);
    }
  }

  backButton.addEventListener('click', backAnim);
});

$(window).on('load',function(){
  if($('#exampleModal').length) {
    $('#exampleModal').modal('show');
  }
});


