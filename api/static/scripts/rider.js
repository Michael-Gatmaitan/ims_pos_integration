const cta = document.getElementsByClassName("cta")[0];
const url = "http://192.168.100.9:5000/api";

cta.onclick = async () => {
  const req = await fetch(`${url}/rider-scan`);
  document.write("Wait for the qr");
  const res = await req.json();

  console.log(res);

  if (res.deliver_id) {
    // alert(`Delivery with id of ${res.deliver_id} successfully delivered`);
    showConfirmation(
      `Delivery with id of ${res.deliver_id} successfully delivered at ${res.deliver_date} 🚀🚀`,
    );
  }
};

const showConfirmation = (message) => {
  const confirm = document.getElementsByClassName("confirm")[0];
  confirm.style.display = "grid";
  const messageCon = confirm.getElementsByClassName("message")[0];

  messageCon.innerText = message;
};

const hideConfirmation = () => {
  const confirm = document.getElementsByClassName("confirm")[0];
  confirm.style.display = "none";
};
