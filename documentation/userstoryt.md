# Pizzapalvelu-sovelluksen käyttötapaukset

### Done

#### Täytteet
- Ylläpitäjänä voin selailla täytteitä
  ```
  SELECT * FROM topping
  ```

- Ylläpitäjänä voin lisätä täytteen
  ```
  INSERT INTO topping (date_created, date_modified, name) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?)
  ```

- Ylläpitäjänä voin muokata täytettä
  ```
  UPDATE topping 
  SET date_modified=CURRENT_TIMESTAMP, name=? 
  WHERE topping.id = ?
  ```

- ylläpitäjänä voin poistaa täytteen
  ```
  DELETE FROM topping 
  WHERE topping.id = ?
  ```

#### Pizzat
- asiakkaana/ylläpitäjänä voin selata pizzoja
  ```
  SELECT * FROM pizza

  SELECT * FROM topping, pizza_topping 
  WHERE ? = pizza_topping.pizza_id AND topping.id = pizza_topping.topping_id
  ```

- ylläpitäjänä voin lisätä pizzan valikoimaan
  ```
  INSERT INTO pizza (date_created, date_modified, name, price) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
  
  INSERT INTO pizza_topping (date_created, date_modified, pizza_id, topping_id) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
  ```

- ylläpitäjänä voin muokata pizzaa
  ```
  UPDATE pizza 
  SET date_modified=CURRENT_TIMESTAMP, name=?, price=? 
  WHERE pizza.id = ?
  
  INSERT INTO pizza_topping (date_created, date_modified, pizza_id, topping_id) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
  
  DELETE FROM pizza_topping WHERE pizza_topping.pizza_id = ? AND pizza_topping.topping_id = ?
  ```

- ylläpitäjänä voin poistaa pizzan
  ```
  DELETE FROM pizza_topping 
  WHERE pizza_topping.pizza_id = ? AND pizza_topping.topping_id = ?
  
  DELETE FROM pizza_topping 
  WHERE pizza_topping.id = ?
  
  DELETE FROM pizza 
  WHERE pizza.id = ?
  ```

#### Käyttäjät
- ylläpitäjänä voin selata käyttäjiä
  ```
  SELECT * FROM account
  ```

- ylläpitäjänä voin muokata käyttäjää
  ```
  UPDATE account 
  SET date_modified=CURRENT_TIMESTAMP, name=?, phone=?, address=? 
  WHERE account.id = ?
  ```

- ylläpitäjänä voin poistaa käyttäjän
  ```
  DELETE FROM account 
  WHERE account.id = ?
  ```


#### Tilaukset
- ylläpitäjänä voin selata tilauksia
  ```
  SELECT * FROM orders
  
  SELECT * FROM pizza, order_pizza 
  WHERE ? = order_pizza.order_id AND pizza.id = order_pizza.pizza_id
  
  SELECT * FROM account WHERE account.id = ?
  ```

- asiakkaana voin tehdä tilauksen
  ```
  INSERT INTO orders (date_created, date_modified, delivery, received, delivered, account_id) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
  
  INSERT INTO order_pizza (date_created, date_modified, order_id, pizza_id) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
  ```

- ylläpitäjänä voin muokata tilausta
  ```
  UPDATE orders 
  SET date_modified=CURRENT_TIMESTAMP, delivery=?, received=? 
  WHERE orders.id = ?
  ```

- ylläpitäjänä voin poistaa tilauksen
  ```
  DELETE FROM order_pizza 
  WHERE order_pizza.order_id = ? AND order_pizza.pizza_id = ?
  
  DELETE FROM order_pizza 
  WHERE order_pizza.id = ?
  
  DELETE FROM orders 
  WHERE orders.id = ?
  ```

#### Käyttäjätilit
- asiakkaana voin luoda käyttäjätilin palveluun
  ```
  INSERT INTO account (date_created, date_modified, name, phone, address, username, password, admin) 
  VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?, ?, ?)
  ```

- asiakkaana/ylläpitäjänä voin kirjautua sisään
  ```
  SELECT * FROM account 
  WHERE account.username = ? AND account.password = ? LIMIT ? OFFSET ?
  ```

- asiakkaana/ylläpitäjänä voin kirjautua ulos
  ```
  SELECT * FROM account 
  WHERE account.id = ?
  ```

- asiakkaana voin katsella tilitietojani sekä tilauksiani
  ```
  SELECT * FROM account 
  WHERE account.id = ?
  
  SELECT * FROM orders 
  WHERE orders.account_id = ?
  
  SELECT * FROM pizza, order_pizza 
  WHERE ? = order_pizza.order_id AND pizza.id = order_pizza.pizza_id
  ```

#### Muut
- kirjautunut ylläpitäjä / asiakas käyttäjärooleilla on eri oikeudet katsoa ja muokata sisältöä
  ```
  SELECT * FROM account 
  WHERE account.id = ?
  ```

- asiakkaana voin nähdä ananasta sisältäviä pizzoja etusivulla
  ```
  SELECT P.id, P.name, T.id, T.name 
  FROM pizza P, topping T, pizza_topping PT 
  WHERE P.id = PT.pizza_id AND T.id = PT.topping_id 
  GROUP BY P.id, T.id HAVING T.name = 'ananas' 
  LIMIT 5
  ```

- asiakkaana voin nähdä chiliä tai jalapenoa sisältäviä pizzoja etusivulla
  ```
  SELECT P.id, P.name, T.id, T.name 
  FROM pizza P, topping T, pizza_topping PT 
  WHERE P.id = PT.pizza_id AND T.id = PT.topping_id AND T.name IN ('chili', 'jalapeno') 
  GROUP BY P.id, T.id 
  LIMIT 5
  ```

- ylläpitäjänä voin nähdä top 3 asiakkaat tilausten yhteissumman ja tilausmäärän perusteella järjestettynä
  ```
  SELECT O.account_id, COUNT(P.id) as amount, SUM(P.price) as spend, A.name 
  FROM orders O 
  LEFT JOIN order_pizza OP ON O.id = OP.order_id 
  LEFT JOIN pizza P ON P.id = OP.pizza_id 
  LEFT JOIN account A ON A.id = O.account_id 
  GROUP BY O.account_id, A.name 
  ORDER BY spend DESC, amount 
  DESC LIMIT 3
  ```


### Backlog

- asiakkaana voin lisätä yhden tai useamman pizzan ostoskoriin
- asiakkaana voin katsella ostoskorin sisältöä
- asiakkaana voin tilata ostoskorin sisällön
