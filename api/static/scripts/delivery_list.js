console.log("delivery script");

const url = "http://127.0.0.1:5000/api";

const getOrderById = async (id) => {
  const req = await fetch(`${url}/order/${id}`);
  const order = await req.json();

  return order;
};

const getProductById = async (id) => {
  const req = await fetch(`${url}/products/${id}`);
  const product = await req.json();

  return product;
};

const getCustomerById = async (id) => {
  const req = await fetch(`${url}/user/${id}`);
  const customer = await req.json();

  return customer;
};

const getDeliveries = async () => {
  const req = await fetch(`${url}/delivery`);
  const deliveries = await req.json();

  console.log(deliveries);

  displayDeliveries(deliveries);
};

getDeliveries();

const displayDeliveries = async (deliveries) => {
  const container = document.getElementsByClassName("container")[0];

  // "customer_id": 1,
  // "deliver_id": 54,
  // "delivered": 0,
  // "order_id": 89,
  // "total": 7500.0

  for (const delivery of deliveries) {
    const { customer_id, deliver_id, delivered, order_id, total } = delivery;

    const order = await getOrderById(order_id);
    console.log(order);

    const { order_date, product_id, total_shipped } = order;

    const user = await getCustomerById(parseInt(customer_id));

    // console.log(customer_id, deliver_id, delivered, order_id, total);
  }
};

// let deliveries = getDeliveries().then((data) => data);
