CREATE TABLE inventory(
    storeID INT NOT NULL,
    externalID INT NOT NULL,
    typeID INT NOT NULL,
    price DECIMAL(10,2),
    quantity INT,
    lastUpdated DATETIME,
    
    PRIMARY KEY (storeID, externalID),
    FOREIGN KEY (storeID) REFERENCES store(storeID),
    FOREIGN KEY (typeID) REFERENCES productType(typeID)
);