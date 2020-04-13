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
});

$(window).on('load',function(){
  if($('#exampleModal').length) {
    $('#exampleModal').modal('show');
  }
});

(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Get the forms we want to add validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();
