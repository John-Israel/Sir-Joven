setTimeout(() => {
    // This finds ALL elements with the id "toast-success"
    const toasts = document.querySelectorAll('#toast-success');
    toasts.forEach(toast => {
        toast.style.display = 'none';
    });
}, 2000); // 2000ms = 2 seconds