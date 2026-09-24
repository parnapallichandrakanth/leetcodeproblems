SELECT C.name as customers FROM 
Customers C LEFT JOIN Orders O
ON C.id=O.customerId
WHERE O.ID is NULL;
