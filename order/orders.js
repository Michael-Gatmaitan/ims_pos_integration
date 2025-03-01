console.log("HEplo!");

const url = "http://127.0.0.1:5000/api/products";

let cart = [];
const handleAddToCart = (product) => {
  if (cart.find((p) => p.pid === product.pid)) {
    const pindex = cart.indexOf(product);
    cart.splice(pindex, 1);
    console.log(cart);
  } else {
    cart.push(product);
  }

  displayCart();
};

const clearCart = () => {};

const deleteItem = (product) => {
  // const itemIndex =
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
      orderQuantity.innerText = q;
    });

    decBtn.addEventListener("click", () => {
      if (q === 1) return;
      q--;
      orderQuantity.innerText = q;
    });

    orderInfo.appendChild(quantityButtons);

    productCard.appendChild(orderInfo);

    orderList.appendChild(productCard);
  }
};

const displayProducts = async () => {
  const response = await fetch(url);
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
      if (product.quantity === 0) {
        alert("The product you selected is out of stock");
        return;
      }
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

displayProducts();
