# Tietokantarakenteen kuvaus

### Tietokantakaavio

![Tietokantakaavio](https://github.com/juissijohtaja/Pizzapalvelu/blob/master/documentation/Pizzapalvelu-dbdiagram.png)

### CREATE TABLE -lauseet

#### User
CREATE TABLE account (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        phone INTEGER NOT NULL, 
        address VARCHAR(144) NOT NULL, 
        username VARCHAR(144) NOT NULL, 
        password VARCHAR(144) NOT NULL, 
        admin BOOLEAN, 
        PRIMARY KEY (id), 
        CHECK (admin IN (0, 1))
);

#### Order
CREATE TABLE orders (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        delivery VARCHAR(144) NOT NULL, 
        oregano BOOLEAN, 
        garlic BOOLEAN, 
        received BOOLEAN, 
        delivered BOOLEAN, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        CHECK (oregano IN (0, 1)), 
        CHECK (garlic IN (0, 1)), 
        CHECK (received IN (0, 1)), 
        CHECK (delivered IN (0, 1)), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);

#### OrderPizza
CREATE TABLE order_pizza (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        order_id INTEGER NOT NULL, 
        pizza_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(order_id) REFERENCES orders (id), 
        FOREIGN KEY(pizza_id) REFERENCES pizza (id)
);

#### Pizza
CREATE TABLE pizza (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        price INTEGER NOT NULL, 
        PRIMARY KEY (id)
);

#### PizzaTopping
CREATE TABLE pizza_topping (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        pizza_id INTEGER NOT NULL, 
        topping_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(pizza_id) REFERENCES pizza (id), 
        FOREIGN KEY(topping_id) REFERENCES topping (id)
);

#### Topping
CREATE TABLE topping (
        id INTEGER NOT NULL, 
        date_created DATETIME, 
        date_modified DATETIME, 
        name VARCHAR(144) NOT NULL, 
        PRIMARY KEY (id)
);

