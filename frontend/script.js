async function analyzeResume() {
    const fileInput = document.getElementById("resumeFile");

    if (fileInput.files.length === 0) {
        alert("Please upload a resume PDF first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("http://127.0.0.1:8000/analyze-resume/", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    if (data.analysis) {
        sessionStorage.setItem("analysisResult", data.analysis);
        window.location.href = "result.html";
    } else {
        alert("Error analyzing resume.");
    }
}


