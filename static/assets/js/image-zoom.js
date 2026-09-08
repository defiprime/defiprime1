(function () {
  if (typeof document === 'undefined') return;

  var STYLE = [
    '.dp-zoom-img{cursor:zoom-in;transition:opacity .15s ease}',
    '.dp-zoom-img:hover{opacity:.92}',
    '.dp-zoom-overlay{position:fixed;inset:0;background:rgba(20,20,40,.92);display:flex;align-items:center;justify-content:center;z-index:9999;padding:2vh 2vw;cursor:zoom-out;opacity:0;transition:opacity .18s ease;backdrop-filter:blur(4px)}',
    '.dp-zoom-overlay.dp-open{opacity:1}',
    '.dp-zoom-overlay img{max-width:100%;max-height:100%;width:auto;height:auto;box-shadow:0 12px 60px rgba(0,0,0,.5);border-radius:4px;background:#fff}',
    '.dp-zoom-close{position:absolute;top:18px;right:22px;color:#fff;font:600 28px/1 system-ui,sans-serif;background:none;border:0;cursor:pointer;opacity:.85;padding:4px 10px}',
    '.dp-zoom-close:hover{opacity:1}',
    '@media (max-width:600px){.dp-zoom-overlay{padding:1vh 1vw}}'
  ].join('');

  var styleEl = document.createElement('style');
  styleEl.appendChild(document.createTextNode(STYLE));
  document.head.appendChild(styleEl);

  function isZoomable(img) {
    if (!img || img.tagName !== 'IMG') return false;
    if (img.closest('a')) return false;
    if (img.closest('.feature, header, .header, .author-block, .latest-grid, .post-tags')) return false;
    if (!img.closest('article.article--post')) return false;
    return true;
  }

  function markImages() {
    var imgs = document.querySelectorAll('article.article--post img');
    for (var i = 0; i < imgs.length; i++) {
      if (isZoomable(imgs[i])) imgs[i].classList.add('dp-zoom-img');
    }
  }

  var overlay = null;
  function open(src, alt) {
    if (overlay) close();
    overlay = document.createElement('div');
    overlay.className = 'dp-zoom-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-label', 'Zoomed image');
    overlay.innerHTML = '<button class="dp-zoom-close" aria-label="Close zoom">×</button>';
    var img = document.createElement('img');
    img.src = src;
    if (alt) img.alt = alt;
    overlay.appendChild(img);
    document.body.appendChild(overlay);
    document.body.style.overflow = 'hidden';
    requestAnimationFrame(function () { overlay.classList.add('dp-open'); });
    overlay.addEventListener('click', close);
  }

  function close() {
    if (!overlay) return;
    var node = overlay;
    overlay = null;
    document.body.style.overflow = '';
    node.classList.remove('dp-open');
    setTimeout(function () { if (node.parentNode) node.parentNode.removeChild(node); }, 180);
  }

  document.addEventListener('click', function (e) {
    var t = e.target;
    if (t && t.tagName === 'IMG' && isZoomable(t)) {
      e.preventDefault();
      var src = t.currentSrc || t.src || t.getAttribute('data-src');
      open(src, t.alt);
    }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') close();
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', markImages);
  } else {
    markImages();
  }
})();
