async function get_simplified_text() {
  const input_text = document.getElementById("input_text").value;
  response = await fetch("http://127.0.0.1:5000/simplify", {
    method: "POST",
    body: JSON.stringify({ input_text: input_text }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  });
  json = await response.json();
  simplified_text = json.simplified_text;
  document.getElementById("simplified").value = simplified_text;
}
