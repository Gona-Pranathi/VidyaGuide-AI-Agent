

async function analyzeResume() {
  const fileInput = document.getElementById("resumeFile");
  const file = fileInput.files[0];

  if (!file) {
    alert("Please select a resume PDF first.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://127.0.0.1:8000/analyze-resume/", {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    // Save analysis to browser storage
    localStorage.setItem("resumeAnalysis", data.analysis);

    // Redirect to result page
    window.location.href = "result.html";

  } catch (error) {
    alert("Error connecting to backend.");
    console.error(error);
  }
}