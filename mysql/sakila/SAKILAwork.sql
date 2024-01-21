SELECT film.title, film.synopsis, film.release_year, film.rating, film.special_features, actor.first_name, actor.last_name, category.name AS genre
FROM film
join film_category ON film_category.film_id = film.film_id
join category ON category.category_id = film_category.category_id
join film_actor ON film_actor.film_id = film.film_id 
join actor on actor.actor_id = film_actor.actor_id
WHERE category.name='Action'
AND actor.first_name='SANDRA'
AND actor.last_name = 'Kilmer'