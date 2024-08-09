$(document).ready(function () {
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  console.log(data);
  data.films.forEach(element => {
    $.get(element, function (data) {
      const film_name = data.name;
      $('UL#list_movies').append(`<li>${film_name}</li>`);
    });
  });
})});
