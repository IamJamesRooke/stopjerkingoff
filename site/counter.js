/* Shows "12,345 visitors conquering lust" in the sidebar, using GoatCounter's
   public counter (no cookies, no personal data). Needs "Allow adding visitor
   counts on your website" switched on in GoatCounter's settings; until then,
   or if the count can't load, nothing is shown. */
(function () {
  function show() {
    var el = document.getElementById("sjo-count");
    if (!el) return;
    fetch("https://stopjerkingoff.goatcounter.com/counter/TOTAL.json")
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (d) {
        var n = d.count_unique || d.count;
        if (!n) return;
        el.textContent = n + (String(n) === "1" ? " visitor" : " visitors") + " conquering lust";
        el.hidden = false;
      })
      .catch(function () {});
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", show);
  else show();
})();
