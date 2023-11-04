function goBackAndReload() {
    window.history.go(-2); // Go back to the previous page
    window.location.reload(); // Reload the current page (which is now the previous page)
}