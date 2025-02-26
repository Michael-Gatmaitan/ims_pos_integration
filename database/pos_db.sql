CREATE TABLE sales (
  sale_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  sale_value double(10,2) NOT NULL,
  order_id INT(11) NOT NULL
);

CREATE TABLE delivers (
  deliver_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  total double(10, 2) NOT NULL,
  customer_id INT(11) NOT NULL,
  delivered DEFAULT TINYINT(0)
);
