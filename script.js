const form = document.getElementById("upload-form");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const fileInput = document.getElementById("photo-input");

  if (fileInput.files.length > 0) {
    const file = fileInput.files[0];
    const formData = new FormData();

    formData.append("photo", file);

    fetch("/upload", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          alert("Photo uploaded successfully!");
        } else {
          alert("An error occurred while uploading the photo.");
        }
      })
      .catch((error) => {
        console.error(error);
        alert("An error occurred while uploading the photo.");
      });
  }
});
