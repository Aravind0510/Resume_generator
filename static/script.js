document.getElementById("pdfForm").onsubmit = async function (e) {
    e.preventDefault();

    const formData = new FormData();
    const file = document.getElementById("pdfUpload").files[0];
    formData.append("file", file);

    document.getElementById("output").innerText = "Generating resume...";

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });
        const result = await response.json();

        if (response.ok) {
            const resumeFilename = result.resume_url.split('/').pop();
            const viewLink = result.resume_url;
            const downloadLink = `/uploads/${resumeFilename}`;
            
            document.getElementById("output").innerHTML = `
                <p>Resume generated successfully!</p>
                <a href="${viewLink}" target="_blank">View Resume</a><br>
                
            `;
        } else {
            document.getElementById("output").innerText = "Error: " + result.message;
        }
    } catch (error) {
        console.error(error);
        document.getElementById("output").innerText = "An error occurred!";
    }
};

document.getElementById("pdfForm").onsubmit = async function (e) {
    e.preventDefault();

    const formData = new FormData();
    const file = document.getElementById("pdfUpload").files[0];
    formData.append("file", file);

    const outputDiv = document.getElementById("output");
    const spinner = document.getElementById("loadingSpinner");
    const progressBar = document.getElementById("progressBar");

    outputDiv.innerText = "";
    spinner.style.display = "block"; // Show spinner
    progressBar.style.display = "block"; // Show progress bar
    let progress = 0;
    const interval = setInterval(() => {
        progress += 10;
        if (progress > 100) progress = 100;
        progressBar.firstElementChild.style.width = progress + "%";
    }, 500);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();

        if (response.ok) {
            outputDiv.innerHTML = `
                <p class="success">Resume generated successfully!</p>
                <a href="${result.resume_url}" target="_blank">View Resume</a><br>
            `;
            outputDiv.classList.add('success'); // Success animation
        } else {
            outputDiv.innerText = "Error: " + result.message;
        }
    } catch (error) {
        console.error(error);
        outputDiv.innerText = "An error occurred!";
    } finally {
        spinner.style.display = "none"; // Hide spinner
        clearInterval(interval); // Stop progress bar
        progressBar.style.display = "none";
    }
};

const quotes = [
    "Your future starts with a strong resume.",
    "Let your resume speak for you!",
    "Craft a resume that stands out.",
    "Your career journey begins with the right resume."
];

// Function to change quote every 5 seconds
function changeQuote() {
    const quoteElement = document.getElementById('dynamicQuote');
    let index = 0;
    setInterval(() => {
        quoteElement.innerText = quotes[index];
        index = (index + 1) % quotes.length;
    }, 5000); // Change every 5 seconds
}

// Execute the function after DOM is ready
document.addEventListener('DOMContentLoaded', function () {
    changeQuote();
});