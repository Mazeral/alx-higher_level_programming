-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_generes.name AS 'genre'
	COUNT(tv_show_generes.show_id) AS 'number_of_shows'
	FROM genres
	INNER JOIN tv_show_generes ON genres.genre_id = tv_show_generes.genre_id
	GROUP BY genres.name
	ORDER BY number_of_shows DESC
