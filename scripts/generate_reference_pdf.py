import os
import subprocess
import sys

def build_html():
    html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>古人类物种与人种名称全景对照手册</title>
<style>
  @page {
    size: A4 portrait;
    margin: 10mm 11mm 11mm 11mm;
  }
  @media print {
    body {
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
  }
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    color: #1e293b;
    background: #ffffff;
    font-size: 9pt;
    line-height: 1.38;
  }

  /* Header Cover */
  .doc-header {
    border-bottom: 2px solid #0284c7;
    padding-bottom: 10px;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .doc-title-group h1 {
    font-size: 17pt;
    color: #0f172a;
    font-weight: 800;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .doc-title-group .subtitle {
    font-size: 9.5pt;
    color: #475569;
    margin-top: 4px;
    font-weight: 500;
  }
  .doc-meta {
    text-align: right;
    font-size: 7.5pt;
    color: #64748b;
    line-height: 1.5;
  }
  .doc-meta .badge {
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    padding: 2px 7px;
    border-radius: 4px;
    font-weight: 700;
    margin-bottom: 3px;
  }

  /* Notice Box */
  .notice-box {
    background: #f8fafc;
    border-left: 3.5px solid #0ea5e9;
    padding: 8px 12px;
    border-radius: 0 6px 6px 0;
    margin-bottom: 14px;
    font-size: 8.2pt;
    color: #334155;
    line-height: 1.55;
  }
  .notice-box b {
    color: #0369a1;
  }

  /* Section Styles */
  .sec-heading {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    border-left: 4px solid #0284c7;
    padding-left: 8px;
    margin: 14px 0 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    page-break-after: avoid;
  }
  .sec-heading .sec-tag {
    font-size: 7.5pt;
    font-weight: normal;
    color: #64748b;
    background: #f1f5f9;
    padding: 2px 6px;
    border-radius: 4px;
  }

  /* Tables */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 12px;
    font-size: 7.35pt;
  }
  th, td {
    padding: 3.8px 5px;
    text-align: left;
    vertical-align: top;
    border: 1px solid #e2e8f0;
  }
  th {
    background: #f1f5f9;
    color: #1e293b;
    font-weight: 700;
    font-size: 8pt;
  }
  tr:nth-child(even) td {
    background: #fafbfc;
  }
  tr {
    page-break-inside: avoid;
  }
  td.cn-name {
    font-weight: 700;
    color: #0f172a;
    white-space: nowrap;
  }
  td.sci-name {
    font-style: italic;
    color: #0369a1;
    font-family: Georgia, "Times New Roman", serif;
  }
  .grp-badge {
    display: inline-block;
    font-size: 6.8pt;
    padding: 1px 4px;
    border-radius: 3px;
    font-weight: 600;
    white-space: nowrap;
  }
  .grp-pre { background: #f1f5f9; color: #475569; border: 1px solid #cbd5e1; }
  .grp-aus { background: #fef3c7; color: #92400e; border: 1px solid #fde68a; }
  .grp-par { background: #ffedd5; color: #9a3412; border: 1px solid #fed7aa; }
  .grp-homo { background: #dbeafe; color: #1e40af; border: 1px solid #bfdbfe; }
  .grp-late { background: #ede9fe; color: #5b21b6; border: 1px solid #ddd6fe; }
  .grp-sapiens { background: #ffe4e6; color: #9f1239; border: 1px solid #fecdd3; }

  /* Info Cards Grid */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 12px;
    page-break-inside: avoid;
  }
  .info-card {
    border: 1px solid #e2e8f0;
    background: #ffffff;
    border-radius: 6px;
    padding: 8px 10px;
  }
  .info-card h4 {
    font-size: 8.8pt;
    color: #0f172a;
    margin-bottom: 4px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .info-card p {
    font-size: 7.35pt;
    color: #475569;
    line-height: 1.5;
  }

  /* Page Break Rule */
  .page-break {
    page-break-before: always;
  }

  /* Footer */
  .doc-footer {
    border-top: 1px solid #e2e8f0;
    margin-top: 14px;
    padding-top: 8px;
    display: flex;
    justify-content: space-between;
    font-size: 7.5pt;
    color: #94a3b8;
  }
</style>
</head>
<body>

  <!-- 头部 -->
  <div class="doc-header">
    <div class="doc-title-group">
      <h1>人类演化物种与人种名称对照手册</h1>
      <div class="subtitle">古人类演化谱系（Species）与现代智人地理人群（Ancestry）权威中英学名全景对照</div>
    </div>
    <div class="doc-meta">
      <span class="badge">人类演化全景图 · 权威出品</span><br>
      官方在线版：evolution.stockbuster.cn<br>
      更新时间：2026年9月 · 沪ICP备2026033174号-1
    </div>
  </div>

  <!-- 科学澄清导语 -->
  <div class="notice-box">
    <b>【重要科学界定】</b>在生命科学与人类学体系中，<b>“物种 (Species)”</b>与日常口语中的<b>“人种 (Race)”</b>是两个截然不同维度的概念：<br>
    ① <b>物种（表一）</b>：指古生物学上的人族与人属物种（如直立人、尼安德特人、能人、智人）。它们具有显著的骨骼与解剖学差异，多数在历史上已演化灭绝；<br>
    ② <b>人种/人群（表二）</b>：指<b>现存唯一人属物种——智人（Homo sapiens）内部</b>因适应局部气候而产生的表型连续过渡变异。全人类基因组相似度高达 <b>99.9%</b>，现代群体遗传学已用<b>“地理祖源人群（Geographic Ancestry）”</b>全面取代传统的种族划分。
  </div>

  <!-- 第一部分：古人类演化物种对照表 -->
  <div class="sec-heading">
    <span>第一部分：人族演化物种（Species）中英与拉丁学名全景表</span>
    <span class="sec-tag">涵盖 700万年演化史上 26 个核心物种</span>
  </div>

  <table>
    <thead>
      <tr>
        <th style="width:13%">中文正名</th>
        <th style="width:18%">规范拉丁学名 (二名法)</th>
        <th style="width:12%">英文通称</th>
        <th style="width:8%">阶元分组</th>
        <th style="width:11%">存续年代</th>
        <th style="width:10%">脑容量</th>
        <th style="width:28%">著名标本 / 化石 / 关键科学特征</th>
      </tr>
    </thead>
    <tbody>
      <!-- 早期人族 -->
      <tr>
        <td class="cn-name">乍得沙赫人</td>
        <td class="sci-name">Sahelanthropus tchadensis</td>
        <td>Sahelanthropus</td>
        <td><span class="grp-badge grp-pre">早期人族</span></td>
        <td>700万–600万年前</td>
        <td>约 350 ml</td>
        <td>“图迈”（Toumaï）。已知最古老人族候选，枕骨大孔前移；2026年股骨分析证实其具备双足行走能力。</td>
      </tr>
      <tr>
        <td class="cn-name">图根原人</td>
        <td class="sci-name">Orrorin tugenensis</td>
        <td>Orrorin / Millennium Man</td>
        <td><span class="grp-badge grp-pre">早期人族</span></td>
        <td>610万–580万年前</td>
        <td>—</td>
        <td>“千禧人”。股骨颈显示直立行走，同时保留适应攀爬的手臂，呈现“两足+树栖”镶嵌状态。</td>
      </tr>
      <tr>
        <td class="cn-name">卡达巴地猿</td>
        <td class="sci-name">Ardipithecus kadabba</td>
        <td>Kadabba Ardipithecus</td>
        <td><span class="grp-badge grp-pre">早期人族</span></td>
        <td>580万–520万年前</td>
        <td>—</td>
        <td>埃塞俄比亚出土早期基干人族，脚趾骨形态表明存在初始两足推进机制。</td>
      </tr>
      <tr>
        <td class="cn-name">始祖地猿</td>
        <td class="sci-name">Ardipithecus ramidus</td>
        <td>Ardi / Ground Ape</td>
        <td><span class="grp-badge grp-pre">早期人族</span></td>
        <td>450万–430万年前</td>
        <td>300–350 ml</td>
        <td>“阿尔迪”（Ardi）。生活于森林，地面双足行走但保留抓握大脚趾，彻底推翻“直立行走源于稀树草原”旧说。</td>
      </tr>

      <!-- 南方古猿属 -->
      <tr>
        <td class="cn-name">湖畔南方古猿</td>
        <td class="sci-name">Australopithecus anamensis</td>
        <td>Anamensis</td>
        <td><span class="grp-badge grp-aus">南方古猿</span></td>
        <td>420万–390万年前</td>
        <td>—</td>
        <td>已知最早的南方古猿。胫骨结构完全具备两足行走功能，上下半身演化显著不同步。</td>
      </tr>
      <tr>
        <td class="cn-name">阿法南方古猿</td>
        <td class="sci-name">Australopithecus afarensis</td>
        <td>Afarensis / Lucy's Species</td>
        <td><span class="grp-badge grp-aus">南方古猿</span></td>
        <td>390万–290万年前</td>
        <td>380–430 ml</td>
        <td>“露西”（Lucy）、坦桑尼亚莱托里 366 万年前火山灰脚印（证明足弓形成、无对握拇趾）。</td>
      </tr>
      <tr>
        <td class="cn-name">非洲南方古猿</td>
        <td class="sci-name">Australopithecus africanus</td>
        <td>Africanus</td>
        <td><span class="grp-badge grp-aus">南方古猿</span></td>
        <td>300万–210万年前</td>
        <td>420–500 ml</td>
        <td>“汤恩幼儿”（Taung Child）、“普莱斯夫人”。达特借此将人类演化寻根重心转向非洲。</td>
      </tr>
      <tr>
        <td class="cn-name">惊奇南方古猿</td>
        <td class="sci-name">Australopithecus garhi</td>
        <td>Garhi</td>
        <td><span class="grp-badge grp-aus">南方古猿</span></td>
        <td>约 250万年前</td>
        <td>约 450 ml</td>
        <td>与最早带切割痕迹的羚羊骨同层出土，被视为最早使用石器获取骨髓肉类的候选者。</td>
      </tr>
      <tr>
        <td class="cn-name">源泉南方古猿</td>
        <td class="sci-name">Australopithecus sediba</td>
        <td>Sediba</td>
        <td><span class="grp-badge grp-aus">南方古猿</span></td>
        <td>约 198万年前</td>
        <td>约 420 ml</td>
        <td>南非马拉帕洞穴。手部兼具精准抓握与短指骨，骨盆形态接近早期人属，属演化过渡特征显著的晚期旁支。</td>
      </tr>
      <tr>
        <td class="cn-name">平脸肯尼亚人</td>
        <td class="sci-name">Kenyanthropus platyops</td>
        <td>Flat-faced Kenya Ape</td>
        <td><span class="grp-badge grp-aus">南方古猿</span></td>
        <td>350万–320万年前</td>
        <td>—</td>
        <td>KNM-WT 40000。面部扁平，可能与洛梅克维 330 万年前最早石器工业制造者有关。</td>
      </tr>

      <!-- 傍人属 -->
      <tr>
        <td class="cn-name">埃塞俄比亚傍人</td>
        <td class="sci-name">Paranthropus aethiopicus</td>
        <td>Black Skull Hominin</td>
        <td><span class="grp-badge grp-par">傍人属</span></td>
        <td>270万–230万年前</td>
        <td>约 410 ml</td>
        <td>“黑头骨”（KNM-WT 17000）。粗壮型特化支系的开端，拥有巨大矢状脊与极突出面颊。</td>
      </tr>
      <tr>
        <td class="cn-name">鲍氏傍人</td>
        <td class="sci-name">Paranthropus boisei</td>
        <td>Boisei / Nutcracker Man</td>
        <td><span class="grp-badge grp-par">傍人属</span></td>
        <td>230万–120万年前</td>
        <td>约 510 ml</td>
        <td>“胡桃夹子人”。拥有现代人4倍面积的超大臼齿与坚厚下颌，专性咀嚼湿地草本，与早期人属共存超100万年。</td>
      </tr>
      <tr>
        <td class="cn-name">粗壮傍人</td>
        <td class="sci-name">Paranthropus robustus</td>
        <td>Robustus</td>
        <td><span class="grp-badge grp-par">傍人属</span></td>
        <td>180万–120万年前</td>
        <td>约 530 ml</td>
        <td>南非特有粗壮人族，同位素表明其兼食地下块茎与白蚁，最终在大脑爆发的人属竞争中灭绝。</td>
      </tr>

      <!-- 人属 · 早期 -->
      <tr>
        <td class="cn-name">能人</td>
        <td class="sci-name">Homo habilis</td>
        <td>Handy Man</td>
        <td><span class="grp-badge grp-homo">人属(早期)</span></td>
        <td>240万–160万年前</td>
        <td>510–690 ml</td>
        <td>“手巧的人”，奥杜威 OH 7。首次突破600ml脑量阈值，系统制造奥杜威模式一打制石器。</td>
      </tr>
      <tr>
        <td class="cn-name">鲁道夫人</td>
        <td class="sci-name">Homo rudolfensis</td>
        <td>Rudolfensis</td>
        <td><span class="grp-badge grp-homo">人属(早期)</span></td>
        <td>190万–180万年前</td>
        <td>约 750 ml</td>
        <td>KNM-ER 1470 头骨。大脑容量达 750ml，面宽平坦，与能人共同见证早期人属的多样性。</td>
      </tr>
      <tr>
        <td class="cn-name">匠人</td>
        <td class="sci-name">Homo ergaster</td>
        <td>African Early Erectus</td>
        <td><span class="grp-badge grp-homo">人属(早期)</span></td>
        <td>190万–140万年前</td>
        <td>700–900 ml</td>
        <td>“图尔卡纳男孩”（KNM-WT 15000）。身材修长高大（达1.8m），完全适应耐力长跑，率先打造阿舍利对称手斧。</td>
      </tr>
      <tr>
        <td class="cn-name">直立人</td>
        <td class="sci-name">Homo erectus</td>
        <td>Upright Man / Java / Peking Man</td>
        <td><span class="grp-badge grp-homo">人属(中坚)</span></td>
        <td>190万–11万年前</td>
        <td>850–1100 ml</td>
        <td>生存近180万年。第一波走出非洲（德马尼西、爪哇人、北京猿人、蓝田人、元谋人）；系统掌握用火与群体狩猎。</td>
      </tr>

      <!-- 人属 · 中晚期与区域分化 -->
      <tr>
        <td class="cn-name">先驱人</td>
        <td class="sci-name">Homo antecessor</td>
        <td>Pioneer Man</td>
        <td><span class="grp-badge grp-late">人属(中晚期)</span></td>
        <td>85万–80万年前</td>
        <td>约 1000 ml</td>
        <td>西班牙阿塔普埃卡。西欧最早的人属化石之一，兼具原始牙齿与现代人特征面中份，存同类相食痕迹。</td>
      </tr>
      <tr>
        <td class="cn-name">博多人</td>
        <td class="sci-name">Homo bodoensis</td>
        <td>Bodo Man</td>
        <td><span class="grp-badge grp-late">人属(中晚期)</span></td>
        <td>60万–40万年前</td>
        <td>约 1250 ml</td>
        <td>2021新拟种，埃塞俄比亚博多头骨。代表中更新世非洲向智人演化过渡的古老人群。</td>
      </tr>
      <tr>
        <td class="cn-name">海德堡人</td>
        <td class="sci-name">Homo heidelbergensis</td>
        <td>Heidelberg Man</td>
        <td><span class="grp-badge grp-late">人属(中晚期)</span></td>
        <td>70万–20万年前</td>
        <td>1100–1400 ml</td>
        <td>德国毛尔下颌、阿塔普埃卡“骨坑”。建造木结构居所、使用投掷木标枪（舍宁根标枪），智人与尼人祖先候选。</td>
      </tr>
      <tr>
        <td class="cn-name">尼安德特人</td>
        <td class="sci-name">Homo neanderthalensis</td>
        <td>Neanderthal</td>
        <td><span class="grp-badge grp-late">人属(中晚期)</span></td>
        <td>43万–4万年前</td>
        <td>1200–1750 ml (均1450)</td>
        <td>欧亚西部冰期适应霸主。莫斯特石器、墓葬习俗、骨笛与象征艺术；与现代人祖先杂交，留存1.8%–2.6%基因。</td>
      </tr>
      <tr>
        <td class="cn-name">龙人 / 丹尼索瓦人</td>
        <td class="sci-name">Homo longi (Denisovan)</td>
        <td>Dragon Man / Denisovan</td>
        <td><span class="grp-badge grp-late">人属(中晚期)</span></td>
        <td>100万–3万年前</td>
        <td>约 1420 ml</td>
        <td>哈尔滨龙人头骨（2025确认为丹人真容）、夏河下颌骨。向现代人贡献耐寒与EPAS1高海拔低氧适应基因。</td>
      </tr>
      <tr>
        <td class="cn-name">巨颅人</td>
        <td class="sci-name">Homo juluensis</td>
        <td>Julu Man</td>
        <td><span class="grp-badge grp-late">人属(中晚期)</span></td>
        <td>30万–10万年前</td>
        <td>1700–1800 ml</td>
        <td>2024年《自然·通讯》基于山西许家窑与河南许昌化石新命名。人属史上已知最大脑容量，具特化内耳迷路。</td>
      </tr>
      <tr>
        <td class="cn-name">纳勒迪人</td>
        <td class="sci-name">Homo naledi</td>
        <td>Star Man</td>
        <td><span class="grp-badge grp-late">人属(中晚期)</span></td>
        <td>33.5万–23.6万年前</td>
        <td>465–610 ml</td>
        <td>南非新星洞出土1500+件标本。极小脑量却配具极其现代的手足关节，颠覆“脑变大才产生复杂行为”认知。</td>
      </tr>
      <tr>
        <td class="cn-name">佛罗勒斯人</td>
        <td class="sci-name">Homo floresiensis</td>
        <td>Flores Hobbit</td>
        <td><span class="grp-badge grp-late">人属(岛屿矮化)</span></td>
        <td>70万–5万年前</td>
        <td>约 420 ml</td>
        <td>印尼“霍比特人”，成人身高仅 1.06 米。岛屿矮化演化奇迹，猎捕矮剑齿象与科莫多巨蜥，与智人同时代。</td>
      </tr>
      <tr>
        <td class="cn-name">吕宋人</td>
        <td class="sci-name">Homo luzonensis</td>
        <td>Luzon Man</td>
        <td><span class="grp-badge grp-late">人属(岛屿矮化)</span></td>
        <td>13.4万–5万年前</td>
        <td>小型</td>
        <td>菲律宾吕宋岛卡劳洞。微型牙齿与攀爬弯曲趾骨镶嵌共存，显示远古人类极早便具备跨越深海海峡能力。</td>
      </tr>

      <!-- 智人 -->
      <tr style="background:#fff1f2">
        <td class="cn-name" style="color:#be123c">智人 (现代人)</td>
        <td class="sci-name" style="color:#be123c;font-weight:700">Homo sapiens</td>
        <td>Modern Human / Wise Man</td>
        <td><span class="grp-badge grp-sapiens">智人 (现存)</span></td>
        <td>31.5万年前 至今</td>
        <td>1100–1900 ml (均1350)</td>
        <td>摩洛哥伊尔胡德、埃塞俄比亚奥莫一号、山顶洞人。全球80亿人唯一幸存物种；语言、认知革命与科学技术文明。</td>
      </tr>
    </tbody>
  </table>

  <!-- Page 2 下半部：人属演化四大关键阶段与技术工业对照 -->
  <div class="sec-heading" style="margin-top:16px;">
    <span>附：人属（Homo）演化四大关键阶段与代表性石器技术工业对照</span>
    <span class="sec-tag">石器工业模式 Mode 1 ~ 5</span>
  </div>

  <table style="margin-bottom:0;">
    <thead>
      <tr>
        <th style="width:15%">演化分期</th>
        <th style="width:18%">主要代表物种</th>
        <th style="width:16%">典型技术工业模式</th>
        <th style="width:24%">代表性遗址与考古实物</th>
        <th style="width:27%">关键认知与行为演化里程碑</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="cn-name" style="color:#0284c7">早期人属<br><small style="font-weight:normal;color:#64748b">约 240万–140万年前</small></td>
        <td>能人、鲁道夫人、匠人</td>
        <td><b>奥杜威工业 (模式一)</b><br><small style="color:#64748b">砾石砍砸器、石片</small></td>
        <td>坦桑尼亚奥杜威峡谷、肯尼亚图尔卡纳湖东岸</td>
        <td>脑容量突破600ml阈值；有意识预制锋利刃口切割肉食骨髓；耐力奔跑适应开阔热带草原。</td>
      </tr>
      <tr>
        <td class="cn-name" style="color:#0284c7">直立人与中期人属<br><small style="font-weight:normal;color:#64748b">约 190万–20万年前</small></td>
        <td>直立人（爪哇/北京/德马尼西）、先驱人、海德堡人、博多人</td>
        <td><b>阿舍利工业 (模式二)</b><br><small style="color:#64748b">双面对称手斧、薄刃斧</small></td>
        <td>格鲁吉亚德马尼西、中国周口店/郧县、德国舍宁根木标枪</td>
        <td>首次走出非洲扩散至全欧亚大陆；系统掌握控制用火；制造对称标准手斧；组织化群体狩猎大型猛兽。</td>
      </tr>
      <tr>
        <td class="cn-name" style="color:#0284c7">晚期人属与区域共存<br><small style="font-weight:normal;color:#64748b">约 43万–3万年前</small></td>
        <td>尼安德特人、丹尼索瓦人/龙人、巨颅人、纳勒迪人、佛罗勒斯人、吕宋人</td>
        <td><b>莫斯特工业 (模式三)</b><br><small style="color:#64748b">勒瓦娄哇预制石核剥片</small></td>
        <td>法国拉沙佩勒、西伯利亚丹尼索瓦洞、中国哈尔滨/许家窑、印尼梁布亚</td>
        <td>脑容量达演化峰值（均1450ml+）；长程规划剥制精细石刃；仪式性埋葬死者、照顾伤病；海岛特化矮化。</td>
      </tr>
      <tr>
        <td class="cn-name" style="color:#be123c">解剖学现代智人<br><small style="font-weight:normal;color:#64748b">约 31.5万年前 至今</small></td>
        <td>智人（Homo sapiens）</td>
        <td><b>石叶与复合工具 (模式四/五)</b><br><small style="color:#64748b">骨角器、细石器、陶器</small></td>
        <td>摩洛哥伊尔胡德、南非布隆伯斯洞、欧洲肖维壁画、中国山顶洞</td>
        <td>完全现代的象征符号思维与复杂句法语言；壁画与骨笛艺术；全球殖民扩散；农业定居与现代科学技术革命。</td>
      </tr>
    </tbody>
  </table>

  <div class="page-break"></div>

  <!-- 第二部分：传统人种与现代群体遗传学对照表 -->
  <div class="sec-heading">
    <span>第二部分：传统体质人类学“人种（Race）”与现代分子群体遗传学对照表</span>
    <span class="sec-tag">现代智人单一物种（Homo sapiens）内部的遗传与地理人群</span>
  </div>

  <table>
    <thead>
      <tr>
        <th style="width:13%">传统分类(旧称)</th>
        <th style="width:15%">英文/拉丁学术名</th>
        <th style="width:11%">传统通俗名</th>
        <th style="width:18%">传统主要地理分布</th>
        <th style="width:23%">现代群体遗传学规范术语 (祖源群体)</th>
        <th style="width:20%">代表性遗传单倍群 (参考)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="cn-name">欧罗巴人种</td>
        <td>Caucasoid / Caucasian</td>
        <td>白色人种 / 白种人</td>
        <td>欧洲、北非、西亚、中亚、南亚</td>
        <td><b>西欧亚人群 (West Eurasian)</b></td>
        <td>父系 Y: R1a, R1b, I, J<br>母系 mtDNA: H, U, T, J, K</td>
      </tr>
      <tr>
        <td class="cn-name">蒙古利亚人种</td>
        <td>Mongoloid</td>
        <td>黄色人种 / 黄种人</td>
        <td>东亚、东南亚、西伯利亚、中亚</td>
        <td><b>东欧亚人群 / 东亚人群 (East Asian)</b></td>
        <td>父系 Y: O (O1/O2), C2, D1a1<br>母系 mtDNA: A, B, D, F, M7, G</td>
      </tr>
      <tr>
        <td class="cn-name">尼格罗人种</td>
        <td>Negroid</td>
        <td>黑色人种 / 黑种人</td>
        <td>撒哈拉以南非洲大陆大部分地区</td>
        <td><b>撒哈拉以南非洲人群 (Sub-Saharan African)</b></td>
        <td>父系 Y: E1b1a, E1b1b, B<br>母系 mtDNA: L1, L2, L3 (多样性最高)</td>
      </tr>
      <tr>
        <td class="cn-name">澳大利亚人种</td>
        <td>Australoid</td>
        <td>棕色人种</td>
        <td>澳大利亚原住民、美拉尼西亚、巴布亚</td>
        <td><b>大洋洲原住民 / 澳-美拉尼西亚人群 (Oceanian)</b></td>
        <td>父系 Y: C1b2b, K2b1, M, S<br>母系 mtDNA: P, Q (含最高丹人基因)</td>
      </tr>
      <tr>
        <td class="cn-name">美洲人种 (独立型)</td>
        <td>Amerind / Indigenous American</td>
        <td>印第安人 / 红种人</td>
        <td>美洲大陆土著居民</td>
        <td><b>美洲原住民人群 (Indigenous American)</b><br><small style="color:#64748b">晚期东亚祖源穿过白令陆桥后形成</small></td>
        <td>父系 Y: Q-M242, C2b<br>母系 mtDNA: A2, B2, C1, D1, X2a</td>
      </tr>
      <tr>
        <td class="cn-name">开普人种 (独立型)</td>
        <td>Capoid</td>
        <td>科伊桑人 / 丛林人</td>
        <td>非洲南部纳米布与喀拉哈里荒漠</td>
        <td><b>科伊桑支系 (Khoisan / Southern African)</b><br><small style="color:#64748b">现代智人基因库中最早分化出的基干支系</small></td>
        <td>父系 Y: A (A00, A0), B2b<br>母系 mtDNA: L0d, L0k</td>
      </tr>
    </tbody>
  </table>

  <!-- 第三部分：核心演化常识与辨析 -->
  <div class="sec-heading">
    <span>第三部分：科学常识与易混淆概念深度辨析</span>
    <span class="sec-tag">现代人类学基石认知</span>
  </div>

  <div class="grid-2">
    <div class="info-card">
      <h4>🧬 1. 物种 (Species) 与人种 (Race) 的本质界限</h4>
      <p>
        生物分类阶元中，“物种”是存在生殖隔离或显著形态演化差异的客观实体（如直立人、尼安德特人与智人彼此脑容量、骨盆及颅骨差异达两倍）。而日常所谓“黄种人、白种人、黑种人”全都在智人（Homo sapiens）同一个种内，彼此<b>完全没有任何生殖隔离</b>。外表差异仅仅是近几万年来人体对局地纬度、紫外线辐射强弱产生的美拉宁色素与微量基因自适应表型。
      </p>
    </div>

    <div class="info-card">
      <h4>🦴 2. 全人类体内沉睡的“远古混血遗产”</h4>
      <p>
        古DNA高通量测序打破了绝对的“完全替代”模型：现代人在约 6 万年前走出非洲途中，与已在欧亚大陆繁衍数十万年的古人类发生了杂交。今天<b>所有非洲以外的现代人（欧亚及美洲人）均携带有 1.8%–2.6% 的尼安德特人基因</b>（带来抗寒与免疫加成）；而东亚人群、藏族同胞以及大洋洲美拉尼西亚人更携带有高达 <b>0.2%–6% 的丹尼索瓦人（龙人）基因</b>（如耐低氧的 EPAS1 突变）。
      </p>
    </div>

    <div class="info-card">
      <h4>🌍 3. “单一起源”与全人类 99.9% 极高相似度</h4>
      <p>
        基因组学测算表明：任意两个毫无血缘关系的现代人之间，DNA序列相似度高达 <b>99.9%</b>。在全基因组 30 亿个碱基对中，仅有千分之一的位点存在单核苷酸多态性（SNP）。所谓“人种间”的遗传差异，甚至远小于撒哈拉以南非洲大陆内部两个邻近部族之间的差异。这证明全球 80 亿现代人源于距今约 7 万–5 万年前走出非洲的极小瓶颈种群。
      </p>
    </div>

    <div class="info-card">
      <h4>🏛️ 4. 生物分类阶元层级极速速查指南</h4>
      <p>
        · <b>人总科 (Hominoidea)</b>：包含人科与长臂猿科；<br>
        · <b>人科 (Hominidae)</b>：包含人、黑猩猩、大猩猩、红毛猩猩；<br>
        · <b>人亚科 (Homininae)</b>：排除红毛猩猩，保留人与非洲大猿；<br>
        · <b>人族 (Hominini)</b>：人支系自 700 万年前脱离黑猩猩后的所有直系与旁系；<br>
        · <b>人属 (Homo)</b>：以能人、直立人、尼人、智人为代表的具大脑与复杂工具属；<br>
        · <b>智人 (Homo sapiens)</b>：今天地球上唯一存活的人类物种。
      </p>
    </div>
  </div>

  <!-- 页脚 -->
  <div class="doc-footer">
    <span>文献资料来源：Nature, Science, Cell, PNAS, 中国科学院古脊椎动物与古人类研究所（IVPP）权威发布研究</span>
    <span>人类演化全景图 · evolution.stockbuster.cn · 沪ICP备2026033174号-1</span>
  </div>

</body>
</html>
"""
    return html_content

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    html_path = os.path.join(script_dir, "reference_table_printable.html")
    pdf_path = os.path.join(project_root, "人种与古人类物种名称对照表.pdf")

    print(f"1. 写入可打印 HTML 模板: {html_path}")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(build_html())

    print(f"2. 调用 Google Chrome Headless 引擎渲染矢量 PDF...")
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path}"
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"生成失败! 错误信息: {res.stderr}")
        sys.exit(1)

    if os.path.exists(pdf_path):
        size_kb = round(os.path.getsize(pdf_path) / 1024, 2)
        print(f"3. 成功生成 PDF: {pdf_path} (大小: {size_kb} KB)")
    else:
        print("未找到生成的 PDF 文件！")
        sys.exit(1)

if __name__ == "__main__":
    main()
