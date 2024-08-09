# 0x15. JavaScript - Web jQuery

This directory contains tasks related to JavaScript and jQuery, focusing on manipulating HTML elements, making HTTP requests, and handling events using both vanilla JavaScript and the jQuery library.

## Table of Contents

- [0. No JQuery](#0-no-jquery)
- [1. With JQuery](#1-with-jquery)
- [2. Click and turn red](#2-click-and-turn-red)
- [3. Add `.red` class](#3-add-red-class)
- [4. Toggle classes](#4-toggle-classes)
- [5. List of elements](#5-list-of-elements)
- [6. Change the text](#6-change-the-text)
- [7. Star Wars character](#7-star-wars-character)
- [8. Star Wars movies](#8-star-wars-movies)
- [9. Say Hello!](#9-say-hello)

## 0. No JQuery

**Task**: Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- Use `document.querySelector` to select the `<header>` tag.
- Do not use the jQuery API.

**File**: `0-script.js`

```javascript
document.querySelector('header').style.color = '#FF0000';
```

**Test**: Open `0-main.html` in your browser to verify the script works as expected.

## 1. With JQuery

**Task**: Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):

- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `1-script.js`

```javascript
$('header').css('color', '#FF0000');
```

**Test**: Open `1-main.html` in your browser to verify the script works as expected.

## 2. Click and turn red

**Task**: Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `2-script.js`

```javascript
$('#red_header').click(function() {
    $('header').css('color', '#FF0000');
});
```

**Test**: Open `2-main.html` in your browser and click on the `DIV#red_header` to verify the script works as expected.

## 3. Add `.red` class

**Task**: Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`:

- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `3-script.js`

```javascript
$('#red_header').click(function() {
    $('header').addClass('red');
});
```

**Test**: Open `3-main.html` in your browser and click on the `DIV#red_header` to verify the script works as expected.

## 4. Toggle classes

**Task**: Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:

- The `<header>` element must always have one class: `red` or `green`, never both at the same time, and never empty.
- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `4-script.js`

```javascript
$('#toggle_header').click(function() {
    $('header').toggleClass('red green');
});
```

**Test**: Open `4-main.html` in your browser and click on the `DIV#toggle_header` to verify the script works as expected.

## 5. List of elements

**Task**: Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:

- The new element must be: `<li>Item</li>`.
- The new element must be added to `UL.my_list`.
- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `5-script.js`

```javascript
$('#add_item').click(function() {
    $('.my_list').append('<li>Item</li>');
});
```

**Test**: Open `5-main.html` in your browser and click on the `DIV#add_item` to verify the script works as expected.

## 6. Change the text

**Task**: Write a JavaScript script that updates the text of the `<header>` element to "New Header!!!" when the user clicks on `DIV#update_header`:

- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `6-script.js`

```javascript
$('#update_header').click(function() {
    $('header').text('New Header!!!');
});
```

**Test**: Open `6-main.html` in your browser and click on the `DIV#update_header` to verify the script works as expected.

## 7. Star Wars character

**Task**: Write a JavaScript script that fetches the character name from this [URL](https://swapi-api.alx-tools.com/api/people/5/?format=json):

- The name must be displayed in the HTML tag `DIV#character`.
- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `7-script.js`

```javascript
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    $('#character').text(data.name);
});
```

**Test**: Open `7-main.html` in your browser to verify the script works as expected.

## 8. Star Wars movies

**Task**: Write a JavaScript script that fetches and lists the titles for all movies from this [URL](https://swapi-api.alx-tools.com/api/films/?format=json):

- All movie titles must be listed in the HTML tag `UL#list_movies`.
- Use the jQuery API.
- Do not use `document.querySelector`.

**File**: `8-script.js`

```javascript
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    data.results.forEach(function(movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
    });
});
```

**Test**: Open `8-main.html` in your browser to verify the script works as expected.

## 9. Say Hello!

**Task**: Write a JavaScript script that fetches a translation of “hello” from [this URL](https://hellosalut.stefanbohacek.dev/?lang=fr) and displays it in the HTML tag `DIV#hello`:

- Use the jQuery API.
- Do not use `document.querySelector`.
- Your script must work when it is imported from the `<head>` tag.

**File**: `9-script.js`

```javascript
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('#hello').text(data.hello);
});
```

**Test**: Open `9-main.html` in your browser to verify the script works as expected.

## Author

Mohammad Omar Siddiq
```

This `README.md` file provides a summary of each task, the corresponding file, and a sample script to accomplish the task. You can use this as a guide while working on the tasks in the specified repository and directory.
