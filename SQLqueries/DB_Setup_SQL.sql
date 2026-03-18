CREATE DATABASE drop_alert;
USE drop_alert;

CREATE TABLE store(
	storeID INT PRIMARY KEY AUTO_INCREMENT,
    storeName VARCHAR(60) NOT NULL
);

CREATE TABLE productType(
	typeID INT PRIMARY KEY AUTO_INCREMENT,
    typeName VARCHAR(80) NOT NULL
);


CREATE TABLE product(
	productID INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(80) NOT NULL,
    typeID INT NOT NULL,
    
    FOREIGN KEY (typeID) REFERENCES productType(typeID)
);


CREATE TABLE inventory(
	storeID INT NOT NULL,
    productID INT NOT NULL,
    externalID INT NOT NULL,
    price DECIMAL(10,2),
    quantity INT,
    
    PRIMARY KEY (storeID, productID),
    FOREIGN KEY (storeID) REFERENCES store(storeID),
    FOREIGN KEY (productID) REFERENCES product(productID)
);
