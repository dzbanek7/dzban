DROP TABLE IF EXISTS tbcustomers;
CREATE TABLE tbcustomers
(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    adress TEXT
);

DROP TABLE IF EXISTS tbsubscription;
CREATE TABLE tbsubscription
(
    subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    price_per_month INTEGER,
    subscription_length TEXT
);

DROP TABLE IF EXISTS tborder;
CREATE TABLE tborder
(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    subscription_id INTEGER,
    purchase_date DATE,
    FOREIGN KEY(customer_id) REFERENCES tbcustomer(customer_id),
    FOREIGN KEY(subscription_id) REFERENCES tbsubscription(subscription_id)
);


