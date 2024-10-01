document.addEventListener("DOMContentLoaded", function () {
    // Example of adding more job data dynamically
    const jobsViewedContainer = document.getElementById("jobs-viewed");
    const jobsAppliedContainer = document.getElementById("jobs-applied");

    const dummyJobsViewed = [
        { title: "UI/UX Designer at DesignPro", dateViewed: "September 13, 2024" },
        { title: "Data Scientist at AI Labs", dateViewed: "September 11, 2024" }
    ];

    const dummyJobsApplied = [
        { title: "Software Engineer at CodeWorks", dateApplied: "September 9, 2024" },
        { title: "Marketing Manager at GrowthInc", dateApplied: "September 7, 2024" }
    ];

    dummyJobsViewed.forEach(job => {
        const jobCard = document.createElement("div");
        jobCard.className = "job-card";
        jobCard.innerHTML = `
            <h3>${job.title}</h3>
            <p>Viewed on: ${job.dateViewed}</p>
            <a href="#" class="job-link">View Job Details</a>
        `;
        jobsViewedContainer.appendChild(jobCard);
    });

    dummyJobsApplied.forEach(job => {
        const jobCard = document.createElement("div");
        jobCard.className = "job-card";
        jobCard.innerHTML = `
            <h3>${job.title}</h3>
            <p>Applied on: ${job.dateApplied}</p>
            <a href="#" class="job-link">View Job Details</a>
        `;
        jobsAppliedContainer.appendChild(jobCard);
    });
});
