function predictNoise() {
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      area: document.getElementById("area").value,
      time: document.getElementById("time").value,
      traffic: document.getElementById("traffic").value
    })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText =
      "Noise Risk: " + data.risk;
  });
}
