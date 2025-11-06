// main.js

document.addEventListener('DOMContentLoaded', function() {

  // cargar bootstrap si no existe
  function loadScript(url, cb){
    var s = document.createElement('script');
    s.src = url;
    s.async = true;
    s.onload = function(){ if(cb) cb(); };
    document.head.appendChild(s);
  }
  var bsUrl = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js';
  if (typeof bootstrap === 'undefined') loadScript(bsUrl);

  // funcion que anima una barra dada 
  function animateBar(bar){
    if (!bar) return;
    var target = bar.getAttribute('data-target');
    if (!target) return;
    var val = parseInt(target, 10);
    if (isNaN(val)) val = 0;
    val = Math.max(0, Math.min(100, val));
    bar.style.setProperty('--target-width', val + '%');
    setTimeout(function(){ bar.classList.add('fill'); }, 50);
  }

  // usar IntersectionObserver si esta disponible
  var bars = document.querySelectorAll('.progress-bar');
  if (bars.length > 0) {
    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function(entries, obs){
        entries.forEach(function(entry){
          if (entry.isIntersecting) {
            animateBar(entry.target);
            obs.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });

      bars.forEach(function(b){ observer.observe(b); });

      // animar todas despues de 3s
      setTimeout(function(){
        bars.forEach(function(b){
          if (!b.classList.contains('fill')) animateBar(b);
        });
      }, 3000);
    } else {
      setTimeout(function(){ bars.forEach(animateBar); }, 200);
    }
  }

// scroll suave para links internos
const navLinks = document.querySelectorAll('a.nav-link[href^="#"]');
if (navLinks.length > 0) {
  navLinks.forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (!target) return;

      const offset = 70; // altura del navbar fijo
      const targetY = target.getBoundingClientRect().top + window.pageYOffset - offset;
      const startY = window.pageYOffset;
      const distance = targetY - startY;
      const duration = 600; // duracion total del desplazamiento 
      let startTime = null;

      // funcion de animacion con easeInOutQuad
      function smoothScroll(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const progress = Math.min(timeElapsed / duration, 1);
        const ease = progress < 0.5
          ? 2 * progress * progress
          : -1 + (4 - 2 * progress) * progress; // easeInOut
        window.scrollTo(0, startY + distance * ease);

        if (timeElapsed < duration) {
          requestAnimationFrame(smoothScroll);
        }
      }

      requestAnimationFrame(smoothScroll);
    });
  });
}


});
