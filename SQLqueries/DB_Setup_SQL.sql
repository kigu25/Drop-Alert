CREATE DATABASE drop_alert;
USE drop_alert;

CREATE TABLE store(
	storeID INT PRIMARY KEY AUTO_INCREMENT,
    storeName VARCHAR(60)
);

CREATE TABLE productType(
	typeID INT PRIMARY KEY AUTO_INCREMENT,
    typeName VARCHAR(80)
);


CREATE TABLE product(
	productID int PRIMARY KEY AUTO_INCREMENT,
    externalID int NOT NULL,
    name VARCHAR(80),
    typeID int NOT NULL,
    
    FOREIGN KEY(typeID) REFERENCES ProductType(typeID)
);


CREATE TABLE inventory(
	storeID INT NOT NULL,
	productID INT NOT NULL,
    price DECIMAL(10,2),
    quantity INT,
    
    PRIMARY KEY(storeID, productID),
    FOREIGN KEY(storeID) REFERENCES store(storeID),
    FOREIGN KEY(productID) REFERENCES product(productID)
);