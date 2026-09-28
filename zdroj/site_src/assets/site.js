/* Superticket.sk – drobné interakcie (bez knižníc) */
(function () {
  var d = document, html = d.documentElement;
  html.classList.add('js');

  /* Mobilné menu */
  var mb = d.querySelector('.menu-btn'), mn = d.getElementById('mnav');
  function closeMenu() { if (!mb) return; mb.setAttribute('aria-expanded', 'false'); mn.hidden = true; }
  if (mb && mn) {
    mb.addEventListener('click', function () {
      var open = mb.getAttribute('aria-expanded') === 'true';
      mb.setAttribute('aria-expanded', String(!open));
      mn.hidden = open;
    });
    mn.addEventListener('click', function (e) { if (e.target.closest('a')) closeMenu(); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });
  }

  /* Kopírovanie e-mailu / telefónu */
  d.querySelectorAll('[data-copy]').forEach(function (b) {
    var label = b.querySelector('.lbl');
    var orig = label ? label.textContent : '';
    b.addEventListener('click', function () {
      var text = b.getAttribute('data-copy');
      function done(msg) { if (label) { label.textContent = msg; setTimeout(function () { label.textContent = orig; }, 2200); } }
      function selectFallback() {
        var el = d.getElementById(b.getAttribute('aria-controls'));
        if (el) { var r = d.createRange(); r.selectNodeContents(el); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); }
        done('Označené');
      }
      try {
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () { done('Skopírované'); }, selectFallback);
        } else { selectFallback(); }
      } catch (e) { selectFallback(); }
    });
  });

  /* Lepiace CTA na mobile (detail podujatia) */
  var sc = d.querySelector('.sticky-cta');
  if (sc && 'IntersectionObserver' in window) {
    var watch = [d.querySelector('.ehero'), d.getElementById('vstupenky')].filter(Boolean), vis = new Map();
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { vis.set(e.target, e.isIntersecting); });
      var anyVisible = false; vis.forEach(function (v) { if (v) anyVisible = true; });
      sc.classList.toggle('is-on', !anyVisible);
    }, { threshold: 0 });
    watch.forEach(function (t) { io.observe(t); });
  }

  /* Toast po pridaní do košíka (volá ho Bzuco callback) */
  var toast = d.getElementById('toast'), tt;
  window.stToast = function () {
    if (!toast) return;
    toast.hidden = false;
    requestAnimationFrame(function () { toast.classList.add('is-on'); });
    clearTimeout(tt);
    tt = setTimeout(function () { toast.classList.remove('is-on'); }, 6000);
  };

  /* Bzuco: ak sa predaj nenačíta do 12 s, ukážeme náhradný kontakt */
  d.querySelectorAll('[data-bz-slot]').forEach(function (slot) {
    setTimeout(function () {
      if (!html.classList.contains('bz-ready')) slot.classList.add('bz-failed');
    }, 12000);
  });


  /* Obsah právnych textov – na desktope rozbalený */
  if (window.matchMedia && matchMedia('(min-width:1040px)').matches) {
    d.querySelectorAll('details.toc').forEach(function (t) { t.open = true; });
  }




  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Veľké karty – svetelný bod sleduje kurzor */
  d.querySelectorAll('[data-spot]').forEach(function (el) {
    el.addEventListener('pointermove', function (e) {
      var r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (e.clientX - r.left) + 'px');
      el.style.setProperty('--my', (e.clientY - r.top) + 'px');
    });
  });

  /* Odznak – čísla sa pri zobrazení napočítajú */
  var nums = d.querySelectorAll('[data-count]');
  if (nums.length && 'IntersectionObserver' in window && !reduce) {
    var fmt = function (n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '\u00a0'); };
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        cio.unobserve(en.target);
        var el = en.target, end = +el.getAttribute('data-count'), small = el.querySelector('small');
        var suffix = small ? small.outerHTML : '', t0 = performance.now(), dur = 1600;
        (function step(t) {
          var k = Math.min(1, (t - t0) / dur), v = Math.round(end * (1 - Math.pow(1 - k, 3)));
          el.innerHTML = fmt(v) + suffix;
          if (k < 1) requestAnimationFrame(step);
        })(t0);
      });
    }, { threshold: 0.5 });
    nums.forEach(function (n) { cio.observe(n); });
  }

  /* Minulé akcie – vitrína (karusel) */
  d.querySelectorAll('[data-show]').forEach(function (show) {
    var slides = show.querySelectorAll('.show__slide'), txts = show.querySelectorAll('.show__txt'),
        plays = show.querySelectorAll('.show__play'), bars = show.querySelectorAll('.show__bar'),
        n = slides.length, cur = 0, timer = null, DUR = 5500;
    show.style.setProperty('--dur', DUR + 'ms');
    function go(k) {
      cur = (k + n) % n;
      slides.forEach(function (s, j) { s.classList.toggle('is-on', j === cur); });
      txts.forEach(function (s) { s.hidden = +s.getAttribute('data-i') !== cur; });
      plays.forEach(function (s) { s.hidden = +s.getAttribute('data-i') !== cur; });
      bars.forEach(function (b, j) {
        b.classList.toggle('is-done', j < cur);
        b.classList.remove('is-on'); void b.offsetWidth;
        b.classList.toggle('is-on', j === cur);
        b.setAttribute('aria-selected', j === cur ? 'true' : 'false');
      });
      restart();
    }
    function restart() { clearTimeout(timer); if (!reduce && !show.classList.contains('is-paused')) timer = setTimeout(function () { go(cur + 1); }, DUR); }
    show.querySelector('[data-prev]').addEventListener('click', function () { go(cur - 1); });
    show.querySelector('[data-next]').addEventListener('click', function () { go(cur + 1); });
    bars.forEach(function (b) { b.addEventListener('click', function () { go(+b.getAttribute('data-go')); }); });
    show.addEventListener('mouseenter', function () { show.classList.add('is-paused'); clearTimeout(timer); });
    show.addEventListener('mouseleave', function () { show.classList.remove('is-paused'); go(cur); });
    var sx = null, stage = show.querySelector('.show__stage');
    stage.addEventListener('pointerdown', function (e) { sx = e.clientX; });
    stage.addEventListener('pointerup', function (e) { if (sx === null) return; var dx = e.clientX - sx; sx = null; if (Math.abs(dx) > 40) go(cur + (dx < 0 ? 1 : -1)); });
    show.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') go(cur + 1); if (e.key === 'ArrowLeft') go(cur - 1); });
    if (reduce) show.classList.add('is-paused');
    go(0);
  });

  /* Minulé akcie – filter */
  var grid = d.querySelector('[data-pgrid]');
  d.querySelectorAll('[data-filter]').forEach(function (b, _, all) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      all.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      grid.classList.remove('is-anim'); void grid.offsetWidth; grid.classList.add('is-anim');
      grid.querySelectorAll('.pcard').forEach(function (c) {
        var ok = f === 'all' || (f === 'video' ? c.hasAttribute('data-video') : c.getAttribute('data-year') === f);
        c.hidden = !ok;
      });
    });
  });


  /* Grafika -> fotka: na dotykových zariadeniach sa pri zobrazení karty striedajú */
  var touch = window.matchMedia && matchMedia('(hover: none)').matches;
  if (touch && !reduce && 'IntersectionObserver' in window) {
    var timers = new Map();
    var rio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var el = en.target;
        if (en.isIntersecting) {
          if (!timers.has(el)) timers.set(el, setInterval(function () { el.classList.toggle('is-reveal'); }, 3200));
        } else {
          clearInterval(timers.get(el)); timers.delete(el); el.classList.remove('is-reveal');
        }
      });
    }, { threshold: 0.55 });
    d.querySelectorAll('[data-reveal]').forEach(function (el) { rio.observe(el); });
  }

  /* Odpočty (koniec cenovej vlny / začiatok podujatia) */
  var cds = d.querySelectorAll('[data-countdown]');
  if (cds.length) {
    var pad = function (n) { return (n < 10 ? '0' : '') + n; };
    var tick = function () {
      var now = Date.now();
      cds.forEach(function (el) {
        var diff = Date.parse(el.getAttribute('data-countdown')) - now;
        if (isNaN(diff)) return;
        if (diff <= 0) { el.classList.add('is-over'); var w = el.closest('.wave'); if (w) w.hidden = true; return; }
        var s = Math.floor(diff / 1000), dd = Math.floor(s / 86400), hh = Math.floor(s % 86400 / 3600), mm = Math.floor(s % 3600 / 60), ss = s % 60;
        var set = function (u, v) { var b = el.querySelector('[data-u="' + u + '"]'); if (b && b.textContent !== v) b.textContent = v; };
        set('d', String(dd)); set('h', pad(hh)); set('m', pad(mm)); set('s', pad(ss));
      });
    };
    tick(); setInterval(tick, 1000);
  }

  /* Galéria – zväčšenie fotiek (lightbox) */
  var lbLinks = d.querySelectorAll('[data-lb]');
  if (lbLinks.length) {
    var lb, lbImg, lbCount, group = [], idx = 0, lastFocus = null;
    var build = function () {
      lb = d.createElement('div'); lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Fotogaléria'); lb.hidden = true;
      var ic = function (n) { return '<svg class="ico" aria-hidden="true"><use href="#i-' + n + '"/></svg>'; };
      lb.innerHTML = '<img class="lb__img" alt="">' +
        '<button class="lb__btn lb__close" type="button" aria-label="Zavrieť">' + ic('close') + '</button>' +
        '<button class="lb__btn lb__prev" type="button" aria-label="Predchádzajúca fotka">' + ic('arrow') + '</button>' +
        '<button class="lb__btn lb__next" type="button" aria-label="Ďalšia fotka">' + ic('arrow') + '</button>' +
        '<span class="lb__count"></span>';
      d.body.appendChild(lb);
      lbImg = lb.querySelector('.lb__img'); lbCount = lb.querySelector('.lb__count');
      lb.querySelector('.lb__close').addEventListener('click', close);
      lb.querySelector('.lb__prev').addEventListener('click', function () { show(idx - 1); });
      lb.querySelector('.lb__next').addEventListener('click', function () { show(idx + 1); });
      lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
      var sx = null;
      lb.addEventListener('pointerdown', function (e) { sx = e.clientX; });
      lb.addEventListener('pointerup', function (e) { if (sx === null) return; var dx = e.clientX - sx; sx = null; if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1)); });
    };
    var show = function (k) {
      idx = (k + group.length) % group.length;
      var a = group[idx], im = a.querySelector('img');
      lbImg.src = a.getAttribute('href'); lbImg.alt = im ? im.alt : '';
      lbCount.textContent = (idx + 1) + ' / ' + group.length;
    };
    var onKey = function (e) {
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowRight') show(idx + 1);
      if (e.key === 'ArrowLeft') show(idx - 1);
    };
    var open = function (a) {
      if (!lb) build();
      group = [].slice.call(d.querySelectorAll('[data-lb="' + a.getAttribute('data-lb') + '"]'));
      lastFocus = a; show(group.indexOf(a));
      lb.hidden = false; requestAnimationFrame(function () { lb.classList.add('is-on'); });
      d.documentElement.style.overflow = 'hidden';
      d.addEventListener('keydown', onKey);
      lb.querySelector('.lb__close').focus();
    };
    var close = function () {
      lb.classList.remove('is-on'); d.documentElement.style.overflow = '';
      d.removeEventListener('keydown', onKey);
      setTimeout(function () { lb.hidden = true; }, 250);
      if (lastFocus) lastFocus.focus();
    };
    lbLinks.forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); open(a); }); });
  }

  /* Cookies – meranie sa načíta iba po súhlase a iba na doméne superticket.sk */
  var KEY = 'st-consent-v1', bar = d.getElementById('cookiebar');
  function getC() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function setC(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function loadAnalytics() {
    var id = html.getAttribute('data-gtm');
    if (!id || !/(^|\.)superticket\.sk$/.test(location.hostname) || window.__stGtm) return;
    window.__stGtm = true;
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
    var s = d.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtm.js?id=' + id;
    d.head.appendChild(s);
  }
  var c = getC();
  if (c === 'all') loadAnalytics();
  else if (!c && bar) bar.hidden = false;
  if (bar) {
    bar.addEventListener('click', function (e) {
      var b = e.target.closest('[data-consent]'); if (!b) return;
      var v = b.getAttribute('data-consent'); setC(v); bar.hidden = true;
      if (v === 'all') loadAnalytics();
    });
  }
  d.querySelectorAll('[data-cookie-settings]').forEach(function (b) {
    b.addEventListener('click', function () { if (bar) { bar.hidden = false; var f = bar.querySelector('button'); if (f) f.focus(); } });
  });
})();
