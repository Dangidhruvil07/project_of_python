document.addEventListener("DOMContentLoaded", function () {

    // ── CATEGORY FILTER ──
    const buttons = document.querySelectorAll(".category-card");
    const products = document.querySelectorAll(".product-item");

    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            buttons.forEach(b => b.classList.remove("active"));
            btn.classList.add("active");

            const filter = btn.getAttribute("data-filter");

            products.forEach(product => {
                const category = product.getAttribute("data-category");
                product.style.display = (filter === "all" || filter === category) ? "block" : "none";
            });
        });
    });

    // ── FADE-UP on scroll (Intersection Observer) ──
    const fadeEls = document.querySelectorAll(".fade-up");
    if ("IntersectionObserver" in window) {
        const io = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.style.opacity = "1";
                    e.target.style.transform = "translateY(0)";
                }
            });
        }, { threshold: 0.1 });

        fadeEls.forEach(el => {
            el.style.opacity = "0";
            el.style.transform = "translateY(20px)";
            el.style.transition = "opacity 0.5s ease, transform 0.5s ease";
            io.observe(el);
        });
    }

    // ── ACTIVE NAV LINK ──
    const currentPath = window.location.pathname;
    document.querySelectorAll(".navbar-nav .nav-link").forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });

});
