$(document).ready(function () {
  $('#toggle_header').on('click', function () {
    if ($('#toggle_header').hasClass('red')) {
      $('#toggle_header').removeClass('red');
      $('#toggle_header').addClass('green');
    } else if ($('#toggle_header').hasClass('green')) {
      $('#toggle_header').removeClass('green');
      $('#toggle_header').addClass('red');
    } else if ($('#toggle_header').hasClass('red') === false && $('#toggle_header').hasClass('green') === false) {
      $('#toggle_header').addClass('red');
    }
  });
});
