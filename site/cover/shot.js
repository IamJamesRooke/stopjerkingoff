const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const [file,w,h,out] = process.argv.slice(2);
  const p = await b.newPage({viewport:{width:+w,height:+h}});
  await p.goto('file://'+require('path').resolve(__dirname,file)); await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(500);
  await p.screenshot({path:require('path').resolve(out)});
  await b.close();
})();
