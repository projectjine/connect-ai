/* stitch-global.js – handles media popup, insights AJAX, and blur‑guard CTA */
document.addEventListener('DOMContentLoaded', () => {
  // ---------- Media Popup ----------
  const gate = document.getElementById('media-gate');
  const modal = document.getElementById('media-modal');
  const closeBtn = modal?.querySelector('.close-btn');
  if (gate && modal) {
    gate.addEventListener('click', () => modal.classList.remove('hidden'));
    closeBtn?.addEventListener('click', () => modal.classList.add('hidden'));
    modal.querySelector('.modal-backdrop')?.addEventListener('click', () => modal.classList.add('hidden'));
  }

  // ---------- Insights AJAX ----------
  const grid = document.getElementById('insights-grid');
  const tabs = document.querySelectorAll('.insights-tabs button');
  const loadCategory = (slug) => {
    fetch(`/wp-json/stitch/v1/insights?category=${slug}`)
      .then(r => r.json())
      .then(renderCards)
      .catch(console.error);
  };
  const renderCards = (posts) => {
    grid.innerHTML = posts.map(p => `
      <article class="insight-card">
        <a href="${p.link}">
          <img src="${p.thumb}" alt="${p.title}" />
          <h3>${p.title}</h3>
          <p>${p.excerpt}</p>
        </a>
      </article>`).join('');
  };
  tabs.forEach(btn => {
    btn.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      btn.classList.add('active');
      loadCategory(btn.dataset.cat);
    });
  });
  if (tabs[0]) tabs[0].click();

  // ---------- Blur‑Guard CTA ----------
  if (document.body.classList.contains('stitch-blur-guard')) {
    const btn = document.createElement('button');
    btn.textContent = '전체 글 읽기';
    btn.className = 'unlock-btn';
    btn.onclick = () => window.location.href = '/membership-plans';
    const content = document.querySelector('.post-content');
    if (content) content.appendChild(btn);
  }
});
