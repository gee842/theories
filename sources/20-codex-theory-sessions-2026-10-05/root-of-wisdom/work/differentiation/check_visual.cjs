const { chromium } = require('/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');
const assert = require('assert');
(async () => {
  const browser = await chromium.launch({headless: true});
  const page = await browser.newPage({viewport: {width: 780, height: 600}});
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  await page.goto('file:///Users/ren/Documents/Codex/2026-10-05/root-of-wisdom/work/differentiation/domain-preview.html');
  const frame = page.frameLocator('iframe');
  const values = () => frame.locator('.domain-nodes .tabular-nums').allTextContents();
  await frame.locator('#domain-start').selectOption('zero');
  assert.deepStrictEqual(await values(), ['0.000','0.000','0.000','0.000']);
  await frame.locator('#domain-start').selectOption('vertical');
  const vertical = await values();
  assert(vertical[0][0] === '+' && vertical[1][0] === '−' && vertical[2][0] === '−' && vertical[3][0] === '+');
  await frame.locator('#domain-time').evaluate(el => { el.value='0'; el.dispatchEvent(new Event('input', {bubbles: true})); });
  assert.deepStrictEqual(await values(), ['+0.010','−0.010','−0.010','+0.010']);
  await frame.locator('#domain-time').evaluate(el => { el.value='12'; el.dispatchEvent(new Event('input', {bubbles: true})); });
  assert.deepStrictEqual(await values(), ['+0.707','−0.707','−0.707','+0.707']);
  await frame.locator('#domain-start').selectOption('horizontal');
  assert.deepStrictEqual(await values(), ['+0.707','+0.707','−0.707','−0.707']);
  await page.setViewportSize({width: 320, height: 650});
  await page.screenshot({path: __dirname+'/domain-preview-narrow.png', fullPage: true});
  const layout = await frame.locator('#shared-process-domains').evaluate(root => {
    const svg = root.querySelector('svg');
    const bounds = svg.getBoundingClientRect();
    const text = [...svg.querySelectorAll('text')].map(el => {const r=el.getBoundingClientRect();return {text:el.textContent,left:r.left,right:r.right,top:r.top,bottom:r.bottom};});
    return {width:root.clientWidth,scrollWidth:root.scrollWidth,svgWidth:bounds.width,
      textFits:text.every(r=>r.left>=bounds.left && r.right<=bounds.right && r.top>=bounds.top && r.bottom<=bounds.bottom)};
  });
  assert(layout.scrollWidth <= layout.width);
  assert(layout.textFits);
  assert.deepStrictEqual(errors, []);
  const report = {status:'all visual checks passed', checked:['initial exact symmetry','orientation selection','analytic amplitude at t=0 and t=12','primary interactions update values','320px layout and labels','no browser script errors'], layout, errors};
  fs.writeFileSync(__dirname+'/visual-checks.json', JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report));
  await browser.close();
})();
