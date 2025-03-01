// const labels = Utils.months({count: 7});
// const data = {
//   labels: labels,
//   datasets: [{
//     label: 'My First Dataset',
//     data: [65, 59, 80, 81, 56, 55, 40],
//     backgroundColor: [
//       'rgba(255, 99, 132, 0.2)',
//       'rgba(255, 159, 64, 0.2)',
//       'rgba(255, 205, 86, 0.2)',
//       'rgba(75, 192, 192, 0.2)',
//       'rgba(54, 162, 235, 0.2)',
//       'rgba(153, 102, 255, 0.2)',
//       'rgba(201, 203, 207, 0.2)'
//     ],
//     borderColor: [
//       'rgb(255, 99, 132)',
//       'rgb(255, 159, 64)',
//       'rgb(255, 205, 86)',
//       'rgb(75, 192, 192)',
//       'rgb(54, 162, 235)',
//       'rgb(153, 102, 255)',
//       'rgb(201, 203, 207)'
//     ],
//     borderWidth: 1
//   }]
// };
//

let xValues = [];
let yValues = [];

const getSalesX = async () => {
  const req = await fetch("http://127.0.0.1:5000/api/sales");
  const data = await req.json();

  // console.log(data);

  xValues = data.map((sale) => sale.sale_value);
  yValues = data.map((sale) => sale.order_id);

  // const orders = data.map((sale) => sale.order_id);
  // orders.forEach(async (order_id) => {
  //   const req = await fetch(`http://127.0.0.1:5000/api/order/${order_id}`);
  //
  //   const data = await req.json();
  //
  //   // console.log(data);
  //
  //   yValues.push(data.order_date);
  //   console.log(yValues);
  // });
};

getSalesX().then((_) => {
  // yValues = new Array(xValues.length).fill(0);
  console.log(xValues, yValues);

  var barColors = ["red", "green", "blue", "orange", "brown"];

  new Chart("myChart", {
    type: "bar",
    data: {
      labels: yValues,
      datasets: [
        {
          backgroundColor: barColors,
          data: xValues,
        },
      ],
    },
    // options: {...}
  });
});

// console.log(xValues, yValues);

// var xValues = ["Italy", "France", "Spain", "USA", "Argentina"];
// var yValues = [55, 49, 44, 24, 15];
