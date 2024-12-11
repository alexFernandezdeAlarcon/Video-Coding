document.getElementById("video-form").addEventListener("submit", async (event) => {
    event.preventDefault();

    const videoFile = document.getElementById("video-file").files[0];
    const format = document.getElementById("conversion-format").value;

    if (!videoFile) {
        alert("Please choose a video file.");
        return;
    }

    // Show the loading spinner and hide the response message
    document.getElementById("loading").style.display = "block";
    document.getElementById("response").style.display = "none";

    const formData = new FormData();
    formData.append("input_file", videoFile);
    formData.append("format", format);

    try {
        const response = await fetch("http://127.0.0.1:5000/convert_to_format", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();
        // Hide the loading spinner after the request is done
        document.getElementById("loading").style.display = "none";

        if (response.ok) {
            const downloadUrl = `http://127.0.0.1:5000/converted_files/${result.output_file}`;
            document.getElementById("response").innerHTML = `
                <div class="alert alert-success">
                    Conversion successful! <br>
                    <a href="${downloadUrl}" download>Download Converted Video</a>
                </div>
            `;
        } else {
            document.getElementById("response").innerHTML = `
                <div class="alert alert-danger">Error: ${result.error}</div>
            `;
        }
    } catch (error) {
        console.error(error);
        // Hide the spinner if an error occurs
        document.getElementById("loading").style.display = "none";
        document.getElementById("response").innerHTML = `
            <div class="alert alert-danger">An error occurred. Check console for details.</div>
        `;
    }

    // Show the response message
    document.getElementById("response").style.display = "block";
});
