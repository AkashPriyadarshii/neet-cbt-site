# DESIGN.md — NEET CBT 2027 Simulator

A clinical, high-precision technical design specification fusing NTA Examination Rigor, Swiss Editorial Grid, and Modern Bio-Digital Cockpit aesthetics. Built for high-stakes medical entrance preparation.

---

## 1. System Fusion & Architecture

This design rejects generic AI-default templates (centered heroes, 3 floating cards, purple gradients, and warm-amber themes) by fusing three structurally distinct design systems:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                 DESIGN FUSION                                   │
├──────────────────────────┬────────────────────────────┬─────────────────────────┤
│ System A: NTA Terminal   │ System B: Swiss Precision   │ System C: Bio-Digital   │
│ Examination Rigor        │ Editorial Grid             │ Clinical Cockpit        │
├──────────────────────────┼────────────────────────────┼─────────────────────────┤
│ • Authentic 5-state NTA  │ • Asymmetric data columns  │ • Obsidian / Deep Marine│
│   Question Palette tokens│ • Structural 1px hairlines │   ground with Cyan-Teal │
│ • Section A/B rules (10  │ • High-density data tables │ • High-contrast exam-room│
│   of 15 optional logic)  │ • Strict typographic scale │   Daylight mode toggle  │
│ • Live countdown clock   │ • Monospaced telemetry     │ • Tactile key-shortcut  │
│   with threshold alerts  │   (IBM Plex Mono)          │   badges ([S], [M], [C])│
└──────────────────────────┴────────────────────────────┴─────────────────────────┘
```

---

## 2. Color Palette & Hue Proof

### Hue Proof (Clearing 15°–45° Banned Zone)
Every primary, surface, and brand accent strictly clears the 15°–45° warm-cream / orange-amber band:

| Token Name | Hex Code | HSL Value | Hue Angle | Zone Status |
|---|---|---|---|---|
| `--brand-cyan` | `#0ea5e9` | `hsl(199, 89%, 48%)` | **199°** | **Cleared** (+154° from zone) |
| `--brand-teal` | `#0d9488` | `hsl(175, 84%, 32%)` | **175°** | **Cleared** (+130° from zone) |
| `--brand-deep` | `#0369a1` | `hsl(201, 96%, 32%)` | **201°** | **Cleared** (+156° from zone) |
| `--ground-dark`| `#070b14` | `hsl(223, 49%, 5%)`  | **223°** | **Cleared** (+178° from zone) |
| `--card-dark`  | `#0f172a` | `hsl(222, 47%, 11%)` | **222°** | **Cleared** (+177° from zone) |
| `--nta-answered`| `#16a34a`| `hsl(142, 76%, 36%)` | **142°** | **Cleared** (Authentic NTA) |
| `--nta-marked`  | `#9333ea`| `hsl(271, 81%, 56%)` | **271°** | **Cleared** (Authentic NTA) |
| `--nta-review-ans`| `#7c3aed`| `hsl(263, 70%, 58%)`| **263°** | **Cleared** (Authentic NTA) |
| `--nta-unattempt`| `#dc2626`| `hsl(0, 72%, 51%)`  | **0°**   | **Cleared** (Authentic NTA) |
| `--nta-not-visited`| `#64748b`| `hsl(215, 16%, 47%)`| **215°** | **Cleared** (Authentic NTA) |

---

## 3. Typography Hierarchy

- **Display & Headings:** `Plus Jakarta Sans`, Weights 600, 700, 800 (Letter-spacing: `-0.03em` to `-0.01em`). Clean, authoritative, modern clinical clarity.
- **Body Text:** `IBM Plex Sans`, Weights 400, 500, 600 (Line-height: `1.6`). Engineered for long-form readability on screens under intense exam conditions.
- **Data & Telemetry:** `IBM Plex Mono` / `JetBrains Mono` for timers, question indices, marks calculation, and percentile telemetry.

```css
--font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
--font-body: 'IBM Plex Sans', system-ui, -apple-system, sans-serif;
--font-mono: 'IBM Plex Mono', ui-monospace, monospace;
```

---

## 4. UI Layout & Functional Architecture

1. **Gov-Rigor Status Bar:** Broadcasts official NEET UG 2027 CBT transition data with direct action triggers.
2. **Clinical Command Header:** Logo seal with dual-tone ring, quick section anchor navigation, Daylight/Obsidian exam theme toggle, and launch button.
3. **Asymmetric Hero Console:**
   - Left Column: Headline with clinical precision, value metrics (180 Qs, 720 Marks, 200 Mins, 100% Offline PWA), instant launch CTA, and PYQ import badge.
   - Right Column: **Interactive Live NTA CBT Test Widget** allowing visitors to switch subjects, select options, click Save & Next, toggle Mark for Review, and watch real-time palette state transitions.
4. **Shift Intelligence & Comparative Telemetry:** Side-by-side analysis of OMR sheet risks vs CBT precision advantages (18 minutes saved from bubbling = 18 minutes gained for revision).
5. **Real Interface Screenshot Matrix:** High-definition responsive viewports for `testneetscreen.webp`, `homecbt.webp`, `login.webp`, and `scorecbt.webp`.
6. **Syllabus & Weightage Interactive Cockpit:** High-yield NEET chapter breakdown across Physics, Chemistry, and Biology with NCERT weightage badges.
7. **Offline-First PWA & PYQ JSON Engine:** Technical documentation of the zero-cloud, 100% local IndexedDB storage architecture with JSON import schema.
8. **Structured FAQ Accordion:** Comprehensive answers to candidate doubts with Schema.org `FAQPage` markup.
9. **Official Disclaimer & Author Footer:** Clear NTA trademark notice and educational open-source attribution to Akash Priyadarshi.

---

## 5. Accessibility & Performance Guardrails

- **WCAG 2.2 AA Compliance:** High-contrast text ratios (minimum `7.1:1` for body text, `4.5:1` for UI badges).
- **Zero AI Prose Slop:** No em-dashes in prose, no throat-clearing fluff, no passive copula overuse.
- **Pure Native Execution:** Self-contained vanilla CSS + vanilla JavaScript. Zero framework runtime overhead, instant cold start, full mobile touch and desktop keyboard navigation support.
