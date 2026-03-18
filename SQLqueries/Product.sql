INSERT INTO Product(name, typeID) VALUES
("151", 1),
("151", 2),
("151", 3),
("151", 4),
("151", 5),
("151", 6),
("151", 7),
("151", 8),
("151", 9)
;

#Subquery to insert a product and ALL available productTypes at one go
#Just select the set-name and send the query
INSERT INTO product (name, typeID)
SELECT "Perfect Order", typeID FROM productType;
