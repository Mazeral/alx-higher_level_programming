$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    json_data = data;
    $('DIV#character').text(json_data.name);
    console.log(json_data);
  });
});
