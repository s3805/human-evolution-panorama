import re

def update_html():
    with open('人类演化全景图.html', 'r', encoding='utf-8') as f:
        content = f.read()

    original_length = len(content)

    # 1. Add font css link in head
    head_link_target = "<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🧬</text></svg>\">"
    head_link_replacement = head_link_target + "\n<link rel=\"stylesheet\" href=\"fonts/phosphor-duotone.css\">"
    assert head_link_target in content, "head_link_target not found"
    content = content.replace(head_link_target, head_link_replacement, 1)

    # 2. Add .ph-duotone helper style in CSS
    style_target = "/* ============ 设计令牌 ============ */"
    style_replacement = """/* Phosphor Duotone Icon Helper */
.ph-duotone{display:inline-block;vertical-align:-0.12em;font-style:normal;line-height:1}
.ph-duotone::before,.ph-duotone::after{font-family:'Phosphor-Duotone'!important}

/* ============ 设计令牌 ============ */"""
    assert style_target in content, "style_target not found"
    content = content.replace(style_target, style_replacement, 1)

    # 3. Nav audio pill icon
    nav_audio_target = '<span class="nav-audio-ico">🎧</span>'
    nav_audio_replacement = '<span class="nav-audio-ico"><i class="ph-duotone ph-headphones"></i></span>'
    assert nav_audio_target in content, "nav_audio_target not found"
    content = content.replace(nav_audio_target, nav_audio_replacement, 1)

    # 4. Chapter 1 Key points (kp-grid)
    kp_target = """  <div class="kp-grid">
    <div class="kp reveal" style="--c:var(--cyan)"><span class="ico">🌿</span>
      <h4>多物种共存是常态</h4>
      <p>约 300 万年前的东非，至少有 4 个不同人族支系在同一片土地上活动（早期人属、傍人属、南方古猿属多个种）。2025 年发表于《自然》的两项研究进一步确认了这一点。</p></div>
    <div class="kp reveal" style="--c:var(--violet)"><span class="ico">🔥</span>
      <h4>直立行走早于大脑</h4>
      <p>直立行走在 700 万年前就已出现（2026 年 1 月《科学进展》为乍得沙赫人提供了迄今最强证据），而脑容量的爆发要等到 200 万年前人属登场——足足晚了 500 万年。</p></div>
    <div class="kp reveal" style="--c:var(--amber)"><span class="ico">🧬</span>
      <h4>我们是"混血"的产物</h4>
      <p>非洲以外的现代人基因组中约有 1.8%–2.6% 来自尼安德特人；大洋洲与东亚人群还携带 0.2%–6% 的丹尼索瓦人基因。人类的故事里，"融合"和"替代"同样重要。</p></div>
    <div class="kp reveal" style="--c:var(--emerald)"><span class="ico">🌏</span>
      <h4>东亚不是演化的"边缘"</h4>
      <p>2026 年 2 月，中国科学院古脊椎动物与古人类研究所在《自然》发表成果，系统论证了过去 200 万年间东亚在人属演化中扮演的核心角色——多谱系共存、连续演化、附带杂交。</p></div>
    <div class="kp reveal" style="--c:var(--rose)"><span class="ico">🏝️</span>
      <h4>岛屿会造出"霍比特人"</h4>
      <p>在弗洛勒斯岛和吕宋岛，孤立环境让人族发生"岛屿矮化"：佛罗勒斯人身高仅约 1.06 米、脑容量约 420 毫升，却存活到距今约 5 万年前——与我们同时代。</p></div>
    <div class="kp reveal" style="--c:var(--blue)"><span class="ico">🧑‍🤝‍🧑</span>
      <h4>全人类同属一个物种</h4>
      <p>现代遗传学证实：所有活着的人都属智人种，彼此间不存在生殖隔离，基因组相似度 99.9%。人群之间的外形差异只是对局地环境的适应性表型，由极少数基因位点控制。</p></div>
  </div>"""

    kp_replacement = """  <div class="kp-grid">
    <div class="kp reveal" style="--c:var(--cyan)"><span class="ico"><i class="ph-duotone ph-plant" style="color:var(--cyan)"></i></span>
      <h4>多物种共存是常态</h4>
      <p>约 300 万年前的东非，至少有 4 个不同人族支系在同一片土地上活动（早期人属、傍人属、南方古猿属多个种）。2025 年发表于《自然》的两项研究进一步确认了这一点。</p></div>
    <div class="kp reveal" style="--c:var(--violet)"><span class="ico"><i class="ph-duotone ph-footprints" style="color:var(--violet)"></i></span>
      <h4>直立行走早于大脑</h4>
      <p>直立行走在 700 万年前就已出现（2026 年 1 月《科学进展》为乍得沙赫人提供了迄今最强证据），而脑容量的爆发要等到 200 万年前人属登场——足足晚了 500 万年。</p></div>
    <div class="kp reveal" style="--c:var(--amber)"><span class="ico"><i class="ph-duotone ph-dna" style="color:var(--amber)"></i></span>
      <h4>我们是"混血"的产物</h4>
      <p>非洲以外的现代人基因组中约有 1.8%–2.6% 来自尼安德特人；大洋洲与东亚人群还携带 0.2%–6% 的丹尼索瓦人基因。人类的故事里，"融合"和"替代"同样重要。</p></div>
    <div class="kp reveal" style="--c:var(--emerald)"><span class="ico"><i class="ph-duotone ph-globe-hemisphere-east" style="color:var(--emerald)"></i></span>
      <h4>东亚不是演化的"边缘"</h4>
      <p>2026 年 2 月，中国科学院古脊椎动物与古人类研究所在《自然》发表成果，系统论证了过去 200 万年间东亚在人属演化中扮演的核心角色——多谱系共存、连续演化、附带杂交。</p></div>
    <div class="kp reveal" style="--c:var(--rose)"><span class="ico"><i class="ph-duotone ph-mountains" style="color:var(--rose)"></i></span>
      <h4>岛屿会造出"霍比特人"</h4>
      <p>在弗洛勒斯岛和吕宋岛，孤立环境让人族发生"岛屿矮化"：佛罗勒斯人身高仅约 1.06 米、脑容量约 420 毫升，却存活到距今约 5 万年前——与我们同时代。</p></div>
    <div class="kp reveal" style="--c:var(--blue)"><span class="ico"><i class="ph-duotone ph-users" style="color:var(--blue)"></i></span>
      <h4>全人类同属一个物种</h4>
      <p>现代遗传学证实：所有活着的人都属智人种，彼此间不存在生殖隔离，基因组相似度 99.9%。人群之间的外形差异只是对局地环境的适应性表型，由极少数基因位点控制。</p></div>
  </div>"""
    assert kp_target in content, "kp_target not found"
    content = content.replace(kp_target, kp_replacement, 1)

    # 5. Clarifying concepts title
    c1_title = '<h4 style="font-size:1.05rem;margin-bottom:16px">📐 先厘清几个容易混淆的概念</h4>'
    c1_title_repl = '<h4 style="font-size:1.05rem;margin-bottom:16px"><i class="ph-duotone ph-ruler" style="color:var(--cyan);margin-right:6px"></i>先厘清几个容易混淆的概念</h4>'
    assert c1_title in content, "c1_title not found"
    content = content.replace(c1_title, c1_title_repl, 1)

    # 6. Coexistence lab
    lab_title = '<h4 style="font-size:1.05rem;margin-bottom:4px">🧪 共存实验室</h4>'
    lab_title_repl = '<h4 style="font-size:1.05rem;margin-bottom:4px"><i class="ph-duotone ph-flask" style="color:var(--cyan);margin-right:6px"></i>共存实验室</h4>'
    assert lab_title in content, "lab_title not found"
    content = content.replace(lab_title, lab_title_repl, 1)

    lab_btn = '<button class="lab-btn" id="cmpRnd" type="button">🎲 随机一对</button>'
    lab_btn_repl = '<button class="lab-btn" id="cmpRnd" type="button"><i class="ph-duotone ph-shuffle" style="margin-right:4px"></i>随机一对</button>'
    assert lab_btn in content, "lab_btn not found"
    content = content.replace(lab_btn, lab_btn_repl, 1)

    # 7. Chapter 3 explanation
    c3_title = '<h4 style="font-size:1.02rem;margin-bottom:8px">🧭 这张图在说什么</h4>'
    c3_title_repl = '<h4 style="font-size:1.02rem;margin-bottom:8px"><i class="ph-duotone ph-compass" style="color:var(--cyan);margin-right:6px"></i>这张图在说什么</h4>'
    assert c3_title in content, "c3_title not found"
    content = content.replace(c3_title, c3_title_repl, 1)

    # 8. Brain facts
    bf_target = """    <div class="brain-facts">
      <div class="bf reveal" style="--c:var(--cyan)">
        <h5>🥩 昂贵的组织假说</h5>
        <p>大脑只占体重 2%，却消耗 20% 的能量（婴儿高达 60%）。学界主流解释是：肉食增加 + 烹饪 + 用火，
          让肠道缩短、能量重新分配给大脑。直立人掌握用火后，脑容量的爬升曲线明显变陡。</p>
      </div>
      <div class="bf reveal" style="--c:var(--violet)">
        <h5>📉 近 1 万年反而变小了</h5>
        <p>智人的平均脑容量在约 3 万年前达到峰值（约 1500 毫升），此后下降了约 10%，现代平均约 1350 毫升。
          主流解释包括体型变小、能量预算优化，以及社会分工带来的<strong>群体层面</strong>智能。</p>
      </div>
      <div class="bf reveal" style="--c:var(--amber)">
        <h5>🏝️ 岛屿法则：反向演化</h5>
        <p>佛罗勒斯人（约 420 毫升）与吕宋人展示了"岛屿矮化"：资源有限、缺乏天敌的孤立环境中，
          大型动物变小、小型动物变大。它们的脑虽然小，却制作工具、猎捕剑齿象，行为复杂程度远超体积暗示。</p>
      </div>
      <div class="bf reveal" style="--c:var(--emerald)">
        <h5>🧠 结构比体积更重要</h5>
        <p>尼安德特人的脑容量（平均约 1450 毫升）比现代人更大，但顶叶与小脑的比例不同：
          现代人更发达的是与<b>社会认知、语言、长程规划</b>相关的区域。体积只是粗糙的代理指标。</p>
      </div>
    </div>"""

    bf_repl = """    <div class="brain-facts">
      <div class="bf reveal" style="--c:var(--cyan)">
        <h5><i class="ph-duotone ph-knife" style="color:var(--cyan);margin-right:6px"></i>昂贵的组织假说</h5>
        <p>大脑只占体重 2%，却消耗 20% 的能量（婴儿高达 60%）。学界主流解释是：肉食增加 + 烹饪 + 用火，
          让肠道缩短、能量重新分配给大脑。直立人掌握用火后，脑容量的爬升曲线明显变陡。</p>
      </div>
      <div class="bf reveal" style="--c:var(--violet)">
        <h5><i class="ph-duotone ph-chart-line-down" style="color:var(--violet);margin-right:6px"></i>近 1 万年反而变小了</h5>
        <p>智人的平均脑容量在约 3 万年前达到峰值（约 1500 毫升），此后下降了约 10%，现代平均约 1350 毫升。
          主流解释包括体型变小、能量预算优化，以及社会分工带来的<strong>群体层面</strong>智能。</p>
      </div>
      <div class="bf reveal" style="--c:var(--amber)">
        <h5><i class="ph-duotone ph-island" style="color:var(--amber);margin-right:6px"></i>岛屿法则：反向演化</h5>
        <p>佛罗勒斯人（约 420 毫升）与吕宋人展示了"岛屿矮化"：资源有限、缺乏天敌的孤立环境中，
          大型动物变小、小型动物变大。它们的脑虽然小，却制作工具、猎捕剑齿象，行为复杂程度远超体积暗示。</p>
      </div>
      <div class="bf reveal" style="--c:var(--emerald)">
        <h5><i class="ph-duotone ph-brain" style="color:var(--emerald);margin-right:6px"></i>结构比体积更重要</h5>
        <p>尼安德特人的脑容量（平均约 1450 毫升）比现代人更大，但顶叶与小脑的比例不同：
          现代人更发达的是与<b>社会认知、语言、长程规划</b>相关的区域。体积只是粗糙的代理指标。</p>
      </div>
    </div>"""
    assert bf_target in content, "bf_target not found"
    content = content.replace(bf_target, bf_repl, 1)

    # 9. Chapter 5 migration globe hint & static milestones
    mouse_hint = '<span class="ml" style="margin-left:auto;color:var(--tx3)">🖱️ 拖动地球可自由旋转</span>'
    mouse_hint_repl = '<span class="ml" style="margin-left:auto;color:var(--tx3)"><i class="ph-duotone ph-mouse" style="margin-right:4px"></i>拖动地球可自由旋转</span>'
    assert mouse_hint in content, "mouse_hint not found"
    content = content.replace(mouse_hint, mouse_hint_repl, 1)

    c5_miles = """  <div class="mile-grid">
    <div class="mile reveal"><span class="mi">🦶</span><div><h5>德马尼西人</h5><span>约 180 万年前 · 格鲁吉亚</span>
      <p>非洲以外最早的确凿人属化石，脑容量仅约 600–780 毫升，证明"走出非洲"发生在大脑变大之前。</p></div></div>
    <div class="mile reveal"><span class="mi">🔥</span><div><h5>用火与狩猎</h5><span>约 100 万–40 万年前</span>
      <p>德国舍宁根出土约 30 万年前的木质标枪，证明系统化狩猎大型猎物；用火让高纬度地区得以殖民。</p></div></div>
    <div class="mile reveal"><span class="mi">⛵</span><div><h5>跨越海洋</h5><span>约 65 万–5 万年前</span>
      <p>弗洛勒斯岛、吕宋岛的化石证明，某些人族在极早年代就具备了跨越深海海峡的能力（可能是漂流或简易筏）。</p></div></div>
    <div class="mile reveal"><span class="mi">🎨</span><div><h5>象征性思维爆发</h5><span>约 7 万–4 万年前</span>
      <p>南非布隆伯斯洞窟的刻纹赭石（约 7.3 万年）、欧洲洞穴壁画（约 4 万年）、最早的骨笛与雕塑，标志着"现代行为"的出现。</p></div></div>
    <div class="mile reveal"><span class="mi">🌾</span><div><h5>新石器革命</h5><span>约 1.2 万年前</span>
      <p>从新月沃地、中国长江黄河流域、中美洲等多个中心独立起源的农业，让人类的种群规模呈指数级增长。</p></div></div>
    <div class="mile reveal"><span class="mi">🗿</span><div><h5>全球殖民完成</h5><span>约 1 万年前 – 近代</span>
      <p>从太平洋岛屿到北极圈，智人成为唯一遍布全球的人属物种——上一次有多个人属共存，还是 4 万年前的事。</p></div></div>
  </div>"""

    c5_miles_repl = """  <div class="mile-grid">
    <div class="mile reveal"><span class="mi"><i class="ph-duotone ph-footprints" style="color:#38bdf8"></i></span><div><h5>德马尼西人</h5><span>约 180 万年前 · 格鲁吉亚</span>
      <p>非洲以外最早的确凿人属化石，脑容量仅约 600–780 毫升，证明"走出非洲"发生在大脑变大之前。</p></div></div>
    <div class="mile reveal"><span class="mi"><i class="ph-duotone ph-fire" style="color:#f97316"></i></span><div><h5>用火与狩猎</h5><span>约 100 万–40 万年前</span>
      <p>德国舍宁根出土约 30 万年前的木质标枪，证明系统化狩猎大型猎物；用火让高纬度地区得以殖民。</p></div></div>
    <div class="mile reveal"><span class="mi"><i class="ph-duotone ph-boat" style="color:#38bdf8"></i></span><div><h5>跨越海洋</h5><span>约 65 万–5 万年前</span>
      <p>弗洛勒斯岛、吕宋岛的化石证明，某些人族在极早年代就具备了跨越深海海峡的能力（可能是漂流或简易筏）。</p></div></div>
    <div class="mile reveal"><span class="mi"><i class="ph-duotone ph-palette" style="color:#fb7185"></i></span><div><h5>象征性思维爆发</h5><span>约 7 万–4 万年前</span>
      <p>南非布隆伯斯洞窟的刻纹赭石（约 7.3 万年）、欧洲洞穴壁画（约 4 万年）、最早的骨笛与雕塑，标志着"现代行为"的出现。</p></div></div>
    <div class="mile reveal"><span class="mi"><i class="ph-duotone ph-grains" style="color:#facc15"></i></span><div><h5>新石器革命</h5><span>约 1.2 万年前</span>
      <p>从新月沃地、中国长江黄河流域、中美洲等多个中心独立起源的农业，让人类的种群规模呈指数级增长。</p></div></div>
    <div class="mile reveal"><span class="mi"><i class="ph-duotone ph-globe-hemisphere-west" style="color:#34d399"></i></span><div><h5>全球殖民完成</h5><span>约 1 万年前 – 近代</span>
      <p>从太平洋岛屿到北极圈，智人成为唯一遍布全球的人属物种——上一次有多个人属共存，还是 4 万年前的事。</p></div></div>
  </div>"""
    assert c5_miles in content, "c5_miles not found"
    content = content.replace(c5_miles, c5_miles_repl, 1)

    # 10. Chapter 6
    c6_gift = '<h4 style="font-size:1.05rem;margin-bottom:6px">🎁 它们留给我们的"礼物"：适应性渗入</h4>'
    c6_gift_repl = '<h4 style="font-size:1.05rem;margin-bottom:6px"><i class="ph-duotone ph-gift" style="color:var(--amber);margin-right:6px"></i>它们留给我们的"礼物"：适应性渗入</h4>'
    assert c6_gift in content, "c6_gift not found"
    content = content.replace(c6_gift, c6_gift_repl, 1)

    dtp_ico = '<span class="dtp-ico">🧬</span>'
    dtp_ico_repl = '<span class="dtp-ico"><i class="ph-duotone ph-dna" style="color:#f43f5e"></i></span>'
    assert dtp_ico in content, "dtp_ico not found"
    content = content.replace(dtp_ico, dtp_ico_repl, 1)

    dtp_hint = '<div class="dtp-hint">💡 探索提示：'
    dtp_hint_repl = '<div class="dtp-hint"><i class="ph-duotone ph-lightbulb" style="color:var(--amber);margin-right:5px"></i>探索提示：'
    assert dtp_hint in content, "dtp_hint not found"
    content = content.replace(dtp_hint, dtp_hint_repl, 1)

    # 11. Chapter 7 & 8 titles & golden spike cards
    c7_turn = '<h4 style="font-size:1.06rem;margin:38px 0 4px" class="reveal">🔑 关键转折点</h4>'
    c7_turn_repl = '<h4 style="font-size:1.06rem;margin:38px 0 4px" class="reveal"><i class="ph-duotone ph-key" style="color:var(--amber);margin-right:6px"></i>关键转折点</h4>'
    assert c7_turn in content, "c7_turn not found"
    content = content.replace(c7_turn, c7_turn_repl, 1)

    c7_pop = '<h4 style="font-size:1.05rem">📈 世界人口：1.2 万年前 → 2100 年</h4>'
    c7_pop_repl = '<h4 style="font-size:1.05rem"><i class="ph-duotone ph-chart-line-up" style="color:var(--rose);margin-right:6px"></i>世界人口：1.2 万年前 → 2100 年</h4>'
    assert c7_pop in content, "c7_pop not found"
    content = content.replace(c7_pop, c7_pop_repl, 1)

    c7_time = '<h4 style="font-size:1.02rem;margin-bottom:4px">⏱️ 每增加 10 亿人，用了多久</h4>'
    c7_time_repl = '<h4 style="font-size:1.02rem;margin-bottom:4px"><i class="ph-duotone ph-timer" style="color:var(--cyan);margin-right:6px"></i>每增加 10 亿人，用了多久</h4>'
    assert c7_time in content, "c7_time not found"
    content = content.replace(c7_time, c7_time_repl, 1)

    c7_rate = '<h4 style="font-size:1.02rem;margin-bottom:4px">🌡️ 三条关键增长率</h4>'
    c7_rate_repl = '<h4 style="font-size:1.02rem;margin-bottom:4px"><i class="ph-duotone ph-thermometer" style="color:var(--amber);margin-right:6px"></i>三条关键增长率</h4>'
    assert c7_rate in content, "c7_rate not found"
    content = content.replace(c7_rate, c7_rate_repl, 1)

    pin_target = """      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
        <span style="font-size:1.5rem">📌</span>
        <h4 style="font-size:1.05rem">金钉子方案：克劳福德湖 1952</h4>
      </div>"""
    pin_repl = """      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
        <span style="font-size:1.5rem;line-height:1"><i class="ph-duotone ph-push-pin" style="color:var(--amber)"></i></span>
        <h4 style="font-size:1.05rem">金钉子方案：克劳福德湖 1952</h4>
      </div>"""
    assert pin_target in content, "pin_target not found"
    content = content.replace(pin_target, pin_repl, 1)

    vote_target = """      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
        <span style="font-size:1.5rem">🗳️</span>
        <h4 style="font-size:1.05rem">2024 年 3 月：12 比 4，被否决</h4>
      </div>"""
    vote_repl = """      <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
        <span style="font-size:1.5rem;line-height:1"><i class="ph-duotone ph-x-circle" style="color:var(--rose)"></i></span>
        <h4 style="font-size:1.05rem">2024 年 3 月：12 比 4，被否决</h4>
      </div>"""
    assert vote_target in content, "vote_target not found"
    content = content.replace(vote_target, vote_repl, 1)

    c8b_start = '<h4 style="font-size:1.06rem;margin:32px 0 4px" class="reveal">🕰️ 起点之争：四个候选时刻</h4>'
    c8b_start_repl = '<h4 style="font-size:1.06rem;margin:32px 0 4px" class="reveal"><i class="ph-duotone ph-clock" style="color:var(--cyan);margin-right:6px"></i>起点之争：四个候选时刻</h4>'
    assert c8b_start in content, "c8b_start not found"
    content = content.replace(c8b_start, c8b_start_repl, 1)

    c8b_accel = '<h4 style="font-size:1.06rem;margin:38px 0 4px" class="reveal">📊 大加速：1750 → 今天</h4>'
    c8b_accel_repl = '<h4 style="font-size:1.06rem;margin:38px 0 4px" class="reveal"><i class="ph-duotone ph-chart-bar" style="color:var(--violet);margin-right:6px"></i>大加速：1750 → 今天</h4>'
    assert c8b_accel in content, "c8b_accel not found"
    content = content.replace(c8b_accel, c8b_accel_repl, 1)

    c9_dna = '<h4 style="font-size:1.02rem">🧬 人类遗传变异的分布</h4>'
    c9_dna_repl = '<h4 style="font-size:1.02rem"><i class="ph-duotone ph-dna" style="color:var(--cyan);margin-right:6px"></i>人类遗传变异的分布</h4>'
    assert c9_dna in content, "c9_dna not found"
    content = content.replace(c9_dna, c9_dna_repl, 1)

    c9_map = '<h4 style="font-size:1.02rem;margin-bottom:10px">📍 多样性的起源：奠基者效应</h4>'
    c9_map_repl = '<h4 style="font-size:1.02rem;margin-bottom:10px"><i class="ph-duotone ph-map-pin" style="color:var(--amber);margin-right:6px"></i>多样性的起源：奠基者效应</h4>'
    assert c9_map in content, "c9_map not found"
    content = content.replace(c9_map, c9_map_repl, 1)

    c10_books = '<h4 style="font-size:1.02rem;margin-bottom:12px">📚 主要资料来源</h4>'
    c10_books_repl = '<h4 style="font-size:1.02rem;margin-bottom:12px"><i class="ph-duotone ph-books" style="color:var(--emerald);margin-right:6px"></i>主要资料来源</h4>'
    assert c10_books in content, "c10_books not found"
    content = content.replace(c10_books, c10_books_repl, 1)

    fg_dna = '<div class="fg">🧬</div>'
    fg_dna_repl = '<div class="fg"><i class="ph-duotone ph-dna"></i></div>'
    assert fg_dna in content, "fg_dna not found"
    content = content.replace(fg_dna, fg_dna_repl, 1)

    # 12. Floating & Sound Player Controls
    totop_target = '<button id="toTop" aria-label="返回顶部" title="返回顶部">↑</button>'
    totop_repl = '<button id="toTop" aria-label="返回顶部" title="返回顶部"><i class="ph-duotone ph-arrow-up"></i></button>'
    assert totop_target in content, "totop_target not found"
    content = content.replace(totop_target, totop_repl, 1)

    themebtn_target = '<button id="themeBtn" aria-label="切换亮色/暗色主题" title="切换主题">☀️</button>'
    themebtn_repl = '<button id="themeBtn" aria-label="切换亮色/暗色主题" title="切换主题"><i class="ph-duotone ph-sun"></i></button>'
    assert themebtn_target in content, "themebtn_target not found"
    content = content.replace(themebtn_target, themebtn_repl, 1)

    sfb_ico = '<span class="sfb-ico">🎧</span>'
    sfb_ico_repl = '<span class="sfb-ico"><i class="ph-duotone ph-headphones"></i></span>'
    assert sfb_ico in content, "sfb_ico not found"
    content = content.replace(sfb_ico, sfb_ico_repl, 1)

    sfb_mute = '<button class="sfb-quick-mute" id="sfbQuickMute" title="一键关闭声音" aria-label="一键关闭声音">✕</button>'
    sfb_mute_repl = '<button class="sfb-quick-mute" id="sfbQuickMute" title="一键关闭声音" aria-label="一键关闭声音"><i class="ph-duotone ph-speaker-slash"></i></button>'
    assert sfb_mute in content, "sfb_mute not found"
    content = content.replace(sfb_mute, sfb_mute_repl, 1)

    sp_title = '<span>🎧 700万年原生态沉浸声景</span>'
    sp_title_repl = '<span><i class="ph-duotone ph-headphones" style="margin-right:6px"></i>700万年原生态沉浸声景</span>'
    assert sp_title in content, "sp_title not found"
    content = content.replace(sp_title, sp_title_repl, 1)

    sp_close = '<button id="soundPanelClose" class="sound-panel-close" title="收起面板">✕</button>'
    sp_close_repl = '<button id="soundPanelClose" class="sound-panel-close" title="收起面板"><i class="ph-duotone ph-x"></i></button>'
    assert sp_close in content, "sp_close not found"
    content = content.replace(sp_close, sp_close_repl, 1)

    sp_sw_ico = '<span class="ssr-ico" id="soundSwitchIco">🔇</span>'
    sp_sw_ico_repl = '<span class="ssr-ico" id="soundSwitchIco"><i class="ph-duotone ph-speaker-slash"></i></span>'
    assert sp_sw_ico in content, "sp_sw_ico not found"
    content = content.replace(sp_sw_ico, sp_sw_ico_repl, 1)

    scenes_target = """  <div class="sound-scenes">
    <button class="scene-btn active" data-scene="auto">
      <span class="s-ico">✨</span>
      <span class="s-nm">时空自适应</span>
      <span class="s-sub">随浏览历史时代自动切换</span>
    </button>
    <button class="scene-btn" data-scene="jungle">
      <span class="s-ico">🌿</span>
      <span class="s-nm">雨林深处</span>
      <span class="s-sub">700~420万年·鸟鸣与树冠微风</span>
    </button>
    <button class="scene-btn" data-scene="savanna">
      <span class="s-ico">🌾</span>
      <span class="s-nm">稀树草原</span>
      <span class="s-sub">420~50万年·旷野热风与虫鸣</span>
    </button>
    <button class="scene-btn" data-scene="cave">
      <span class="s-ico">🔥</span>
      <span class="s-nm">冰川洞穴</span>
      <span class="s-sub">50~1万年·风雪呼啸与篝火噼啪</span>
    </button>
  </div>"""

    scenes_repl = """  <div class="sound-scenes">
    <button class="scene-btn active" data-scene="auto">
      <span class="s-ico"><i class="ph-duotone ph-sparkle"></i></span>
      <span class="s-nm">时空自适应</span>
      <span class="s-sub">随浏览历史时代自动切换</span>
    </button>
    <button class="scene-btn" data-scene="jungle">
      <span class="s-ico"><i class="ph-duotone ph-plant"></i></span>
      <span class="s-nm">雨林深处</span>
      <span class="s-sub">700~420万年·鸟鸣与树冠微风</span>
    </button>
    <button class="scene-btn" data-scene="savanna">
      <span class="s-ico"><i class="ph-duotone ph-sun"></i></span>
      <span class="s-nm">稀树草原</span>
      <span class="s-sub">420~50万年·旷野热风与虫鸣</span>
    </button>
    <button class="scene-btn" data-scene="cave">
      <span class="s-ico"><i class="ph-duotone ph-fire"></i></span>
      <span class="s-nm">冰川洞穴</span>
      <span class="s-sub">50~1万年·风雪呼啸与篝火噼啪</span>
    </button>
  </div>"""
    assert scenes_target in content, "scenes_target not found"
    content = content.replace(scenes_target, scenes_repl, 1)

    # 13. JavaScript: MILESTONES array
    miles_target = """const MILESTONES = [
  {i:'🦴',t:'约 700 万年前',h:'直立行走的开端',p:'人族与黑猩猩支系分道扬镳。两足行走是这场分手的第一个标志。'},
  {i:'🪨',t:'260 万年前',h:'系统性制造工具',sfx:'flint',sfxTip:'聆听燧石敲击剥片实录',p:'从"偶然使用"到"按规格制作"，认知能力的第一次质变。'},
  {i:'🌍',t:'180 万年前',h:'第一次走出非洲',p:'直立人扩散至格鲁吉亚、印尼与中国，人属首次成为跨大陆物种。'},
  {i:'🔥',t:'约 100 万年前',h:'掌握火',sfx:'fire',sfxTip:'聆听远古营火噼啪原声',flintMini:true,p:'烹饪扩展了可食资源，也延长了白昼——夜晚从此属于社交与故事。'},
  {i:'🧠',t:'80 万–20 万年前',h:'脑容量爆发',p:'曲线最陡的一段。群体协作、生态位扩张与技术积累形成正反馈。'},
  {i:'👤',t:'31.5 万年前',h:'智人出现',p:'摩洛哥杰贝尔·伊尔胡德——目前已知最早的解剖学现代人化石。'},
  {i:'🤝',t:'约 6 万年前',h:'与古人类杂交',p:'走出非洲的智人与尼安德特人、丹尼索瓦人相遇并留下后代。'},
  {i:'🎭',t:'7 万–4 万年前',h:'象征性行为革命',sfx:'flute',sfxTip:'聆听史前骨笛复原原声',p:'艺术、宗教、复杂语言——"文化爆炸"让智人彻底区别于其他物种。'},
  {i:'🧊',t:'约 4 万年前',h:'尼安德特人消失',p:'最后一个与我们有直接亲缘关系的物种退场，人属只剩一支。'},
  {i:'🌾',t:'1.17 万年前',h:'全新世与农业',p:'末次冰期结束，农业在多个中心独立起源，人口开始指数增长。'},
  {i:'🚀',t:'今天',h:'唯一的幸存者',p:'80 亿人，遍布七大洲——以及，正在把目光投向更远的地方。'}
];"""

    miles_repl = """const MILESTONES = [
  {icon:'ph-footprints',c:'#38bdf8',t:'约 700 万年前',h:'直立行走的开端',p:'人族与黑猩猩支系分道扬镳。两足行走是这场分手的第一个标志。'},
  {icon:'ph-axe',c:'#fbbf24',t:'260 万年前',h:'系统性制造工具',sfx:'flint',sfxTip:'聆听燧石敲击剥片实录',p:'从"偶然使用"到"按规格制作"，认知能力的第一次质变。'},
  {icon:'ph-globe-hemisphere-east',c:'#34d399',t:'180 万年前',h:'第一次走出非洲',p:'直立人扩散至格鲁吉亚、印尼与中国，人属首次成为跨大陆物种。'},
  {icon:'ph-fire',c:'#f97316',t:'约 100 万年前',h:'掌握火',sfx:'fire',sfxTip:'聆听远古营火噼啪原声',flintMini:true,p:'烹饪扩展了可食资源，也延长了白昼——夜晚从此属于社交与故事。'},
  {icon:'ph-brain',c:'#a78bfa',t:'80 万–20 万年前',h:'脑容量爆发',p:'曲线最陡的一段。群体协作、生态位扩张与技术积累形成正反馈。'},
  {icon:'ph-skull',c:'#38bdf8',t:'31.5 万年前',h:'智人出现',p:'摩洛哥杰贝尔·伊尔胡德——目前已知最早的解剖学现代人化石。'},
  {icon:'ph-dna',c:'#f43f5e',t:'约 6 万年前',h:'与古人类杂交',p:'走出非洲的智人与尼安德特人、丹尼索瓦人相遇并留下后代。'},
  {icon:'ph-palette',c:'#fb7185',t:'7 万–4 万年前',h:'象征性行为革命',sfx:'flute',sfxTip:'聆听史前骨笛复原原声',p:'艺术、宗教、复杂语言——"文化爆炸"让智人彻底区别于其他物种。'},
  {icon:'ph-snowflake',c:'#93c5fd',t:'约 4 万年前',h:'尼安德特人消失',p:'最后一个与我们有直接亲缘关系的物种退场，人属只剩一支。'},
  {icon:'ph-grains',c:'#facc15',t:'1.17 万年前',h:'全新世与农业',p:'末次冰期结束，农业在多个中心独立起源，人口开始指数增长。'},
  {icon:'ph-rocket',c:'#e879f9',t:'今天',h:'唯一的幸存者',p:'80 亿人，遍布七大洲——以及，正在把目光投向更远的地方。'}
];"""
    assert miles_target in content, "miles_target not found"
    content = content.replace(miles_target, miles_repl, 1)

    # 14. JavaScript: Theme button text/innerHTML toggle
    theme_js = "if(tbtn){tbtn.textContent=t==='light'?'🌙':'☀️';"
    theme_js_repl = "if(tbtn){tbtn.innerHTML=t==='light'?'<i class=\"ph-duotone ph-moon\"></i>':'<i class=\"ph-duotone ph-sun\"></i>';"
    assert theme_js in content, "theme_js not found"
    content = content.replace(theme_js, theme_js_repl, 1)

    # 15. JavaScript: Timeline popup details button
    dlink_target = '<button class="dlink" data-id="${s.id}" type="button">🗂 在物种档案库中查看 →</button>'
    dlink_repl = '<button class="dlink" data-id="${s.id}" type="button"><i class="ph-duotone ph-folder" style="margin-right:4px"></i>在物种档案库中查看 →</button>'
    assert dlink_target in content, "dlink_target not found"
    content = content.replace(dlink_target, dlink_repl, 1)

    # 16. JavaScript: Lab verdict
    verdict_target = """      <div class="cmp-verdict ${yes?'yes':'no'}">${yes
        ?`✅ 同时代 —— 两者在地球上共存约 ${span(ov)}`
        :`💤 擦肩而过 —— 时间上至少相隔 ${span(-ov)}`}</div>"""
    verdict_repl = """      <div class="cmp-verdict ${yes?'yes':'no'}">${yes
        ?`<i class="ph-duotone ph-check-circle" style="color:var(--emerald);margin-right:6px"></i>同时代 —— 两者在地球上共存约 ${span(ov)}`
        :`<i class="ph-duotone ph-hourglass" style="color:var(--rose);margin-right:6px"></i>擦肩而过 —— 时间上至少相隔 ${span(-ov)}`}</div>"""
    assert verdict_target in content, "verdict_target not found"
    content = content.replace(verdict_target, verdict_repl, 1)

    # 17. JavaScript: Species cards in archive
    card_meta_target = """        <div class="sp-meta">
          <span class="mt">${fmtMa(s.start)}</span>
          <span class="mt">🧠 ${s.brain} ml</span>
          <span class="mt">📏 ${s.height||'—'}</span>
        </div>
        <p>${s.desc}</p>
        <div class="loc">📍 ${s.region}</div>
        <button class="clink" data-id="${s.id}" type="button">🌳 在谱系树中定位</button>"""

    card_meta_repl = """        <div class="sp-meta">
          <span class="mt">${fmtMa(s.start)}</span>
          <span class="mt"><i class="ph-duotone ph-brain" style="color:var(--violet);margin-right:3px"></i>${s.brain} ml</span>
          <span class="mt"><i class="ph-duotone ph-ruler" style="color:var(--cyan);margin-right:3px"></i>${s.height||'—'}</span>
        </div>
        <p>${s.desc}</p>
        <div class="loc"><i class="ph-duotone ph-map-pin" style="color:var(--rose);margin-right:4px"></i>${s.region}</div>
        <button class="clink" data-id="${s.id}" type="button"><i class="ph-duotone ph-tree-structure" style="margin-right:4px"></i>在谱系树中定位</button>"""
    assert card_meta_target in content, "card_meta_target not found"
    content = content.replace(card_meta_target, card_meta_repl, 1)

    # 18. JavaScript: TECH and MILESTONES rendering
    tech_mile_target = """    const sfxBtn=t.sfx?`<button class="sfx-play-btn" data-sfx="${t.sfx}" type="button" title="${t.sfxTip}"><span>🔊 ${t.sfxLabel}</span></button>`:'';
    d.innerHTML=`<span class="n">${t.n}</span><div class="yr">${t.yr}</div><h4>${t.t}</h4><p>${t.d}</p>${sfxBtn}`;
    strip.appendChild(d);
  });
  const mg=$('#mileGrid');
  if(mg){
    MILESTONES.forEach(m=>{
      const d=document.createElement('div');d.className='mile';
      const sfxBtn=m.sfx?`<button class="sfx-play-btn sm" data-sfx="${m.sfx}" type="button" title="${m.sfxTip}"><span>🔊 聆听原声</span></button>`:'';
      const flintBtn=m.flintMini?`<button class="flint-mini-btn" id="flintMiniTrigger" type="button" title="进入燧石摩擦击火试炼"><span>🔥 燧石击火试炼</span></button>`:'';
      d.innerHTML=`<span class="mi" ${m.flintMini?'style="cursor:pointer" title="点击开启燧石击火试炼"':''}>${m.i}</span><div><h5>${m.h}</h5><span>${m.t}</span><p>${m.p}</p><div class="mile-actions">${sfxBtn}${flintBtn}</div></div>`;
      mg.appendChild(d);
    });
    if(window.observeReveal) window.observeReveal(mg);
  }
  document.addEventListener('click',e=>{
    const b=e.target.closest('.sfx-play-btn');
    if(b){
      e.stopPropagation();
      const sfx=b.dataset.sfx;
      if(sfx&&window.SoundEngine){
        window.SoundEngine.playSFX(sfx);
        b.classList.add('playing');
        setTimeout(()=>b.classList.remove('playing'),1200);
      }
      return;
    }
    const fb=e.target.closest('#flintMiniTrigger') || (e.target.classList.contains('mi') && e.target.textContent.trim()==='🔥');"""

    tech_mile_repl = """    const sfxBtn=t.sfx?`<button class="sfx-play-btn" data-sfx="${t.sfx}" type="button" title="${t.sfxTip}"><span><i class="ph-duotone ph-speaker-simple-high" style="margin-right:4px"></i>${t.sfxLabel}</span></button>`:'';
    d.innerHTML=`<span class="n">${t.n}</span><div class="yr">${t.yr}</div><h4>${t.t}</h4><p>${t.d}</p>${sfxBtn}`;
    strip.appendChild(d);
  });
  const mg=$('#mileGrid');
  if(mg){
    MILESTONES.forEach(m=>{
      const d=document.createElement('div');d.className='mile';
      const sfxBtn=m.sfx?`<button class="sfx-play-btn sm" data-sfx="${m.sfx}" type="button" title="${m.sfxTip}"><span><i class="ph-duotone ph-speaker-simple-high" style="margin-right:3px"></i>聆听原声</span></button>`:'';
      const flintBtn=m.flintMini?`<button class="flint-mini-btn" id="flintMiniTrigger" type="button" title="进入燧石摩擦击火试炼"><span><i class="ph-duotone ph-fire" style="color:#f97316;margin-right:3px"></i>燧石击火试炼</span></button>`:'';
      d.innerHTML=`<span class="mi" ${m.flintMini?'data-flint="1" style="cursor:pointer" title="点击开启燧石击火试炼"':''}><i class="ph-duotone ${m.icon}" style="color:${m.c}"></i></span><div><h5>${m.h}</h5><span>${m.t}</span><p>${m.p}</p><div class="mile-actions">${sfxBtn}${flintBtn}</div></div>`;
      mg.appendChild(d);
    });
    if(window.observeReveal) window.observeReveal(mg);
  }
  document.addEventListener('click',e=>{
    const b=e.target.closest('.sfx-play-btn');
    if(b){
      e.stopPropagation();
      const sfx=b.dataset.sfx;
      if(sfx&&window.SoundEngine){
        window.SoundEngine.playSFX(sfx);
        b.classList.add('playing');
        setTimeout(()=>b.classList.remove('playing'),1200);
      }
      return;
    }
    const fb=e.target.closest('#flintMiniTrigger') || e.target.closest('.mi[data-flint="1"]');"""
    assert tech_mile_target in content, "tech_mile_target not found"
    content = content.replace(tech_mile_target, tech_mile_repl, 1)

    # 19. JavaScript: China fossil sites province icon
    prov_target = '<div style="font-size:.78rem;color:var(--tx3);margin-bottom:10px">📍 ${s.prov}</div>'
    prov_repl = '<div style="font-size:.78rem;color:var(--tx3);margin-bottom:10px"><i class="ph-duotone ph-map-pin" style="color:var(--rose);margin-right:4px"></i>${s.prov}</div>'
    assert prov_target in content, "prov_target not found"
    content = content.replace(prov_target, prov_repl, 1)

    # 20. JavaScript: STARTS and ACCEL
    starts_accel_target = """  // 人类世起点之争
  const STARTS=[
    {i:'🌾',t:'约 8000–5000 年前',h:'早期农业假说',
     p:'Ruddiman 提出：新石器农业与森林砍伐使大气 CO₂ 与甲烷在工业革命前数千年就已偏离自然轨道。若采此说，"人类世"的开端几乎与"文明"同义。'},
    {i:'🌎',t:'1610 年 · Orbis 低谷',h:'殖民与再造林',
     p:'Lewis 与 Maslin：欧洲殖民美洲导致原住民人口锐减、耕地弃荒、森林恢复固碳，南极冰芯记录到 CO₂ 在 1610 年前后出现约 7–10 ppm 的明显下探。这是"全球化"留在大气中的第一道伤疤。'},
    {i:'⚙️',t:'约 1760 年',h:'工业革命',
     p:'克鲁岑最初的提议，也是 IPCC 选定的"工业化前"基准年（1750）。蒸汽机与煤炭让人类第一次大规模释放地质时期封存的太阳能。'},
    {i:'☢️',t:'1950 年 · 大加速',h:'AWG 推荐方案',
     p:'钚-239 全球沉降、塑料、混凝土、化肥、CO₂ 陡升——地球系统指标与社会经济指标同步暴涨。克劳福德湖 1952 年纹层被选定为候选金钉子。'}
  ];
  const as=$('#anthroStarts');
  if(as)as.innerHTML=STARTS.map(s=>`<div class="mile reveal"><span class="mi">${s.i}</span>
      <div><h5>${s.h}</h5><span>${s.t}</span><p>${s.p}</p></div></div>`).join('');

  // 大加速
  const ACCEL=[
    {i:'👥',h:'世界人口',a:'约 7.9 亿（1750）',b:'82.7 亿（2026）',w:100,c:'#fb7185',
     p:'增长约 10.5 倍；但增速自 1963 年峰值起持续放缓，预计 2084 年前后触顶。'},
    {i:'🫧',h:'大气 CO₂ 浓度',a:'280 ppm（工业化前）',b:'约 424 ppm（2024）',w:96,c:'#fbbf24',
     p:'增幅超过 50%，为至少两百万年来的最高值，也是地质记录中最陡的一次上升。'},
    {i:'🧪',h:'化肥（氮）使用',a:'几乎为零（1900）',b:'约 1.1 亿吨/年',w:88,c:'#34d399',
     p:'人类活动固定的氮已超过所有自然陆地过程之和，彻底改变了全球氮磷循环。'},
    {i:'🏗️',h:'塑料年产量',a:'0（1950 年前）',b:'约 4 亿吨/年',w:84,c:'#60a5fa',
     p:'塑料与混凝土、铝正在形成全新的"技术圈"（technosphere）沉积层与新型"岩石"。'},
    {i:'🌡️',h:'全球平均气温',a:'工业化前基线',b:'升高约 1.3 ℃',w:70,c:'#fb923c',
     p:'2015—2024 年是有器测记录以来最暖的十年；变暖速率远快于多数自然气候事件。'},
    {i:'💀',h:'物种灭绝速率',a:'自然背景速率',b:'数十至数百倍',w:92,c:'#a78bfa',
     p:'学界普遍认为第六次大规模灭绝正在进行——这是人族 700 万年里第一次由单一物种驱动。'}
  ];
  const ag=$('#accelGrid');
  if(ag){
    ag.innerHTML=ACCEL.map(a=>`<div class="acc" style="--c:${a.c}"><div class="ai">${a.i}</div>
      <h5>${a.h}</h5>
      <div class="cmp"><span class="a">${a.a}</span><span class="ar">→</span><span class="b">${a.b}</span></div>
      <div class="accbar"><i data-w="${a.w}" style="--w:${a.w}%"></i></div>
      <p>${a.p}</p></div>`).join('');"""

    starts_accel_repl = """  // 人类世起点之争
  const STARTS=[
    {icon:'ph-grains',c:'#facc15',t:'约 8000–5000 年前',h:'早期农业假说',
     p:'Ruddiman 提出：新石器农业与森林砍伐使大气 CO₂ 与甲烷在工业革命前数千年就已偏离自然轨道。若采此说，"人类世"的开端几乎与"文明"同义。'},
    {icon:'ph-globe',c:'#34d399',t:'1610 年 · Orbis 低谷',h:'殖民与再造林',
     p:'Lewis 与 Maslin：欧洲殖民美洲导致原住民人口锐减、耕地弃荒、森林恢复固碳，南极冰芯记录到 CO₂ 在 1610 年前后出现约 7–10 ppm 的明显下探。这是"全球化"留在大气中的第一道伤疤。'},
    {icon:'ph-gear',c:'#818cf8',t:'约 1760 年',h:'工业革命',
     p:'克鲁岑最初的提议，也是 IPCC 选定的"工业化前"基准年（1750）。蒸汽机与煤炭让人类第一次大规模释放地质时期封存的太阳能。'},
    {icon:'ph-radioactive',c:'#fb7185',t:'1950 年 · 大加速',h:'AWG 推荐方案',
     p:'钚-239 全球沉降、塑料、混凝土、化肥、CO₂ 陡升——地球系统指标与社会经济指标同步暴涨。克劳福德湖 1952 年纹层被选定为候选金钉子。'}
  ];
  const as=$('#anthroStarts');
  if(as)as.innerHTML=STARTS.map(s=>`<div class="mile reveal"><span class="mi"><i class="ph-duotone ${s.icon}" style="color:${s.c}"></i></span>
      <div><h5>${s.h}</h5><span>${s.t}</span><p>${s.p}</p></div></div>`).join('');

  // 大加速
  const ACCEL=[
    {icon:'ph-users',h:'世界人口',a:'约 7.9 亿（1750）',b:'82.7 亿（2026）',w:100,c:'#fb7185',
     p:'增长约 10.5 倍；但增速自 1963 年峰值起持续放缓，预计 2084 年前后触顶。'},
    {icon:'ph-cloud',h:'大气 CO₂ 浓度',a:'280 ppm（工业化前）',b:'约 424 ppm（2024）',w:96,c:'#fbbf24',
     p:'增幅超过 50%，为至少两百万年来的最高值，也是地质记录中最陡的一次上升。'},
    {icon:'ph-flask',h:'化肥（氮）使用',a:'几乎为零（1900）',b:'约 1.1 亿吨/年',w:88,c:'#34d399',
     p:'人类活动固定的氮已超过所有自然陆地过程之和，彻底改变了全球氮磷循环。'},
    {icon:'ph-buildings',h:'塑料年产量',a:'0（1950 年前）',b:'约 4 亿吨/年',w:84,c:'#60a5fa',
     p:'塑料与混凝土、铝正在形成全新的"技术圈"（technosphere）沉积层与新型"岩石"。'},
    {icon:'ph-thermometer',h:'全球平均气温',a:'工业化前基线',b:'升高约 1.3 ℃',w:70,c:'#fb923c',
     p:'2015—2024 年是有器测记录以来最暖的十年；变暖速率远快于多数自然气候事件。'},
    {icon:'ph-skull',h:'物种灭绝速率',a:'自然背景速率',b:'数十至数百倍',w:92,c:'#a78bfa',
     p:'学界普遍认为第六次大规模灭绝正在进行——这是人族 700 万年里第一次由单一物种驱动。'}
  ];
  const ag=$('#accelGrid');
  if(ag){
    ag.innerHTML=ACCEL.map(a=>`<div class="acc" style="--c:${a.c}"><div class="ai"><i class="ph-duotone ${a.icon}" style="color:${a.c}"></i></div>
      <h5>${a.h}</h5>
      <div class="cmp"><span class="a">${a.a}</span><span class="ar">→</span><span class="b">${a.b}</span></div>
      <div class="accbar"><i data-w="${a.w}" style="--w:${a.w}%"></i></div>
      <p>${a.p}</p></div>`).join('');"""
    assert starts_accel_target in content, "starts_accel_target not found"
    content = content.replace(starts_accel_target, starts_accel_repl, 1)

    # 21. JavaScript: Sound switch icon update
    sw_ico_js = "if (swIco) swIco.textContent = enabled ? '🔊' : '🔇';"
    sw_ico_js_repl = "if (swIco) swIco.innerHTML = enabled ? '<i class=\"ph-duotone ph-speaker-high\"></i>' : '<i class=\"ph-duotone ph-speaker-slash\"></i>';"
    assert sw_ico_js in content, "sw_ico_js not found"
    content = content.replace(sw_ico_js, sw_ico_js_repl, 1)

    # 22. JavaScript: DnaApp talents & quote icon
    dna_tal_js = "const talEl = $('#dicTalent'); if (talEl) talEl.textContent = '⚡ 专属特质：' + data.identity.talent;"
    dna_tal_js_repl = "const talEl = $('#dicTalent'); if (talEl) talEl.innerHTML = '<i class=\"ph-duotone ph-lightning\" style=\"color:var(--amber);margin-right:4px\"></i>专属特质：' + data.identity.talent;"
    assert dna_tal_js in content, "dna_tal_js not found"
    content = content.replace(dna_tal_js, dna_tal_js_repl, 1)

    dna_quote_js = "if (ancName) ancName.textContent = '💡 ' + data.quoteObj.author;"
    dna_quote_js_repl = "if (ancName) ancName.innerHTML = '<i class=\"ph-duotone ph-lightbulb\" style=\"color:var(--amber);margin-right:4px\"></i>' + data.quoteObj.author;"
    assert dna_quote_js in content, "dna_quote_js not found"
    content = content.replace(dna_quote_js, dna_quote_js_repl, 1)

    # 23. Easter Egg Modal 1: DNA Ancestry Report HTML
    dna_modal_close = '<button class="dna-modal-close" id="dnaModalClose" type="button" title="关闭报告" aria-label="关闭">✕</button>'
    dna_modal_close_repl = '<button class="dna-modal-close" id="dnaModalClose" type="button" title="关闭报告" aria-label="关闭"><i class="ph-duotone ph-x"></i></button>'
    assert dna_modal_close in content, "dna_modal_close not found"
    content = content.replace(dna_modal_close, dna_modal_close_repl, 1)

    scanner_ring = '<div class="dna-scanner-ring"><span>🧬</span></div>'
    scanner_ring_repl = '<div class="dna-scanner-ring"><span><i class="ph-duotone ph-dna"></i></span></div>'
    assert scanner_ring in content, "scanner_ring not found"
    content = content.replace(scanner_ring, scanner_ring_repl, 1)

    dic_talent_html = '<div class="dic-talent" id="dicTalent">⚡ 专属特质：空间抽象思维 +100% · 极强夜间灵感</div>'
    dic_talent_html_repl = '<div class="dic-talent" id="dicTalent"><i class="ph-duotone ph-lightning" style="color:var(--amber);margin-right:4px"></i>专属特质：空间抽象思维 +100% · 极强夜间灵感</div>'
    assert dic_talent_html in content, "dic_talent_html not found"
    content = content.replace(dic_talent_html, dic_talent_html_repl, 1)

    row_neander = '<span class="dna-row-nm">🦴 尼安德特人基因渗入</span>'
    row_neander_repl = '<span class="dna-row-nm"><i class="ph-duotone ph-bone" style="color:#fb7185;margin-right:4px"></i>尼安德特人基因渗入</span>'
    assert row_neander in content, "row_neander not found"
    content = content.replace(row_neander, row_neander_repl, 1)

    row_denisov = '<span class="dna-row-nm">🏔️ 丹尼索瓦人基因渗入</span>'
    row_denisov_repl = '<span class="dna-row-nm"><i class="ph-duotone ph-mountains" style="color:#a78bfa;margin-right:4px"></i>丹尼索瓦人基因渗入</span>'
    assert row_denisov in content, "row_denisov not found"
    content = content.replace(row_denisov, row_denisov_repl, 1)

    row_sapiens = '<span class="dna-row-nm">🌍 早期智人非洲血统</span>'
    row_sapiens_repl = '<span class="dna-row-nm"><i class="ph-duotone ph-globe-hemisphere-east" style="color:#34d399;margin-right:4px"></i>早期智人非洲血统</span>'
    assert row_sapiens in content, "row_sapiens not found"
    content = content.replace(row_sapiens, row_sapiens_repl, 1)

    anc_name_html = '<b id="dnaAncestorName">💡 320万年前 · 露西（Lucy）对你说：</b>'
    anc_name_html_repl = '<b id="dnaAncestorName"><i class="ph-duotone ph-lightbulb" style="color:var(--amber);margin-right:4px"></i>320万年前 · 露西（Lucy）对你说：</b>'
    assert anc_name_html in content, "anc_name_html not found"
    content = content.replace(anc_name_html, anc_name_html_repl, 1)

    dna_actions = """      <!-- 操作按钮群 -->
      <div class="dna-actions">
        <button class="dna-btn-poster" id="dnaBtnPoster" type="button">
          <span>生成海报</span>
        </button>
        <button class="dna-btn-reroll" id="dnaBtnReroll" type="button">
          <span>重新测算</span>
        </button>
        <button class="dna-btn-close" id="dnaBtnClose" type="button">
          <span>关闭</span>
        </button>
      </div>"""

    dna_actions_repl = """      <!-- 操作按钮群 -->
      <div class="dna-actions">
        <button class="dna-btn-poster" id="dnaBtnPoster" type="button">
          <i class="ph-duotone ph-image" style="margin-right:5px"></i><span>生成海报</span>
        </button>
        <button class="dna-btn-reroll" id="dnaBtnReroll" type="button">
          <i class="ph-duotone ph-arrow-clockwise" style="margin-right:5px"></i><span>重新测算</span>
        </button>
        <button class="dna-btn-close" id="dnaBtnClose" type="button">
          <i class="ph-duotone ph-x" style="margin-right:5px"></i><span>关闭</span>
        </button>
      </div>"""
    assert dna_actions in content, "dna_actions not found"
    content = content.replace(dna_actions, dna_actions_repl, 1)

    # 24. Poster Modal HTML
    poster_close = '<button class="dna-modal-close" id="posterModalClose" type="button" title="关闭海报" aria-label="关闭">✕</button>'
    poster_close_repl = '<button class="dna-modal-close" id="posterModalClose" type="button" title="关闭海报" aria-label="关闭"><i class="ph-duotone ph-x"></i></button>'
    assert poster_close in content, "poster_close not found"
    content = content.replace(poster_close, poster_close_repl, 1)

    poster_head = '<h4>📸 朋友圈专属海报已生成</h4>'
    poster_head_repl = '<h4><i class="ph-duotone ph-camera" style="color:var(--cyan);margin-right:6px"></i>朋友圈专属海报已生成</h4>'
    assert poster_head in content, "poster_head not found"
    content = content.replace(poster_head, poster_head_repl, 1)

    poster_actions = """    <div class="poster-actions">
      <a class="poster-btn-primary" id="posterBtnDownload" download="我的古人类基因测序海报.png" href="#">
        <span>💾 保存海报图片</span>
      </a>
      <button class="poster-btn-secondary" id="posterBtnCopyText" type="button">
        <span>📋 复制朋友圈配文</span>
      </button>
      <button class="poster-btn-back" id="posterBtnBack" type="button">
        <span>✕ 返回报告</span>
      </button>
    </div>"""

    poster_actions_repl = """    <div class="poster-actions">
      <a class="poster-btn-primary" id="posterBtnDownload" download="我的古人类基因测序海报.png" href="#">
        <span><i class="ph-duotone ph-download-simple" style="margin-right:5px"></i>保存海报图片</span>
      </a>
      <button class="poster-btn-secondary" id="posterBtnCopyText" type="button">
        <span><i class="ph-duotone ph-copy" style="margin-right:5px"></i>复制朋友圈配文</span>
      </button>
      <button class="poster-btn-back" id="posterBtnBack" type="button">
        <span><i class="ph-duotone ph-arrow-left" style="margin-right:5px"></i>返回报告</span>
      </button>
    </div>"""
    assert poster_actions in content, "poster_actions not found"
    content = content.replace(poster_actions, poster_actions_repl, 1)

    # 25. Flint Fire Modal HTML
    flint_close = '<button class="dna-modal-close" id="flintModalClose" title="收起试炼" aria-label="关闭">✕</button>'
    flint_close_repl = '<button class="dna-modal-close" id="flintModalClose" title="收起试炼" aria-label="关闭"><i class="ph-duotone ph-x"></i></button>'
    assert flint_close in content, "flint_close not found"
    content = content.replace(flint_close, flint_close_repl, 1)

    flint_head = '<h3>🔥 燧石击火 · 普罗米修斯试炼</h3>'
    flint_head_repl = '<h3><i class="ph-duotone ph-fire" style="color:#f97316;margin-right:6px"></i>燧石击火 · 普罗米修斯试炼</h3>'
    assert flint_head in content, "flint_head not found"
    content = content.replace(flint_head, flint_head_repl, 1)

    flint_hint = '<div class="flint-hint-badge" id="flintHintBadge">👆 连续快速敲击或摩擦 (热量会自然衰减)</div>'
    flint_hint_repl = '<div class="flint-hint-badge" id="flintHintBadge"><i class="ph-duotone ph-hand-tap" style="margin-right:4px"></i>连续快速敲击或摩擦 (热量会自然衰减)</div>'
    assert flint_hint in content, "flint_hint not found"
    content = content.replace(flint_hint, flint_hint_repl, 1)

    flint_heat = '<span class="flint-heat-label">🔥 摩擦热量与引燃温度</span>'
    flint_heat_repl = '<span class="flint-heat-label"><i class="ph-duotone ph-fire" style="color:#f97316;margin-right:4px"></i>摩擦热量与引燃温度</span>'
    assert flint_heat in content, "flint_heat not found"
    content = content.replace(flint_heat, flint_heat_repl, 1)

    flint_achieve = '<div class="flint-achieve-badge">🏆 成就解锁 · 盗火者</div>'
    flint_achieve_repl = '<div class="flint-achieve-badge"><i class="ph-duotone ph-trophy" style="color:var(--amber);margin-right:4px"></i>成就解锁 · 盗火者</div>'
    assert flint_achieve in content, "flint_achieve not found"
    content = content.replace(flint_achieve, flint_achieve_repl, 1)

    flint_ach_btns = """      <div class="ach-actions">
        <button class="ach-btn" id="flintReplayBtn" type="button">🔄 再击一次火</button>
        <button class="ach-btn secondary" id="flintCloseBtn" type="button">✕ 收起试炼</button>
      </div>"""
    flint_ach_btns_repl = """      <div class="ach-actions">
        <button class="ach-btn" id="flintReplayBtn" type="button"><i class="ph-duotone ph-arrow-clockwise" style="margin-right:4px"></i>再击一次火</button>
        <button class="ach-btn secondary" id="flintCloseBtn" type="button"><i class="ph-duotone ph-x" style="margin-right:4px"></i>收起试炼</button>
      </div>"""
    assert flint_ach_btns in content, "flint_ach_btns not found"
    content = content.replace(flint_ach_btns, flint_ach_btns_repl, 1)

    # Make sure ICP footer is still completely intact
    assert "沪ICP备2026033174号-1" in content, "ICP footer corrupted!"

    with open('人类演化全景图.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully updated 人类演化全景图.html (length {original_length} -> {len(content)})")

if __name__ == '__main__':
    update_html()
