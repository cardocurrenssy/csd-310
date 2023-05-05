use bacchus_winery;

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2022-12-14', (SELECT productsID FROM bacchusproducts WHERE productname = 'merlot'), '12020', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Repub Distributing'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2022-12-18', (SELECT productsID FROM bacchusproducts WHERE productname = 'merlot'), '10899', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Sir Mixalot Co.'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2022-12-28', (SELECT productsID FROM bacchusproducts WHERE productname = 'merlot'), '5499', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Southern Hospitality'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2022-12-29', (SELECT productsID FROM bacchusproducts WHERE productname = 'merlot'), '10899', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Allied Spirits'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-01-10', (SELECT productsID FROM bacchusproducts WHERE productname = 'merlot'), '7499', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Repub Distributing'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-01-17', (SELECT productsID FROM bacchusproducts WHERE productname = 'merlot'), '10899', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Synergy Fine Wines'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-02-05', (SELECT productsID FROM bacchusproducts WHERE productname = 'merlot'), '15499', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Tip It Back Distributors'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-02-15', (SELECT productsID FROM bacchusproducts WHERE productname = 'cabernet sauvignon'), '12799', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Allied Spirits'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-01-10', (SELECT productsID FROM bacchusproducts WHERE productname = 'chablis'), '8499', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Repub Distributing'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-01-17', (SELECT productsID FROM bacchusproducts WHERE productname = 'chardonnay'), '11899', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Synergy Fine Wines'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-02-05', (SELECT productsID FROM bacchusproducts WHERE productname = 'chardonnay'), '14200', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Tip It Back Distributors'));

INSERT INTO `distributorsorders`(order_date, productsID,totalCost,distributorsID)
VALUES('2023-02-15', (SELECT productsID FROM bacchusproducts WHERE productname = 'cabernet sauvignon'), '12799', (SELECT distributorsID FROM distributors WHERE distributorsname = 'Sir Mixalot Co.'));
