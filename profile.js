document.addEventListener('DOMContentLoaded', function() {
    // Dummy function for edit email button (Replace with actual functionality)
    const editEmailButton = document.querySelector('.edit-email-btn');
    editEmailButton.addEventListener('click', function() {
        alert('Edit Email functionality will be implemented here.');
    });

    // Dummy function for edit profile pic button (Replace with actual functionality)
    const editProfilePicButton = document.querySelector('.edit-profile-pic-btn');
    editProfilePicButton.addEventListener('click', function() {
        alert('Edit Profile Picture functionality will be implemented here.');
    });

    const backButton = document.querySelector('.back-button');
    backButton.addEventListener('click', function(event) {
        event.preventDefault();
        // Redirect to dashboard.html
        window.location.href = 'dashboard.html';
    });
});
