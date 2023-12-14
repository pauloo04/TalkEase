async function logout() {
  response = await fetch("http://127.0.0.1:5000/home", {
    method: "POST",
    body: JSON.stringify({ message: "logout" }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  });
}
