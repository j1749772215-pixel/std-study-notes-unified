---
name: std-study-notes-unified
description: v2 统一版：融合 Windows（四级写作/听力）饱满色彩分层与 Mac（四级翻译）高级轻量微组件的 Obsidian 高可读彩色笔记规范。用于跨端共同维护，兼顾亮暗模式、Blue Topaz 主题与移动端自适应。
---

# 课程与真题 Obsidian 高可读彩色笔记统一规范（v2 共同维护版）

> 本 Skill 由 **Windows（写作 / 听力）** 与 **Mac（翻译）** 两端共同维护。所有新建与返工卷一律以本规范和共享样式 [`assets/cet4-unified.css`](./assets/cet4-unified.css) 为准。

---

## 一、核心优先级（绝不倒置）

1. **第一优先 · 人话可读性 + 讲透推演**
   - 假设读者**第一次看、没看过原视频**也能顺着读懂：先讲「为什么这么做 / 老师怎么一步步看出来的」，再给表格、口诀或结论；成段讲解为主，绝不把核心例题压成一行干表。
   - **每卷能单独读**：用到别卷的概念（如三短三长、根模板、左起跟读），第一次出现时用一两句话讲清，再附「详见卷 N」。
   - **事实边界严格**：
     - 凡整理者自己补的逻辑、过渡或反例，**显式标出「整理者补 / 整理者构造的反例」**，不冒充老师原话。
     - 字幕转写错字（如闽江→岷江、78 年→七八年、记号→句号）**一律以板书为准**，不能当事实写进正文。
2. **第二优先 · 完成态板书裁切 +「🖍️ 看图拆板书」**
   - 只在“光看字说不清”处配图，**抽完成态并人工核裁切框**（去黑边、菜单栏、Dock、字幕、无关人像；不用盲目自动裁切以免切掉课件字）。
   - 每张图下必配**青蓝底「🖍️ 看图拆板书」卡（`.rich-card.board-card`）**，把图里红圈、蓝线、黄标、白纸遮挡与划掉线逐笔讲清。
3. **第三优先 · 饱满色彩分层 + 高级轻量微组件（疏密有致）**
   - **大块用饱满彩色填充卡**（保留高辨识度与丰富色彩层次）：卷首导读靛蓝渐层（`.hero-card`）、看图拆板书青蓝卡（`.board-card`）、实操翡翠绿卡（`.card-tip`）、避坑珊瑚红卡（`.card-warn`）、替换/真题示范暖杏琥珀卡（`.card-amber`）、底线暖橙卡（`.card-orange`）、我理解淡紫卡（`.card-purple`），以及蓝/紫/绿多色分步条（`.step-list`）。
   - **细节用高级轻量微组件**（避免全屏都是整宽大块）：
     - **左右并排对比卡**（`.cols` + `.col-bad` ✗ / `.col-good` ✓ / `.col-blue` / `.col-orange` / `.col-purple`）
     - **横向胶囊词链**（`.chain` + `.chip` + `›`）
     - **圆圈自动编号步骤条**（`.steps` + `.step`）
     - **双行句子成分对照图**（`.sent` + `.sent-row` + `.seg` + `<small>`）
     - **紧凑单行提醒块**（`.blk-keng` / `.blk-ji` / `.blk-bu` / `.blk-li` / `.blk-fa` + `.tag`）
   - **统一走共享 CSS class（`cet4-unified.css`）**：两端 Obsidian 均开启 `cet4-unified.css`（同时覆盖 Blue Topaz 透明 Callout、把行内 `code` 改为柔和灰蓝胶囊、表格彩头斑马纹、亮暗色模式与移动端自适应）。单页独立导出 HTML 时再将 CSS 内嵌兜底。

---

## 二、两套颜色不打架原则（铁律）

- **句子成分色（7 色）只进对照图 `.sent` 和例句卡**：
  主语蓝 `.g-subj`、谓语红 `.g-pred`、宾语绿 `.g-obj`、状语紫 `.g-adv`、修饰青 `.g-mod`、连接词橙 `.g-conj`、非谓语棕 `.g-nf`。一个成分整块同色不拆，全卷叫法统一。
- **正文段落里只用 3 种极简句内标记**：
  - `.kw` 蓝底粗体 = 核心概念 / 中文难词
  - `.kw-green` 绿底粗体 = 定下来的英文表达
  - `==黄底==`（`<mark>`）= 全段最该记住的一句话
- **错的写法一律用 `.strike-red` 红色删除线或 `.col-bad` ✗ 卡**，绝不单独用红字，防止读者分不清红色是“谓语”还是“错”。

---

## 三、常用组件速查（直接复制 class）

