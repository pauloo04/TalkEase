async function get_feedbacked_text() {
  const input_text = document.getElementById("input_text").value;
  response = await fetch("http://127.0.0.1:5000/feedback", {
    method: "POST",
    body: JSON.stringify({ input_text: input_text }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  });
  json = await response.json();
  feedbacked_text = json.feedbacked_text;
  document.getElementById("feedbacked").value = feedbacked_text;
}

async function get_audio() {
  let speed = 1;
  if (document.getElementById("slow").checked) {
    speed = 0.5;
  }
  const feedbacked_text = document.getElementById("feedbacked").value;
  var response = await fetch("http://127.0.0.1:5000/audio", {
    method: "POST",
    body: JSON.stringify({ text: feedbacked_text }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  });
  response = await response.blob();
  var blob = new Blob([response], { type: "audio/wav" });
  var blobUrl = URL.createObjectURL(blob);
  audio = document.getElementById("audio");
  audio.src = blobUrl;
  audio.controls = true;
  audio.hidden = false;
}
