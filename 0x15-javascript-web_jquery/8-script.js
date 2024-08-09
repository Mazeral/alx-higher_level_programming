$(document).ready(function () {
/* gets the data from the original link */
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(element => {
      /* look for the title in each film's link */
      $.getJSON(element.url, function (data) {
        const FilmName = data.title;
        $('UL#list_movies').append(`<li>${FilmName}</li>`);
      });
    });
  });
});
