document.addEventListener('DOMContentLoaded', function() {
    // Dummy data for exams (Replace with actual data)
    const examsData = [
        { name: 'Exam 1', startTime: '10:00 AM', duration: '1 hour' },
        { name: 'Exam 2', startTime: '12:00 PM', duration: '2 hours' },
        { name: 'Exam 3', startTime: '02:00 PM', duration: '1.5 hours' },
    ];

    // Function to populate the exam table
    function populateExamTable() {
        const tbody = document.querySelector('.exam-table tbody');
        tbody.innerHTML = ''; // Clear existing rows

        examsData.forEach(function(exam) {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${exam.name}</td>
                <td>${exam.startTime}</td>
                <td>${exam.duration}</td>
                <td><button class="start-exam-btn">Start</button></td>
            `;
            tbody.appendChild(row);
        });
    }

    // Call the function to populate the exam table
    populateExamTable();;
    
});



