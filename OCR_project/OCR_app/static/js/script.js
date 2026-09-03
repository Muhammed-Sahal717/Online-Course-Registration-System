document.addEventListener("DOMContentLoaded", () => {
  // Highlight active nav link dynamically
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll(".nav-link");

  navLinks.forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.style.color = "var(--primary-color)";
      link.style.fontWeight = "700";
    }
  });

  // Client-side confirmation on submission
  const forms = document.querySelectorAll(".app-form");
  forms.forEach((form) => {
    form.addEventListener("submit", () => {
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.textContent = "Submitting...";
      }
    });
  });
});
