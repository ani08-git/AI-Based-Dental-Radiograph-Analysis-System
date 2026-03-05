// Image preview when user uploads file
document.getElementById("imageUpload").addEventListener("change", function(event){

    const file = event.target.files[0];

    if(!file) return;

    const reader = new FileReader();

    reader.onload = function(){
        document.getElementById("preview").src = reader.result;
    };

    reader.readAsDataURL(file);

});


// Function to send image to backend
function sendImage(endpoint){

    const fileInput = document.getElementById("imageUpload");

    if(fileInput.files.length === 0){
        alert("Please upload an X-ray image first");
        return;
    }

    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("image", file);

    document.getElementById("resultText").innerText = "Processing...";

    fetch("http://127.0.0.1:5000/" + endpoint, {

        method: "POST",
        body: formData

    })
    .then(response => response.json())
    .then(data => {

        // Show result text
        document.getElementById("resultText").innerText = data.result;

        // Show processed image returned from backend
        document.getElementById("preview").src =
            "http://127.0.0.1:5000" + data.image + "?t=" + new Date().getTime();

    })
    .catch(error => {

        console.error("Error:", error);

        document.getElementById("resultText").innerText =
            "Error analyzing image.";

    });

}


// Button actions

function segment(){
    sendImage("segment");
}

function toothNumber(){
    sendImage("tooth_number");
}

function detectMissing(){
    sendImage("missing_tooth");
}

function classifyImplant(){
    sendImage("implant_classify");
}