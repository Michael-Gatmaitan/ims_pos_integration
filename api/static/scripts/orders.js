console.log("HEplo!");

// const url = "http://127.0.0.1:5000/api";
const url = "http://192.168.100.9:5000/api";
//192.168.100.9:5000/api/

document.getElementsByClassName("close")[0].addEventListener("click", () => {
  closeModal();
});

// function setAnimationDelays() {
//   const ps = document.getElementsByClassName("p");
//   for (let i = 0; i < ps.length; i++) {
//     const p = ps[i];
//     p.style.animationDelay = `${i}s`;
//   }
// }
// setAnimationDelays();

const getCustomerById = async (id) => {
  const req = await fetch(`${url}/customer/${id}`);
  const customer = await req.json();

  return customer;
};

const getProductById = async (id) => {
  const req = await fetch(`${url}/products/${id}`);
  const product = await req.json();

  return product;
};

let cart = [];
const handleAddToCart = (product) => {
  let idx = -1;
  for (let i = 0; i < cart.length; i++) {
    if (cart[i].pid === product.pid) {
      idx = i;
    }
  }

  if (idx !== -1) {
    cart.splice(idx, 1);
  } else {
    cart.push({ ...product, orderQuantity: 1 });
  }

  displayCart();
};

const handleClearCart = () => {
  cart = [];
  displayCart();
};

const placeOrder = async () => {
  // const cart
  console.log(cart);

  const customerSelect = document.getElementsByName("customer")[0];
  const customerVal = parseInt(customerSelect.value);

  let headers = new Headers();

  headers.append("Content-Type", "application/json");
  headers.append("Accept", "application/json");

  headers.append("Access-Control-Allow-Origin", "*");
  headers.append("Access-Control-Allow-Credentials", "true");

  headers.append("GET", "POST", "OPTIONS");

  // const placeOrderStack = [];

  for (order of cart) {
    console.log(order);

    const customer = await getCustomerById(customerVal);
    const product = await getProductById(parseInt(order.pid));

    console.log(customer, product);

    if (customer.balance < product.base_price) {
      console.error("Insufficient balance");
    }

    // This request causes chain function call to achieve creating
    // of ims_order, sales, delivery, and qrcode generator
    const placeOrderReq = await fetch(
      `${url}/place-order?customer_id=${customerVal}&pid=${parseInt(order.pid)}&q=${order.orderQuantity}`,
      {
        mode: "no-cors",
        method: "POST",
        // headers: headers,
      },
    );

    console.log(placeOrderReq.status);
  }
  showModal(cart);
  cart = [];
  displayCart();

  // Display modal
};

const showModal = async (cart) => {
  // Create delivery id
  const modal = document.getElementsByClassName("rec-qr")[0];

  console.log("Showing modal");
  console.log(cart);

  modal.style.display = "block";

  const recOrders = modal.getElementsByClassName("rec-orders")[0];

  let total = 0;

  cart.forEach((item) => {
    total = item.base_price;

    recOrders.innerHTML += `
      <tr>
        <td align="right">${item.orderQuantity}</td>
        <td align="center">${item.pname}</td>
        <td align="right">₱ ${item.base_price}</td>
      </tr>
    `;
  });

  const totalVal = modal.getElementsByClassName("total-val")[0];
  totalVal.innerHTML = total;

  const qrImageDiv = modal.getElementsByClassName("qr-image")[0];
  // Get last qr stored
  const req = await fetch(`${url}/last-qr`);
  const lastQr = await req.json();

  console.log(lastQr.qrpath);

  qrImageDiv.innerHTML = `<img src="../${lastQr.qrpath}"/>`;
};

const closeModal = () => {
  const modal = document.getElementsByClassName("rec-qr")[0];
  const recOrders = modal.getElementsByClassName("rec-orders")[0];
  recOrders.innerHTML = `          <tr>
            <th>QTY</th>
            <th>ITEM</th>
            <th align="right">TOTAL</th>
          </tr>
`;

  modal.style.display = "none";
};

const customerSelect = () => {
  console.log("Customer selected");
};

// base_price
// description
// model
// pname
// quantity
// unit
//
const handleRemoveCart = (product) => console.log(product);

