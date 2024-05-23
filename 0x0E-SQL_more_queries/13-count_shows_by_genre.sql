-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_generes.name AS ('genre')
	COUNT (*) AS ('number_of_shows')
	INNER JOIN tv_show_generes ON genres.genre_id = tv_show_generes.genre_id
	GROUP BY tv_show_generes.name
