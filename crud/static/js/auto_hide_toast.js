document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        const toasts = document.querySelectorAll('[id^="toast-"]');
        toasts.forEach(toast => {
            toast.style.opacity = "0";
            toast.style.transform = "translateX(100%)";

            setTimeout(() => {
                toast.remove();
            }, 300); // matches animation
        });
    }, 2000);
});