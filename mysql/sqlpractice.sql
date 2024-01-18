SELECT GROUP_CONCAT(' 'sites.domain_name) AS domains, clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id=sites.clients_id
GROUP BY clients.id