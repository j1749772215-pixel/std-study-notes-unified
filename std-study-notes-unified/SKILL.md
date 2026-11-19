---
name: std-study-notes-unified
description: 统一管理视频课/真题精讲（四级写作、四级听力、通用课程）的 Obsidian 高可读彩色笔记规范。适用于 Windows 与 Mac 跨端共同维护，融合「人话可读性第一 + 完成态板书裁切逐笔讲透 + 柔和彩色填充卡片（兼容 Blue Topaz）」三大标准，避免各线程各改各的。
---

# 课程与真题 Obsidian 高可读彩色笔记统一规范（共同维护版）

> 本 Skill 用于统一 **四级写作、四级听力及后续所有视频课/真题笔记** 的成稿标准。无论在 Windows 还是 Mac、哪个对话线程整理或返工，**一律以此份文档为唯一准绳**。

---

## 一、唯一核心原则：优先级绝对不能倒置

整理或修改任何一卷笔记，必须严格按以下顺序把关，**严禁为了刷格式指标而做“换皮不换骨”**：

1. **第一优先 · 人话可读性 + 讲透推演（核心）**
   - 假设读者**第一次看这份笔记**、没看过原视频，也能顺着文字一次读懂。
   - **先讲“为什么这么做 / 老师怎么一步步看出来的”，再给结论和口诀**；不甩压缩黑话，不跳步骤，不把关键例题压成干巴巴的一行表格。
   - 段落自然连贯、说人话，少用“综上所述/由此可见/赋能/抓手”等机械腔。
2. **第二优先 · 图文咬合 + 干净完成态板书**
   - **绝不凑数截图**：只在“光靠文字说不清（结构分布、圈画对比、真题错点、听力选项划词）”处配图。
   - **必抽完成态并裁切干净**：只留板书/课件主体，裁掉黑边、软件菜单栏、系统 Dock、字幕、无关人像和切半邻题。
   - **每张图下必配「🖍️ 看图拆板书」卡**：把图里的红圈、蓝线、黄标、划掉线逐笔讲清对应什么意思，绝不能只贴图不解释。
3. **第三优先 · 视觉减噪 + 大胆柔和彩色填充**
   - **彻底清空非代码反引号 `` `...` `` 与 `<code>`**：Obsidian 亮色主题（如 Blue Topaz）会把行内反引号渲染成刺眼橙色胶囊，破坏阅读节奏。英文词句一律用 *斜体*、**加粗** 或语义色字；年份、题号、时间戳一律纯文本。
   - **告别白底黑字**：Blue Topaz 会把原生 Callout 背景压成透明白底，因此正文关键模块（导读、看图拆板书、分步拆解、实操技巧、避坑红线、示范演练、我理解）**大胆使用柔和底色填充卡片 + 彩色徽章**，一眼分清层次，同时保持低饱和护眼、不刺眼。

---

## 二、统一语义配色表（写作 / 听力 / 通用课程共用）

| 模块用途 | 推荐底色 | 顶栏 / 徽章色 | 左竖条色 | 适用场景（写作 / 听力示例） |
|---|---|---|---|---|
| **卷首导读** | 靛蓝渐层 `#eef2ff → #f0f9ff` | 靛蓝 `#4338ca` | `#4f46e5` | 每卷开头 3 句话讲清本卷解决什么问题 |
| **看图拆板书** | 清透青蓝 `#ecfeff` | 青蓝 `#cffafe` / `#155e75` | `#0891b2` | 写作板书红蓝圈画 / 听力白纸遮挡与划词解读 |
| **分步 / 分段条** | 蓝 `#eff6ff` / 紫 `#f5f3ff` / 绿 `#ecfdf5` | 对应深色白字徽章 | 对应主色 | 写作三段分工、5 句话拆解 / 听力三步跟读流程 |
| **实操技巧 / 验收** | 薄荷翡翠 `#ecfdf5` | 浅绿 `#d1fae5` / `#065f46` | `#10b981` | 考场提分动作、交卷前检查法、听力稳拿分习惯 |
| **避坑红线 / 反例** | 珊瑚玫瑰 `#fff1f2` | 浅红 `#ffe4e6` / `#9f1239` | `#e63946` | 语法硬伤、跑题陷阱、听力干扰项诱饵 |
| **示范 / 真题推演** | 暖杏琥珀 `#fffbeb` | 暖黄 `#fef3c7` / `#92400e` | `#f59e0b` | 写作整篇套写替换示范 / 听力真题逐句定位推演 |
| **重点提醒 / 底线** | 暖橙 `#fff7ed` | 浅橙 `#ffedd5` / `#9a3412` | `#ea580c` | 字数底线、时间红线、第二重点强调 |
| **我理解 / 思路复盘** | 柔和淡紫 `#f5f3ff` | 浅紫 `#ede9fe` / `#5b21b6` | `#7c3aed` | 读者视角的方法串联与考场落笔顺序 |
| **老师原话（蓝卡）** | 极浅蓝 `#f9fcff` | 深钴蓝 `#1565c0` 白字 | 边框 `#bbdefb` | 折叠在 `<details>` 内的逐字原话（必带精确时间戳） |
| **句内荧光重点** | 明黄 `#fef08a` | 深灰字 `#1e293b` | 圆角 `4px` | 每张卡片最多标 1–2 处真正的核心结论 |

---

## 三、标准卡片 HTML 模板（直接复用，兼容 Blue Topaz）

> 所有带填充的卡片均采用**单行紧凑属性 + 纯内联样式**，确保在 Windows/Mac 任意 Obsidian 主题下（即使未开 CSS 代码片段）都能稳定显示柔和彩色底，不退回白底黑字。

### 3.1 看图拆板书卡（青蓝底，紧跟每张板书图下方）

