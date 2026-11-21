/* Reading aids. Remembers the last chapter you opened, in this browser only
   (localStorage; nothing is sent anywhere), and offers "Continue reading" on the
   homepage and in the menu. Also draws a thin reading-progress bar. */
(function () {
  var KEY = "sjo-last";
  function load() {
    try { return JSON.parse(localStorage.getItem(KEY) || "null"); } catch (e) { return null; }
  }
  function save(v) {
    try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) {}
  }
  function here() {
    return (location.pathname.split("/").pop() || "index.html");
  }
  function run() {
    var meta = document.querySelector(".chapter-meta");
    var last = load();
    if (meta && meta.getAttribute("data-path") !== "introduction.html") {
      save({ p: meta.getAttribute("data-path"), t: meta.getAttribute("data-title") });
    }
    if (last && last.p && last.p !== here() && last.p !== "introduction.html") {
      var btn = document.querySelector(".hero-continue");
      if (btn) {
        btn.href = last.p;
        btn.textContent = "Continue: " + last.t;
        btn.hidden = false;
      }
      var summary = document.querySelector(".book-summary ul.summary");
      var logo = summary && summary.querySelector("li.site-logo");
      if (summary && !meta) {
        var li = document.createElement("li");
        li.className = "continue-reading";
        var a = document.createElement("a");
        a.href = last.p;
        a.textContent = "Continue: " + last.t;
        li.appendChild(a);
        summary.insertBefore(li, logo ? logo.nextSibling : summary.firstChild);
      }
    }
    // progress bar for chapter pages
    if (!meta) return;
    var bar = document.createElement("div");
    bar.className = "read-progress";
    document.body.appendChild(bar);
    var box = document.querySelector(".book-body .body-inner") || document.scrollingElement;
    function update() {
      var el = box.scrollHeight > box.clientHeight + 1 ? box : document.scrollingElement;
      var max = el.scrollHeight - el.clientHeight;
      bar.style.width = (max > 0 ? Math.min(100, (el.scrollTop / max) * 100) : 0) + "%";
    }
    box.addEventListener("scroll", update, { passive: true });
    window.addEventListener("scroll", update, { passive: true });
    update();
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", run);
  else run();
})();