const displayCart = () => {
  const orderList = document.getElementById("order-list");
  orderList.innerHTML = "";

  for (let i = 0; i < cart.length; i++) {
    const product = cart[i];
    let q = 1;

    const productCard = document.createElement("div");
    productCard.classList.add("product-card");
    const productInfo = document.createElement("div");
    productInfo.classList.add("product-info");
    const productName = document.createElement("div");
    productName.classList.add("product-name");
    productName.innerText = product.pname;
    const productPrice = document.createElement("div");
    productPrice.classList.add("product-price");
    productPrice.innerText = `₱ ${product.base_price}`;
    const productQuantity = document.createElement("div");
    productQuantity.classList.add("product-quantity");
    productQuantity.innerText = `Stock: ${product.quantity}`;

    productInfo.appendChild(productName);
    productInfo.appendChild(productPrice);
    productInfo.appendChild(productQuantity);

    productCard.appendChild(productInfo);

    const orderInfo = document.createElement("div");
    orderInfo.classList.add("order-info");
    const removeContainer = document.createElement("div");
    removeContainer.classList.add("remove-container");
    const removeButton = document.createElement("button");
    removeButton.innerHTML = `<img src='../static/images/trash.png' />`;
    removeButton.classList.add("remove-btn");

    removeContainer.append(removeButton);
    orderInfo.appendChild(removeContainer);

    const quantityButtons = document.createElement("div");
    quantityButtons.classList.add("quantity-btns");
    const decBtn = document.createElement("button");
    decBtn.classList.add("dec-q");
    decBtn.innerText = "-";
    const orderQuantity = document.createElement("div");
    orderQuantity.classList.add("order-quantity");

    orderQuantity.innerText = q;
    const incBtn = document.createElement("button");
    incBtn.classList.add("inc-q");
    incBtn.innerText = "+";

    quantityButtons.appendChild(decBtn);
    quantityButtons.appendChild(orderQuantity);
    quantityButtons.appendChild(incBtn);

    // events
    removeButton.addEventListener("click", () => {
      handleAddToCart(product);
    });

    incBtn.addEventListener("click", () => {
      if (q >= product.quantity) {
        alert(`Maximum available quantity of ${product.quantity} reached.`);
        return;
      }
      q++;
      cart[i].orderQuantity += 1;
      orderQuantity.innerText = q;
    });

    decBtn.addEventListener("click", () => {
      if (q === 1) return;
      q--;
      cart[i].orderQuantity -= 1;
      orderQuantity.innerText = q;
    });

    orderInfo.appendChild(quantityButtons);

    productCard.appendChild(orderInfo);

    orderList.appendChild(productCard);
  }
};

const displayProducts = async () => {
  const response = await fetch(`${url}/products`);
  const data = await response.json();

  const container = document.getElementById("container");

  if (data.length <= 0) {
    container.innerHTML = `<code>No productes yet.</code>`;
    return;
  }

  // base_price
  // description
  // model
  // pname
  // quantity
  // unit

  for (let i = 0; i < data.length; i++) {
    const product = data[i];

    console.log(product);

    // DOM for product

    const pCon = document.createElement("div");

    pCon.style.opacity = 0;
    pCon.style.animationDelay = `${i / 20}s`;
    console.log(i);

    setTimeout(() => (pCon.style.opacity = 1), (i / 20) * 1000);
    pCon.classList.add("p");
    const pHead = document.createElement("div");
    pHead.classList.add("p-head");
    const pn = document.createElement("h2");
    pn.classList.add("pn");
    pn.innerText = product.pname;
    const pd = document.createElement("p");
    pd.classList.add("pd");
    pd.innerText = product.description;
    pHead.appendChild(pn);
    pHead.appendChild(pd);
    pCon.appendChild(pHead);

    const pFoot = document.createElement("div");
    pFoot.classList.add("p-foot");
    const pq = document.createElement("div");
    pq.classList.add("pq");

    const d1 = document.createElement("div");
    d1.classList.add("d");
    d1.innerText = product.quantity;
    const t1 = document.createElement("div");
    t1.classList.add("title");
    t1.innerText = product.quantity >= 1 ? "Available" : "Out of stock";

    const pbp = document.createElement("div");
    pbp.classList.add("pbp");

    const d2 = document.createElement("div");
    d2.classList.add("d");
    d2.innerText = `₱ ${product.base_price}`;
    const t2 = document.createElement("div");
    t2.classList.add("title");
    t2.innerText = "Price";

    pq.appendChild(d1);
    pq.appendChild(t1);
    pFoot.appendChild(pq);

    pbp.appendChild(d2);
    pbp.appendChild(t2);
    pFoot.appendChild(pbp);
    pCon.appendChild(pFoot);
    container.appendChild(pCon);

    pCon.addEventListener("click", () => {
      if (product.quantity <= 0) {
        alert("The product you selected is out of stock");
        return;
      }

      pCon.classList.toggle("p-active");
      handleAddToCart(product);
    });

    // container.innerHTML += `
    //         <div class="p">
    //           <div class="p-head">
    //             <h2 class="pn">${product.pname}</h2>
    //             <p class="pd">${product.description}</p>
    //           </div>
    //
    //           <div class="p-foot">
    //             <div class="pq">
    //               <div class="d">${product.quantity}</div>
    //               <div class="title">Available</div>
    //             </div>
    //             <div class="pbp r">
    //               <div class="d">${product.base_price}</div>
    //               <div class="title">Price</div>
    //             </div>
    //           </div>
    //
    //         <button onClick="handler()">Hello!!!</button>
    //         </div>
    //       `;
  }
};

const appendCustomers = async () => {
  const selectCustomer = document.getElementsByClassName("customers")[0];
  const res = await fetch(`${url}/customers`);
  const data = await res.json();

  console.log(data);

  for (customer of data) {
    console.log(customer);

    selectCustomer.innerHTML += `
      <option value="${customer.id}">${customer.name}</option>
    `;
  }
};

appendCustomers();

displayProducts();
