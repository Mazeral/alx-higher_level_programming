-- a script that lists all shows contained in hbtn_0d_tvshows without a genre linked. 
SELECT tv_shows.title, tv_shows_genres.genre_id
	FROM tv_shows
	LEFT JOIN tv_shows_genres
	ON tv_shows.id = tv_shows_genres.show_id
	WHERE tv_shows_genres.genre_id IS NULL
