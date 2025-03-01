--  Navigate to http://localhost/phpmyadmin and create a database called "ims_pos" and run this command below

CREATE TABLE sales (
  sale_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  sale_value double(10,2) NOT NULL,
  order_id INT(11) NOT NULL
);

CREATE TABLE delivers (
  deliver_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  total double(10, 2) NOT NULL,
  customer_id INT(11) NOT NULL,
  order_id INT(11) NOT NULL,
  delivered DEFAULT TINYINT(0)
);

CREATE TABLE qrcode (
  qrcode_id INT(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  delivery_id INT(11) NOT NULL,
  qrpath VARCHAR(45) NOT NULL,
  qr_date timestamp NOT NULL DEFAULT current_timestamp()
);
