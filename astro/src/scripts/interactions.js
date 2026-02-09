/**
 * V4 "Dark Luxury" Interactive Effects
 * The Bitcoin Breakdown — thebitcoinbreakdown.com
 *
 * Matches the reference: design-complete.html
 * All effects respect prefers-reduced-motion: reduce.
 */

(function () {
  'use strict';

  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Canvas references (shared across effects)
  var mC = document.getElementById('matrixCanvas');
  var lC = document.getElementById('lightningCanvas');
  var bC = document.getElementById('boltCanvas');
  var tO = document.getElementById('transitionOverlay');

  // ── 1. Scroll Progress ──
  function initScrollProgress() {
    var sp = document.getElementById('scrollProgress');
    if (!sp) return;
    window.addEventListener('scroll', function () {
      var t = document.documentElement.scrollTop;
      var h = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      sp.style.width = (t / h * 100) + '%';
    }, { passive: true });
  }

  // ── 2. Scroll Reveals ──
  function initScrollReveals() {
    var reveals = document.querySelectorAll('.reveal');
    if (!reveals.length) return;

    if (prefersReducedMotion) {
      reveals.forEach(function (el) { el.classList.add('visible'); });
      return;
    }

    var rO = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) e.target.classList.add('visible');
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

    reveals.forEach(function (el) { rO.observe(el); });

    // Auto-reveal blog post content children
    document.querySelectorAll('.post-content.prose > *').forEach(function (el, i) {
      el.classList.add('reveal');
      el.style.transitionDelay = Math.min(i * 0.03, 0.3) + 's';
      rO.observe(el);
    });
  }

  // ── 3. Matrix Rain (soft, 1.5s) ──
  function initMatrixRain() {
    if (!mC || prefersReducedMotion) {
      if (mC) mC.style.display = 'none';
      return;
    }

    var mX = mC.getContext('2d');
    mC.width = innerWidth;
    mC.height = innerHeight;

    var ch = '0123456789ABCDEF₿';
    var fs = 14;
    var co = Math.floor(mC.width / fs);
    var dr = Array(co).fill(0).map(function () { return Math.random() * -10 | 0; });
    var mR = true;

    function drawM() {
      if (!mR) return;
      mX.fillStyle = 'rgba(0,0,0,0.12)';
      mX.fillRect(0, 0, mC.width, mC.height);
      mX.fillStyle = '#FFD700';
      mX.font = fs + 'px monospace';
      for (var i = 0; i < dr.length; i++) {
        if (Math.random() > 0.7) {
          mX.globalAlpha = 0.3 + Math.random() * 0.4;
          mX.fillText(ch[Math.random() * ch.length | 0], i * fs, dr[i] * fs);
        }
        if (dr[i] * fs > mC.height && Math.random() > 0.99) dr[i] = 0;
        dr[i]++;
      }
      mX.globalAlpha = 1;
      requestAnimationFrame(drawM);
    }

    drawM();
    setTimeout(function () {
      mC.classList.add('dissolved');
      setTimeout(function () { mR = false; }, 1000);
    }, 1500);
  }

  // ── 4. Static Discharge (text selection release, subtle) ──
  function initStaticDischarge() {
    if (prefersReducedMotion || !lC) return;

    var lX = lC.getContext('2d');

    document.addEventListener('mouseup', function (e) {
      var sel = window.getSelection();
      if (!sel || sel.toString().length < 2) return;

      lC.width = innerWidth;
      lC.height = innerHeight;

      var branches = 3 + Math.random() * 3 | 0;
      var fr = 0;

      function draw() {
        lX.clearRect(0, 0, lC.width, lC.height);
        if (fr > 8) return;
        var a = 1 - fr / 8;
        lX.shadowColor = 'rgba(255,215,0,' + (a * 0.6) + ')';
        lX.shadowBlur = 8;
        for (var b = 0; b < branches; b++) {
          var ang = (Math.PI * 2 / branches) * b + (Math.random() - 0.5) * 0.8;
          lX.strokeStyle = 'rgba(255,215,0,' + (a * 0.8) + ')';
          lX.lineWidth = 1.5;
          lX.beginPath();
          lX.moveTo(e.clientX, e.clientY);
          var px = e.clientX, py = e.clientY;
          for (var s = 0; s < 6; s++) {
            px += Math.cos(ang) * 20 + (Math.random() - 0.5) * 14;
            py += Math.sin(ang) * 20 + (Math.random() - 0.5) * 14;
            lX.lineTo(px, py);
          }
          lX.stroke();
        }
        lX.shadowColor = 'transparent';
        lX.shadowBlur = 0;
        fr++;
        requestAnimationFrame(draw);
      }

      draw();
    });
  }

  // ── 5. Lightning Bolt Page Transition ──
  function initLightningTransition() {
    if (prefersReducedMotion || !bC || !tO) return;

    var bX = bC.getContext('2d');

    function buildBoltPath(startX, startY, endX, endY, displacement) {
      if (displacement < 4) return [{ x: endX, y: endY }];
      var midX = (startX + endX) / 2 + (Math.random() - 0.5) * displacement;
      var midY = (startY + endY) / 2 + (Math.random() - 0.5) * displacement * 0.3;
      var left = buildBoltPath(startX, startY, midX, midY, displacement / 2);
      var right = buildBoltPath(midX, midY, endX, endY, displacement / 2);
      return left.concat(right);
    }

    function drawBolt(clickX, clickY) {
      bC.width = innerWidth;
      bC.height = innerHeight;
      bX.clearRect(0, 0, bC.width, bC.height);

      var startX = clickX + (Math.random() - 0.5) * 60;
      var startY = 0;
      var points = buildBoltPath(startX, startY, clickX, clickY, 120);
      points.unshift({ x: startX, y: startY });

      // Bright white-gold flash frame
      bX.fillStyle = 'rgba(255, 245, 200, 0.08)';
      bX.fillRect(0, 0, bC.width, bC.height);

      // Draw crisp layers — vibrant core, no fuzz
      var layers = [
        { color: 'rgba(255,215,0,0.5)', width: 4, blur: 10 },
        { color: 'rgba(255,235,140,1)', width: 1.5, blur: 3 },
        { color: 'rgba(255,255,250,1)', width: 0.8, blur: 0 }
      ];

      layers.forEach(function (layer) {
        bX.save();
        bX.strokeStyle = layer.color;
        bX.lineWidth = layer.width;
        bX.shadowColor = '#FFD700';
        bX.shadowBlur = layer.blur;
        bX.lineCap = 'round';
        bX.lineJoin = 'round';
        bX.beginPath();
        bX.moveTo(points[0].x, points[0].y);
        points.forEach(function (p) { bX.lineTo(p.x, p.y); });
        bX.stroke();
        bX.restore();
      });

      // Branch bolts (2-3 small forks off the main bolt)
      var branchCount = 2 + (Math.random() * 2 | 0);
      for (var b = 0; b < branchCount; b++) {
        var forkIdx = Math.floor(Math.random() * points.length * 0.6) + 2;
        if (forkIdx >= points.length) continue;
        var forkPt = points[forkIdx];
        var bEndX = forkPt.x + (Math.random() - 0.5) * 100;
        var bEndY = forkPt.y + 20 + Math.random() * 60;
        var branchPts = buildBoltPath(forkPt.x, forkPt.y, bEndX, bEndY, 30);
        branchPts.unshift(forkPt);
        bX.save();
        bX.strokeStyle = 'rgba(255,215,0,0.4)';
        bX.lineWidth = 2;
        bX.shadowColor = '#FFD700';
        bX.shadowBlur = 6;
        bX.lineCap = 'round';
        bX.beginPath();
        bX.moveTo(branchPts[0].x, branchPts[0].y);
        branchPts.forEach(function (p) { bX.lineTo(p.x, p.y); });
        bX.stroke();
        bX.strokeStyle = 'rgba(255,255,240,0.9)';
        bX.lineWidth = 0.5;
        bX.shadowBlur = 0;
        bX.stroke();
        bX.restore();
      }

      // Impact flash at click point — tight and bright
      var grad = bX.createRadialGradient(clickX, clickY, 0, clickX, clickY, 40);
      grad.addColorStop(0, 'rgba(255,255,250,0.7)');
      grad.addColorStop(0.4, 'rgba(255,215,0,0.25)');
      grad.addColorStop(1, 'transparent');
      bX.fillStyle = grad;
      bX.fillRect(clickX - 40, clickY - 40, 80, 80);

      // Fade out over 18 frames
      var fade = 0;
      function f() {
        bX.fillStyle = 'rgba(0,0,0,0.12)';
        bX.fillRect(0, 0, bC.width, bC.height);
        fade++;
        if (fade < 18) requestAnimationFrame(f);
        else bX.clearRect(0, 0, bC.width, bC.height);
      }
      requestAnimationFrame(f);
    }

    document.querySelectorAll('.tbb-link').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        var href = a.getAttribute('href');
        drawBolt(e.clientX, e.clientY);
        tO.classList.add('active');
        setTimeout(function () {
          tO.classList.remove('active');
          if (href && href !== '#') {
            window.location.href = href;
          }
        }, 800);
      });
    });
  }

  // ── 6. Logo Easter Egg (3s hover triggers glitch) ──
  function initLogoEasterEgg() {
    if (prefersReducedMotion) return;

    var logos = document.querySelectorAll('.logo');
    if (!logos.length) return;

    logos.forEach(function (logo) {
      var lt;
      logo.addEventListener('mouseenter', function () {
        lt = setTimeout(function () {
          logo.classList.add('glitching');
          setTimeout(function () { logo.classList.remove('glitching'); }, 500);
        }, 1000);
      });
      logo.addEventListener('mouseleave', function () {
        clearTimeout(lt);
      });
    });
  }

  // ── 7. Hero Hash (random hex, 80 chars with spaces every 8, changes every 4s) ──
  function initHeroHash() {
    var hH = document.getElementById('heroHash');
    if (!hH) return;

    function gH(n) {
      var h = '0123456789abcdef';
      var r = '';
      for (var i = 0; i < n; i++) {
        r += h[Math.random() * 16 | 0];
        if (i % 8 === 7 && i < n - 1) r += ' ';
      }
      return r;
    }

    hH.textContent = '0x' + gH(80);
    setInterval(function () { hH.textContent = '0x' + gH(80); }, 4000);
  }

  // ── 8. Card Title Scramble (on hover, snap-back on leave) ──
  function initCardScramble() {
    if (prefersReducedMotion) return;

    var sC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&';

    document.querySelectorAll('.scramble-text').forEach(function (el) {
      var card = el.closest('.article-card');
      if (!card) return;
      var o = el.dataset.original || el.textContent;
      var iv;

      card.addEventListener('mouseenter', function () {
        var it = 0;
        clearInterval(iv);
        iv = setInterval(function () {
          el.textContent = o.split('').map(function (c, i) {
            if (c === ' ') return ' ';
            if (i < it) return o[i];
            return sC[Math.random() * sC.length | 0];
          }).join('');
          it += 1.5;
          if (it >= o.length) {
            clearInterval(iv);
            el.textContent = o;
          }
        }, 30);
      });

      card.addEventListener('mouseleave', function () {
        clearInterval(iv);
        el.textContent = o;
      });
    });
  }

  // ── 9. Typing Section Headers (35ms per char on scroll) ──
  function initTypingHeaders() {
    if (prefersReducedMotion) return;

    var headers = document.querySelectorAll('.section-label');
    if (!headers.length) return;

    headers.forEach(function (el) {
      if (!el.dataset.text) {
        el.dataset.text = el.textContent;
        el.textContent = '\u200B';
      }
    });

    var tObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && !e.target.dataset.typed) {
          e.target.dataset.typed = '1';
          var t = e.target.dataset.text;
          var i = 0;
          e.target.textContent = '';
          var iv = setInterval(function () {
            e.target.textContent = t.slice(0, i + 1);
            i++;
            if (i >= t.length) clearInterval(iv);
          }, 35);
        }
      });
    }, { threshold: 0.5 });

    headers.forEach(function (el) { tObs.observe(el); });
  }

  // ── 10. Count-Up Statistics (1500ms, cubic ease-out) ──
  function initCountUp() {
    var stats = document.querySelectorAll('.count-up');
    if (!stats.length) return;

    var cObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && !e.target.dataset.counted) {
          e.target.dataset.counted = '1';
          var t = +e.target.dataset.target;
          var s = e.target.dataset.suffix || '';
          var d = 1500;
          var st = performance.now();

          function step(ts) {
            var p = Math.min((ts - st) / d, 1);
            var ease = 1 - Math.pow(1 - p, 3);
            e.target.textContent = Math.floor(ease * t).toLocaleString() + s;
            if (p < 1) requestAnimationFrame(step);
            else e.target.textContent = t.toLocaleString() + s;
          }

          requestAnimationFrame(step);
        }
      });
    }, { threshold: 0.5 });

    stats.forEach(function (el) { cObs.observe(el); });
  }

  // ── 11. Pull Quote Compile (observe [data-compile], read data-final) ──
  function initPullQuoteCompile() {
    if (prefersReducedMotion) return;

    var gibChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,;:!? ';

    var pqObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && !e.target.dataset.compiled) {
          e.target.dataset.compiled = '1';
          var textEl = e.target.querySelector('.pull-quote-text');
          var final_text = e.target.dataset.final;
          if (!textEl || !final_text) return;

          var fr = 0;
          var iv = setInterval(function () {
            textEl.textContent = final_text.split('').map(function (c, i) {
              if (c === ' ') return ' ';
              if (i < fr) return final_text[i];
              return gibChars[Math.random() * gibChars.length | 0];
            }).join('');
            fr += 2;
            if (fr >= final_text.length) {
              clearInterval(iv);
              textEl.textContent = final_text;
            }
          }, 25);
        }
      });
    }, { threshold: 0.5 });

    document.querySelectorAll('[data-compile]').forEach(function (el) { pqObs.observe(el); });
  }

  // ── 12. Footnote Flash (add + remove class after 600ms) ──
  function initFootnoteFlash() {
    if (prefersReducedMotion) return;

    var fObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && !e.target.dataset.flashed) {
          e.target.dataset.flashed = '1';
          e.target.classList.add('flash');
          setTimeout(function () { e.target.classList.remove('flash'); }, 600);
        }
      });
    }, { threshold: 1 });

    document.querySelectorAll('.fn-ref').forEach(function (el) { fObs.observe(el); });
  }

  // ── 13. Divider Decrypt (threshold: 0.5) ──
  function initDividers() {
    var dividers = document.querySelectorAll('.divider');
    if (!dividers.length) return;

    if (prefersReducedMotion) {
      dividers.forEach(function (el) { el.classList.add('visible'); });
      return;
    }

    var dObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) e.target.classList.add('visible');
      });
    }, { threshold: 0.5 });

    dividers.forEach(function (el) { dObs.observe(el); });
  }

  // ── 14. Divider Sparks (one random spark globally every 3-7s) ──
  function initDividerSparks() {
    if (prefersReducedMotion) return;

    function rSpark() {
      var ss = document.querySelectorAll('.divider-spark');
      var s = ss[Math.random() * ss.length | 0];
      if (!s) return;
      s.style.left = Math.random() * s.parentElement.offsetWidth + 'px';
      s.style.opacity = '1';
      setTimeout(function () { s.style.opacity = '0'; }, 150);
    }

    setInterval(rSpark, 3000 + Math.random() * 4000);
  }

  // ── 15. Encryption Bars (rAF, quartic ease-out, percentage counter) ──
  function initEncryptionBars() {
    if (prefersReducedMotion) return;

    function animateBar(fillEl, percentEl) {
      if (!fillEl) return;
      var targetWidth = parseFloat(fillEl.style.width) || 100;
      fillEl.style.width = '0%';
      var d = 3000;
      var st = performance.now();

      function step(ts) {
        var pr = Math.min((ts - st) / d, 1);
        var ease = 1 - Math.pow(1 - pr, 4);
        fillEl.style.width = ease * targetWidth + '%';
        if (percentEl) percentEl.textContent = Math.round(ease * targetWidth) + '%';
        if (pr < 1) requestAnimationFrame(step);
      }

      requestAnimationFrame(step);
    }

    var eObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting && !e.target.dataset.animated) {
          e.target.dataset.animated = '1';
          var fill = e.target.querySelector('.encrypt-bar-fill');
          var label = e.target.parentElement
            ? e.target.parentElement.querySelector('.encrypt-bar-label')
            : null;
          var percentEl = label ? label.querySelector('span:last-child') : null;
          animateBar(fill, percentEl);
        }
      });
    }, { threshold: 0.5 });

    document.querySelectorAll('.encrypt-bar').forEach(function (el) { eObs.observe(el); });
  }

  // ── 16. Window Resize Handler ──
  function initResize() {
    window.addEventListener('resize', function () {
      if (lC) { lC.width = innerWidth; lC.height = innerHeight; }
      if (mC) { mC.width = innerWidth; mC.height = innerHeight; }
      if (bC) { bC.width = innerWidth; bC.height = innerHeight; }
    });
  }

  // ── INIT ──
  document.addEventListener('DOMContentLoaded', function () {
    // Always active
    initScrollProgress();
    initScrollReveals();
    initDividers();
    initCountUp();
    initEncryptionBars();
    initFootnoteFlash();
    initResize();

    // Animation-dependent (skipped if reduced motion)
    initMatrixRain();
    initHeroHash();
    initCardScramble();
    initTypingHeaders();
    initPullQuoteCompile();
    initDividerSparks();
    initLogoEasterEgg();
    initLightningTransition();
    initStaticDischarge();
  });
})();
