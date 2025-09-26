const url = "http://127.0.0.1:8000/api/customers";

fetch(url)
  .then((resp) => resp.json())
  .then((customemrs) => {
    customemrs.forEach((c) => {
      const customer = `<tr>
                <td>${c.id}</td>
                <td>${c.name}</td>
                <td>${c.email}</td>
                <td>${c.phone}</td>
                <td>${c.city}</td>
            </tr>`;
      document.getElementById("customer_rows").innerHTML += customer;
    });
  });