```html
<div style="margin:12px 0 16px 0;background:#ecfeff;border:1px solid #a5f3fc;border-left:4.5px solid #0891b2;border-radius:10px;overflow:hidden">
<div style="background:#cffafe;padding:7px 14px;font-size:13px;font-weight:700;color:#155e75">🖍️ 看图拆板书 · 标题</div>
<div style="padding:11px 16px;font-size:14.5px;line-height:1.85;color:#1e293b">
<div style="margin-bottom:6px"><span style="background:#ffe4e6;color:#be123c;padding:1px 7px;border-radius:4px;font-weight:700;font-size:12.5px">红圈 / 笔迹 1</span> 逐笔解释含义。</div>
<div><span style="background:#dbeafe;color:#1d4ed8;padding:1px 7px;border-radius:4px;font-weight:700;font-size:12.5px">蓝线 / 笔迹 2</span> 逐笔解释含义。</div>
</div>
</div>
```

### 3.2 实操技巧卡（翡翠绿底） / 避坑红卡（换为 `#fff1f2` / `#fecdd3` / `#e63946` / `#ffe4e6` / `#9f1239`）

```html
<div style="margin:14px 0 18px 0;background:#ecfdf5;border:1px solid #a7f3d0;border-left:4.5px solid #10b981;border-radius:10px;overflow:hidden">
<div style="background:#d1fae5;padding:8px 14px;font-size:13.5px;font-weight:700;color:#065f46">✅ 实操技巧标题</div>
<div style="padding:11px 16px;font-size:14.5px;line-height:1.85;color:#1e293b">
正文直接说人话，最核心一句可用 <span style="background:#fef08a;padding:1px 5px;border-radius:4px;font-weight:700">荧光黄高亮</span>。
</div>
</div>
```

### 3.3 多色分步 / 分段条（蓝 → 紫 → 绿）

```html
<div style="display:flex;flex-direction:column;gap:9px;margin:12px 0 16px 0">
<div style="padding:11px 15px;background:#eff6ff;border:1px solid #bfdbfe;border-left:4.5px solid #2563eb;border-radius:9px;font-size:14.5px;line-height:1.8;color:#1e293b"><span style="background:#2563eb;color:#fff;padding:2px 8px;border-radius:4px;font-weight:700;font-size:12px;margin-right:8px">第一步 / 第一段</span>内容。</div>
<div style="padding:11px 15px;background:#f5f3ff;border:1px solid #ddd6fe;border-left:4.5px solid #7c3aed;border-radius:9px;font-size:14.5px;line-height:1.8;color:#1e293b"><span style="background:#7c3aed;color:#fff;padding:2px 8px;border-radius:4px;font-weight:700;font-size:12px;margin-right:8px">第二步 / 第二段</span>内容。</div>
<div style="padding:11px 15px;background:#ecfdf5;border:1px solid #a7f3d0;border-left:4.5px solid #10b981;border-radius:9px;font-size:14.5px;line-height:1.8;color:#1e293b"><span style="background:#10b981;color:#fff;padding:2px 8px;border-radius:4px;font-weight:700;font-size:12px;margin-right:8px">第三步 / 第三段</span>内容。</div>
</div>
```

### 3.4 配套全库 CSS 代码片段

本 Skill 同目录 `assets/cet4-rich-notes.css` 可放入 Obsidian 的 `<Vault>/.obsidian/snippets/` 并启用，让**所有原生 Callout（`> [!tip]` / `[!warning]` / `[!note]` / `[!example]`）、`==高亮==` 和 Markdown 表格表头**也在全库自动获得一致的柔和彩色填充。

---

## 四、分学科细化约定（共同维护，不各自跑偏）

- **四级写作**：
  - 根模板 / 讲义原貌复原保留清晰色标（蓝字=固定背死、橙底=中心词替换、绿底=氛围词改写）。
  - 真题套写必走「审题信号 → 中心词替换 → 3 个氛围词怎么选 → 完整成文」四步展开。
- **四级听力**：
  - 核心例题必走「选项预处理划差异词 → 听音时抓到什么信号 → 怎么排除其余三项」完整推演，不能只贴选项表甩答案。
  - 截图里的白纸遮挡位置、白/黄/红划线含义，必须在图下「🖍️ 看图拆板书」青蓝卡里逐笔写清，且颜色必须与截图肉眼核对一致。
- **老师原话蓝卡（双学科统一）**：
  - 统一折叠在章节末尾的 `<details><summary>课堂原话（N 条）</summary>...</details>` 中，不打断正文阅读节奏。
  - 原话必须与逐字稿**逐字核对**，时间戳精确落在对应原话行起点，无断高亮、无遗漏省略号。

---

## 五、交付前必须通过的双重验收

1. **人工可读性验收（首要）**：
   - 通读正文一遍：零基础不看视频能不能顺着读懂？有没有压缩黑话、跳步推演、白底黑字大段堆砌？
   - 检查视觉节奏：每一屏内既有清爽白底正文呼吸感，又有彩色填充卡片承担“板书拆解 / 技巧 / 避坑 / 示范”锚点，层次清楚、不花哨。
2. **脚本硬指标验收（底线）**：
   - 运行对应项目的 `run_all.py`：标签闭合 `OK`、蓝卡逐字一致、时间戳对齐、`0` 孤儿图 / `0` 断链、`0` 非代码反引号与 `<code>`。

---

## 六、跨端维护约定（Windows ↔ Mac）

- 本规范独立托管于公开仓库 `std-study-notes-unified`，Windows 与 Mac 均可直接拉取或通过原始链接阅读。
- 任意线程（写作、听力、其他课程）一旦探索出更好读的卡片形态或排坑经验，**先更新本 `SKILL.md` 并推送，再批量改卷**，避免再次出现各改各的风格割裂。
