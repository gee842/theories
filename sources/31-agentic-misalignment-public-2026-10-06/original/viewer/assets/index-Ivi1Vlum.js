(function(){let e=document.createElement(`link`).relList;if(e&&e.supports&&e.supports(`modulepreload`))return;for(let e of document.querySelectorAll(`link[rel="modulepreload"]`))n(e);new MutationObserver(e=>{for(let t of e)if(t.type===`childList`)for(let e of t.addedNodes)e.tagName===`LINK`&&e.rel===`modulepreload`&&n(e)}).observe(document,{childList:!0,subtree:!0});function t(e){let t={};return e.integrity&&(t.integrity=e.integrity),e.referrerPolicy&&(t.referrerPolicy=e.referrerPolicy),e.crossOrigin===`use-credentials`?t.credentials=`include`:e.crossOrigin===`anonymous`?t.credentials=`omit`:t.credentials=`same-origin`,t}function n(e){if(e.ep)return;e.ep=!0;let n=t(e);fetch(e.href,n)}})();var e=document.querySelector(`#app`),t={manifest:null,activeId:new URLSearchParams(window.location.search).get(`t`)||`fraud`,transcript:null,query:``,activeMessageId:null,view:`target`},n={system:`Input`,user:`Input`,assistant:`Output`,tool:`Tool`},r={assistant:`Auditor`,tool:`Tool Result`};function i(e=``){return String(e).replaceAll(`&`,`&amp;`).replaceAll(`<`,`&lt;`).replaceAll(`>`,`&gt;`).replaceAll(`"`,`&quot;`).replaceAll(`'`,`&#039;`)}function a(e){return e?new Intl.DateTimeFormat(`en`,{year:`numeric`,month:`short`,day:`numeric`}).format(new Date(e)):`Unknown`}function o(e){let t=new Map;for(let n of e.annotations.user_comments){let e=t.get(n.message_id)??{comments:[],highlights:[]};e.comments.push(n),t.set(n.message_id,e)}for(let n of s(e)){let e=t.get(n.message_id)??{comments:[],highlights:[]};e.highlights.push(n),t.set(n.message_id,e)}return t}function s(e){return[...e.annotations.user_highlights??[],...e.annotations.judge_highlights??[]]}async function c(){t.manifest=await(await fetch(`/portfolio-transcript-viewer/static/manifest.json`)).json(),t.manifest.transcripts.some(e=>e.id===t.activeId&&e.href)||(t.activeId=t.manifest.transcripts.find(e=>e.href)?.id)}async function l(e){let n=t.manifest.transcripts.find(t=>t.id===e);n?.href&&(t.transcript=await(await fetch(`/portfolio-transcript-viewer/${n.href}`)).json(),t.activeId=e,t.view=`target`,t.activeMessageId=t.transcript.target_messages[0]?.id??null,window.history.replaceState(null,``,`?t=${e}`),b())}function u(e){let n=e.id===t.activeId?`active`:``,r=e.classification?.hit?`hit`:``,a=e.classification?.hit?`<span class="hit-pill">Hit</span>`:``,o=e.external_url?`External source`:`${e.classification?`${e.classification.hit?e.classification.label:`No hit`} · `:``}${e.message_count} messages · ${e.comment_count+e.highlight_count} notes`,s=`
    <span class="tab-title">${i(e.title)}${a}</span>
    <small>${i(o)}</small>
  `;return e.external_url?`
      <a class="transcript-tab external" href="${i(e.external_url)}" target="_blank" rel="noreferrer">
        ${s}
      </a>
    `:`
    <button class="transcript-tab ${n} ${r}" data-transcript="${e.id}">
      ${s}
    </button>
  `}function d(e){let t=e.filter(e=>e.classification);return t.length?`${t.filter(e=>e.classification.hit).length}/${t.length} hits`:`${e.length}`}function f(e,n,r=!1){let a=n.some(e=>e.id===t.activeId)?`open`:``,o=n.filter(e=>!e.subfolder_title||r),s=new Map;if(!r)for(let e of n.filter(e=>e.subfolder_title)){let t=e.subfolder_title;s.set(t,[...s.get(t)??[],e])}return`
    <details class="transcript-folder ${r?`nested`:``}" ${a}>
      <summary>
        <span>${i(e)}</span>
        <small>${i(d(n))}</small>
      </summary>
      <div>
        ${o.map(u).join(``)}
        ${[...s.entries()].map(([e,t])=>f(e,t,!0)).join(``)}
      </div>
    </details>
  `}function p(e){return/frequency/i.test(e.folder_title??``)}function m(e){let n=[];for(let r of t.manifest.sections??[]){if(r.id===`anchors`)continue;let i=t.manifest.transcripts.filter(t=>t.section===r.id&&e(t));i.length&&n.push({...r,transcripts:i})}return n}function h(){let e=t.manifest.transcripts.filter(e=>e.anchor),n=t.manifest.transcripts.filter(e=>e.section===`motivated-mislabelling`&&!e.anchor),r=m(e=>p(e)&&!e.anchor),i=m(e=>e.section!==`motivated-mislabelling`&&!e.anchor&&!p(e)),a=[];return(e.length||n.length)&&a.push(`
      <section class="nav-group">
        <h2>Anchors</h2>
        <div>
          ${n.length?f(`Motivated Mislabelling`,n):``}
          ${e.map(u).join(``)}
        </div>
      </section>
    `),r.length&&a.push(`
      <section class="nav-group">
        <h2>Frequency Runs</h2>
        <div>
          ${r.map(e=>f(e.title,e.transcripts)).join(``)}
        </div>
      </section>
    `),i.length&&a.push(`
      <section class="nav-group">
        <h2>Nearby Cases</h2>
        <div>
          ${i.map(e=>f(e.title,e.transcripts)).join(``)}
        </div>
      </section>
    `),a.join(``)}function g(){let e=t.transcript;return e.auditor_messages?.length?`
    <div class="view-toggle">
      <button class="view-tab ${t.view===`target`?`active`:``}" data-view="target">
        Target Messages
        <small>${e.target_messages.length}</small>
      </button>
      <button class="view-tab ${t.view===`auditor`?`active`:``}" data-view="auditor">
        Auditor Reasoning
        <small>${e.auditor_messages.length}</small>
      </button>
    </div>
  `:``}function _(){let e=t.transcript.auditor_messages??[];return e.length?e.map(e=>{let n=e.id===t.activeMessageId?`active`:``;return`
        <article class="message-card auditor-msg ${e.role} ${n}" id="message-${e.id}" data-message="${e.id}">
          <header>
            <span class="role">${r[e.role]??e.role}</span>
            <span class="message-meta">${i(e.role)} · #${e.index+1}</span>
          </header>
          <pre>${i(e.content)}</pre>
        </article>
      `}).join(``):`<div class="empty">No auditor messages match this search.</div>`}function v(){let e=t.transcript;if(t.view===`auditor`&&e.auditor_messages?.length)return _();let r=o(e),a=e.target_messages;return a.length?a.map(e=>{let a=r.get(e.id),o=e.id===t.activeMessageId?`active`:``,s=a&&(a.comments.length||a.highlights.length);return`
        <article class="message-card ${e.role} ${o}" id="message-${e.id}" data-message="${e.id}">
          <header>
            <span class="role">${n[e.role]??e.role}</span>
            <span class="message-meta">${i(e.role)} · #${e.index+1}</span>
          </header>
          <pre>${i(e.content)}</pre>
          ${s?`<div class="note-count">${a.comments.length} comments · ${a.highlights.length} highlights</div>`:``}
        </article>
      `}).join(``):`<div class="empty">No target messages match this search.</div>`}function y(e){return e?`
    <div class="classification ${e.hit?`hit`:`no-hit`}">
      <strong>${i(e.hit?`Hit: ${e.label}`:`No hit`)}</strong>
      ${e.confidence?`<span>${i(e.confidence)} confidence</span>`:``}
      ${e.summary?`<p>${i(e.summary)}</p>`:``}
    </div>
  `:``}function b(){let n=t.transcript;if(!t.manifest||!n){e.innerHTML=`<main class="loading">Loading transcripts...</main>`;return}e.innerHTML=`
    <div class="shell">
      <aside class="nav">
        <div class="brand">
          <span>Portfolio</span>
          <strong>Transcript Viewer</strong>
        </div>
        <nav>${h()}</nav>
        <p class="notice">Simulated transcripts. Public excerpts include target inputs and outputs only.</p>
      </aside>
      <main class="content">
        <header class="topbar">
          <div>
            <p class="eyebrow">${i(n.theme)}</p>
            <h1>${i(n.title)}</h1>
            <p>${i(n.subtitle)}</p>
            ${y(n.classification)}
          </div>
        </header>
        <dl class="meta-bar">
          <div><dt>Target</dt><dd>${i(n.metadata.target_model??`Unknown`)}</dd></div>
          <div><dt>Auditor</dt><dd>${i(n.metadata.auditor_model??`Unknown`)}</dd></div>
          <div><dt>Created</dt><dd>${a(n.metadata.created_at)}</dd></div>
          <div><dt>Messages</dt><dd>${n.metadata.message_count}</dd></div>
        </dl>
        <div class="banner">${i(n.notice)}</div>
        ${g()}
        <section class="messages">${v()}</section>
      </main>
    </div>
  `}e.addEventListener(`click`,e=>{let n=e.target.closest(`[data-view]`);if(n){t.view=n.dataset.view,t.activeMessageId=(t.view===`auditor`?t.transcript.auditor_messages:t.transcript.target_messages)?.[0]?.id??null,b();return}let r=e.target.closest(`[data-transcript]`);if(r){l(r.dataset.transcript);return}let i=e.target.closest(`[data-message]`);i&&(t.activeMessageId=i.dataset.message,b(),document.querySelector(`#message-${CSS.escape(t.activeMessageId)}`)?.scrollIntoView({block:`nearest`}))}),await c(),await l(t.activeId);