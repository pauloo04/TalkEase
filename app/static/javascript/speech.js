let recordBlob;

document
  .getElementById("start_recording")
  .addEventListener("click", initFunction);
let isRecording = document.getElementById("is_recording");

function initFunction() {
  // Display recording
  async function getUserMedia(constraints) {
    if (window.navigator.mediaDevices) {
      return window.navigator.mediaDevices.getUserMedia(constraints);
    }
    let legacyApi =
      navigator.getUserMedia ||
      navigator.webkitGetUserMedia ||
      navigator.mozGetUserMedia ||
      navigator.msGetUserMedia;
    if (legacyApi) {
      return new Promise(function (resolve, reject) {
        legacyApi.bind(window.navigator)(constraints, resolve, reject);
      });
    } else {
      alert("user api not supported");
    }
  }
  isRecording.textContent = "Recording...";
  //

  let audioChunks = [];
  let rec;
  function handlerFunction(stream) {
    rec = new MediaRecorder(stream);
    rec.start();
    rec.ondataavailable = (e) => {
      audioChunks.push(e.data);
      if (rec.state == "inactive") {
        recordBlob = new Blob(audioChunks, {
          type: "audio/wav; codecs=MS_PCM",
        });

        let formData = new FormData();
        formData.append("blob", recordBlob);

        console.log("blob", recordBlob);

        $.ajax({
          type: "POST",
          url: "/home/speech",
          data: JSON.stringify(formData),
          processData: false,
          contentType: false,
          success: function (response) {
            console.log();
          },
          error: function (error) {
            console.log();
          },
        }).done(function (data) {
          console.log(data);
        });
      }
    };
  }

  function startusingBrowserMicrophone(boolean) {
    getUserMedia({ audio: boolean }).then((stream) => {
      handlerFunction(stream);
    });
  }
  startusingBrowserMicrophone(true);
  // Stoping handler
  document.getElementById("end_recording").addEventListener("click", (e) => {
    rec.stop();
    isRecording.textContent = "Click play button to start listening";
  });
}
