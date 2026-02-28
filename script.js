// Register GSAP plugins
gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

document.addEventListener("DOMContentLoaded", () => {

    // --- Custom Cursor ---
    const cursor = document.querySelector('.cursor');
    const interactiveElements = document.querySelectorAll('button, a, .logo');
    const iframeElements = document.querySelectorAll('iframe');
    const embedWrappers = document.querySelectorAll('.embed-wrapper');

    window.addEventListener('mousemove', (e) => {
        gsap.to(cursor, {
            x: e.clientX,
            y: e.clientY,
            duration: 0.1,
            ease: "power2.out"
        });
    });

    // Make cursor expand slightly on clickable text/buttons
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => cursor.classList.add('hovering'));
        el.addEventListener('mouseleave', () => cursor.classList.remove('hovering'));
    });

    // Hide the custom cursor completely when moving over iframes (Soundcloud)
    // because the iframe eats mouse events and freezes the custom cursor on the edge.
    // We bind this to the embed wrappers since the iframe swallows internal events.
    embedWrappers.forEach(el => {
        el.addEventListener('mouseenter', () => cursor.classList.add('hidden-cursor'));
        el.addEventListener('mouseleave', () => cursor.classList.remove('hidden-cursor'));
    });

    // --- Navigation & Smooth Scroll ---
    const navButtons = document.querySelectorAll('[data-scroll]');

    navButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const target = btn.getAttribute('data-scroll');

            gsap.to(window, {
                duration: 1.5,
                scrollTo: {
                    y: target,
                    offsetY: () => document.querySelector('.navbar').offsetHeight - 10
                },
                ease: "power4.inOut"
            });
        });
    });

    // Change nav style on scroll
    window.addEventListener('scroll', () => {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- Initial Load Animations ---
    const tl = gsap.timeline();

    // Hero title text for entrance animation
    const word = document.querySelector('.hero-title .word');

    // basic wrap to clipping div
    const text = word.innerText;
    word.innerHTML = '';
    const innerSpan = document.createElement('span');
    innerSpan.style.display = 'inline-block';
    innerSpan.innerText = text;
    word.appendChild(innerSpan);
    // Add styling inline for clip-path animation
    word.style.clipPath = 'polygon(0 0, 100% 0, 100% 100%, 0% 100%)';
    gsap.set(innerSpan, { y: 200 });

    tl.to('.hero-image', {
        scale: 1,
        duration: 2,
        ease: "power3.out"
    })
        .to('.hero-title .word span', {
            y: 0,
            duration: 1.5,
            ease: "power4.out"
        }, "-=1.5")
        .fromTo(['.navbar', '.scroll-indicator'],
            { opacity: 0 },
            { opacity: 1, duration: 1, stagger: 0.2 },
            "-=0.5"
        );

    // --- Scroll Trigger Animations ---

    // Parallax on hero image
    gsap.to('.hero-image-wrapper', {
        yPercent: 30,
        ease: "none",
        scrollTrigger: {
            trigger: ".hero-section",
            start: "top top",
            end: "bottom top",
            scrub: true
        }
    });

    // Fade up sections
    const sections = ['#releases', '#podcasts', '#biography'];

    sections.forEach(sec => {
        const sectionEl = document.querySelector(sec);
        const title = sectionEl.querySelector('.section-title');
        const embeds = sectionEl.querySelectorAll('.embed-wrapper');

        // Reveal Title
        gsap.fromTo(title,
            { opacity: 0, y: 100 },
            {
                opacity: 1,
                y: 0,
                duration: 1.2,
                ease: "power3.out",
                scrollTrigger: {
                    trigger: sectionEl,
                    start: "top 80%",
                }
            }
        );

        // Reveal Embeds (staggered)
        gsap.fromTo(embeds,
            { opacity: 0, y: 50 },
            {
                opacity: 1,
                y: 0,
                duration: 1,
                stagger: 0.2,
                ease: "power3.out",
                scrollTrigger: {
                    trigger: sectionEl,
                    start: "top 60%",
                }
            }
        );
    });
});
