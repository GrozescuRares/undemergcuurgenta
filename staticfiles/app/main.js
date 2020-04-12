$( document ).ready(function() {
  $('#clear_filters').on('click', function (event) {
    event.preventDefault();

    console.log('aici')

    $('#tags__contains').val('');
    $("#id_category").val($("#target option:first").val());
    $("#id_location").val($("#target option:first").val());
  });
});