### 3.1 卷首导读卡（`.hero-card`）与饱满语义大卡（`.rich-card`）

```html
<div class="hero-card">
  <div class="hero-card-h">📌 卷 N 导读</div>
  用 2–3 句人话说清本卷解决什么问题，重点词用 <span class="kw">蓝底</span> / <span class="kw-green">绿底</span> 点亮。
</div>

<div class="rich-card board-card">
  <div class="rich-card-h">🖍️ 看图拆板书 · 老师每一笔都在标什么</div>
  <div class="rich-card-b">
    <div><span class="tag tag-red">红圈</span> 对应含义……</div>
    <div><span class="tag tag-blue">蓝线</span> 对应含义……</div>
  </div>
</div>
<!-- 其余饱满大卡只需换外层 class：.card-tip（绿） / .card-warn（红） / .card-amber（琥珀） / .card-orange（橙） / .card-purple（紫） -->
```

### 3.2 左右并排对比卡（`.cols`）与横向词链（`.chain`）

```html
<div class="cols">
  <div class="col col-bad"><div class="col-h">✗ 常见错法</div><span class="strike-red">错误写法</span><div class="note">原因说明</div></div>
  <div class="col col-good"><div class="col-h">✓ 正确写法</div><span class="kw-green">正确写法</span><div class="note">改法要点</div></div>
</div>

<div class="chain">
  <span class="chip">① 审题抓信号</span><span class="arr">›</span>
  <span class="chip chip-2">② 换中心词</span><span class="arr">›</span>
  <span class="chip chip-3">③ 定 3 个氛围词</span><span class="arr">›</span>
  <span class="chip chip-end">套进 5 句话</span>
</div>
```

### 3.3 紧凑单行提示块（`.blk`）与圆圈步骤条（`.steps`）

```html
<div class="blk blk-keng"><span class="tag tag-red">坑</span>考场最易踩的坑……</div>
<div class="blk blk-ji"><span class="tag tag-orange">记</span>必须背牢的一条……</div>
<div class="blk blk-bu"><span class="tag tag-purple">补</span>整理者补的说明……</div>

<div class="steps">
  <div class="step"><b>第一步</b>：说明……</div>
  <div class="step"><b>第二步</b>：说明……</div>
</div>
```

---

## 四、老师原话卡口径（双端统一）

- 统一折叠在章节末尾 `<details><summary>课堂原话（N 条）</summary>...</details>`，用 `.quote` / `.quote-head` / `.quote-body` 深蓝原话卡。
- **用途定位**：给 Agent 回查出处用的**记录**。**必须保留精确课次与时间戳**；允许去掉口水词、修正明显字幕错字、合理截短，**以语义忠实、不歪曲原意为准**（已有全逐字验收的旧卷保持原样即可）。

---

## 五、分学科细化约定（写作 / 听力 / 翻译）

- **四级写作（Windows）**：
  - 根模板 / 讲义原貌复原保留清晰色标（蓝字=固定背死、橙底=中心词替换、绿底=氛围词改写）。
  - 真题套写必走「审题信号 → 中心词替换 → 3 个氛围词怎么选 → 完整成文」四步展开。
- **四级听力（Windows）**：
  - 核心例题必走「选项预处理划差异词 → 听音时抓到什么信号 → 怎么排除其余三项」完整推演，不能只贴选项表甩答案。
  - 截图里的白纸遮挡位置、白/黄/红划线含义，必须在图下「🖍️ 看图拆板书」青蓝卡里逐笔写清，且颜色必须与截图肉眼核对一致。
- **四级翻译（Mac）**：
  - 涉及语序重排或难句拆解时，用 `.sent` 双行句子成分对照图直观画出中文与英文的成分位移；主干/修饰语名称全卷保持一致。

---

## 六、多代理协同与验收底线

- **并行控量**：同时最多开 **3 个**写手/审稿子代理，避免一次性打光额度；每章写完立刻拼回主稿并留 checkpoint；大规模改写前保留 `before/` 快照。
- **双重验收**：
  1. **首读审稿（扮演零基础学生）**：检查顺读理解度、逻辑断层、整理者推断是否标「整理者补」、字幕错字是否已按板书纠正。
  2. **硬校验（文件哈希 / `run_all.py`）**：以实际文件内容和脚本通过为准，不轻信口头“已完成”。

---

## 七、跨端协作约定（Windows ↔ Mac）

- 公共仓库：`https://github.com/j1749772215-pixel/std-study-notes-unified`
- 成品预览台：`https://j1749772215-pixel.github.io/std-study-notes-unified/`
- 交流板：Issue `#1`（用 `gh issue view 1 --comments` 读对方进展，用 `gh issue comment 1` 留言，新样板放入 `docs/` 推送即上线预览）。
