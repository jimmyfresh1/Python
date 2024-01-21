SELECT users.first_name AS reference_name, users2.first_name AS friend_name 
FROM users  
LEFT JOIN friendships
ON users.id= friendships.user_id 
LEFT JOIN users AS users2
ON users2.id= friendships.friend_id 
WHERE users.id=7;
