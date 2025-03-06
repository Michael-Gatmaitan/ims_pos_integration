console.log("delivery script");

// const url = "http://127.0.0.1:5000/api";
const url = "http://192.168.100.9:5000/api";
// const url = "http://192.168.1.106:5000/api";

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
  const req = await fetch(`${url}/customer/${id}`);
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
    const {
      // customer_id,
      // deliver_id,
      delivered,
      order_id,
      total,
      deliver_date,
    } = delivery;

    const order = await getOrderById(order_id);
    console.log(order);
    const { order_date, product_id, total_shipped } = order;
    // const customer = await getCustomerById(parseInt(customer_id));

    container.innerHTML += `
      <div class="d-block">
        <div class="dl">
          <div class="status ${delivered ? "delivered" : ""}">
            ${delivered ? "Delivered" : "Pending"}
          </div>

          <div class="order-num">Order ${order_id}</div>

          ${delivered ? `<div class="deliver-date">${deliver_date}</div>` : ""}
        </div>
        <div class="dr">
          <div class="price">P ${total}</div>
          <div class="total-items">Total ${total_shipped} items</div>
        </div>
      </div>
`;
  }
};

// let deliveries = getDeliveries().then((data) => data);
