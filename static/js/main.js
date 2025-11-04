// main.js
// carga bootstrap y anima barras de progreso cuando entran en pantalla
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

  // funcion que anima una barra dada (lee data-target)
  function animateBar(bar){
    if (!bar) return;
    var target = bar.getAttribute('data-target');
    if (!target) return;
    // segurizar el valor: numero entre 0 y 100
    var val = parseInt(target, 10);
    if (isNaN(val)) val = 0;
    val = Math.max(0, Math.min(100, val));
    // aplicar la variable css y la clase que la usa
    bar.style.setProperty('--target-width', val + '%');
    // un pequeño delay
    setTimeout(function(){ bar.classList.add('fill'); }, 50);
  }

  // usar IntersectionObserver si esta disponible
  var bars = document.querySelectorAll('.progress-bar');
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

    // si despues de 3s todavia no se animaron, animar todas
    setTimeout(function(){
      bars.forEach(function(b){
        if (!b.classList.contains('fill')) animateBar(b);
      });
    }, 3000);

  } else {
    // si no hay observer, animar todas despues de short delay
    setTimeout(function(){
      bars.forEach(function(b){ animateBar(b); });
    }, 200);
  }

});
