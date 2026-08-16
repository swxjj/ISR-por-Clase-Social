---
name: ¿Ganamos o Perdimos?
description: Class-aware inflation analysis for Argentine workers
colors:
  bg-dark: "#070b12"
  bg-card: "#0d1527"
  bg-card-elevated: "#142036"
  bg-hover: "#1b2a47"
  accent-amber: "#38bdf8"
  accent-amber-dim: "rgba(56,189,248,.10)"
  accent-blue: "#38bdf8"
  accent-blue-dim: "rgba(56,189,248,.14)"
  signal-gain: "#10b981"
  signal-gain-dim: "rgba(16,185,129,.12)"
  signal-loss: "#f43f5e"
  signal-loss-dim: "rgba(244,63,94,.12)"
  text-primary: "#ffffff"
  text-secondary: "#cbd5e1"
  text-tertiary: "#94a3b8"
  border-default: "rgba(255,255,255,.08)"
  border-subtle: "rgba(255,255,255,.04)"
typography:
  display:
    fontFamily: "Outfit, sans-serif"
    fontSize: "clamp(2rem, 5vw, 6rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Outfit, sans-serif"
    fontSize: "1.55rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Outfit, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.06em"
    textTransform: "uppercase"
  body:
    fontFamily: "Outfit, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  label:
    fontFamily: "Outfit, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.08em"
    textTransform: "uppercase"
  subheadline:
    fontFamily: "Outfit, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.3
  small:
    fontFamily: "Outfit, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.4
rounded:
  sm: "8px"
  md: "12px"
  pill: "100px"
spacing:
  xs: "2px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "20px"
  xxl: "24px"
  hero: "28px"
  section: "32px"
  gutter-h: "40px"
components:
  button-segmented-default:
    backgroundColor: "{colors.bg-card}"
    textColor: "{colors.text-secondary}"
    rounded: "{rounded.sm}"
    padding: "7px 6px"
  button-segmented-active:
    backgroundColor: "{colors.accent-amber}"
    textColor: "#0d0a00"
    rounded: "{rounded.sm}"
    padding: "7px 6px"
  button-toggle-default:
    backgroundColor: "transparent"
    textColor: "{colors.text-secondary}"
    rounded: "100px"
    padding: "5px 12px"
  button-toggle-active:
    backgroundColor: "{colors.accent-blue-dim}"
    textColor: "{colors.accent-blue}"
    rounded: "100px"
    padding: "5px 12px"
  card-container:
    backgroundColor: "{colors.bg-card}"
    rounded: "{rounded.md}"
    padding: "20px"
  input-date:
    backgroundColor: "{colors.bg-card}"
    textColor: "{colors.text-primary}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  input-range-thumb:
    backgroundColor: "{colors.accent-amber}"
    size: "16px"
  badge-gain:
    backgroundColor: "{colors.signal-gain-dim}"
    textColor: "{colors.signal-gain}"
    rounded: "100px"
    padding: "2px 8px"
  badge-loss:
    backgroundColor: "{colors.signal-loss-dim}"
    textColor: "{colors.signal-loss}"
    rounded: "100px"
    padding: "2px 8px"
---

# Design System: ¿Ganamos o Perdimos?

## Overview

**Creative North Star: "Your Actual Income"**

This design system reveals the real purchasing power of workers by coupling employment data with class-based consumption patterns. The visual language is sophisticated but not intimidating—it speaks with precision and clarity to finance-aware and finance-curious audiences alike. A dark, high-contrast palette makes analytical narratives feel authoritative without coldness. The interaction model prioritizes user control: segmented selectors and transparent data refresh empower workers to explore their own inflation experience.

The system balances three competing needs: analytical rigor (charts, numbers, trends), accessibility (no jargon, clear affordances), and trustworthiness (real INDEC data, obvious sourcing). The dark theme grounds complex financial data in a calm, focused space; amber and blue accents carry semantic weight (agency, contrast, clarity).

**Key Characteristics:**
- Dark, high-contrast foundation with purpose-driven color accents
- Finance-rigorous but human-centered (not sterile)
- Data-driven interactivity: users choose dates, sectors, classes
- Real-time data sourcing, visible and trustworthy
- Responsive two-column grid (sidebar controls, main results)

## Colors

A dark palette with three accent layers: warm amber for primary interactions and data emphasis, cool blue for secondary data threads, and semantic signal colors for trend polarity (green gain, red loss).

### Primary
- **Warm Amber** (#e8b84b): Primary interactive accent. Highlights key UI affordances (active segmented buttons, major KPI numbers when user selects). Used sparingly—less than 10% of any surface. Carries warmth and approachability in an otherwise cool palette.
- **Amber Tint** (rgba(232,184,75,.10)): Low-opacity variant for backgrounds and light emphasis. Guides the eye without overwhelming.

### Secondary
- **Cool Blue** (#4f8ef7): Secondary data accent. Appears on subordinate metrics, component toggles, secondary narrative threads. Less dominant than amber; signals "related but not primary."
- **Blue Tint** (rgba(79,142,247,.14)): Low-opacity variant for container and badge backgrounds.

### Signal Colors
- **Gain Green** (#2ed573): Positive trend indicator. Salary outpaced inflation; user won.
- **Loss Red** (#f74b5e): Negative trend indicator. Inflation outpaced salary; user lost.
- **Dim variants** of both: Low-opacity backgrounds for badge and alert containers.

### Neutral (Layered Backgrounds)
- **Deep Dark** (#070d1a): Main page background. Darkest neutral.
- **Card Background** (#0d1826): Default container fill. Slightly lighter than page.
- **Elevated Card** (#131f33): Raised surface for nested elements (dropdowns, popovers). Lifts above the card layer.
- **Hover State** (#19293f): Interactive hover background. Clear step above baseline.

### Text & Borders
- **Primary Text** (#c8d2e0): Main body and UI labels. High contrast on dark.
- **Secondary Text** (#6b7a8e): Tertiary labels, help text, dim metadata.
- **Tertiary Text** (#384555): Very subtle captions, footers, disabled states.
- **Border Default** (rgba(255,255,255,.07)): Structural dividers, card edges.
- **Border Subtle** (rgba(255,255,255,.04)): Hairline separators; panel boundaries.

### Named Rules

**The Amber Restraint Rule.** Amber is the signature accent but must remain rare: active button states only, top-level KPI callouts, and critical affordances. Its rarity makes it authority.

**The Signal Clarity Rule.** Green (gain) and red (loss) carry unambiguous semantic weight. Use nowhere else. Ensure accessibility: pair color with iconography (↑ or ↓).

## Typography

**Display Font:** DM Serif Display (serif; Google Fonts)  
**Body Font:** DM Sans (sans-serif; Google Fonts)

**Character:** Sophisticated in a fiscal sense, precise but never cold. The serif display pairing conveys authority; the sans body keeps tone approachable and human.

### Hierarchy

- **Display** (400, clamp(1.55rem, 4vw, 6rem), 1.0): Hero KPI numbers. Occupies center of attention. Serif, generous tracking.
- **Headline** (400, 1.55rem, 1.2): Page and section titles. Serif, tight tracking (–0.02em) for visual refinement.
- **Title** (600, 0.85rem, 1.4, 0.06em text-transform uppercase): Small section headers, control labels, chart legends. Draws hierarchy without excess weight.
- **Body** (400, 0.9rem, 1.55): Main narrative and KPI context. Default reading text. Max ~70ch per line in main content.
- **Label** (600, 0.7rem, 1.4, 0.08em text-transform uppercase): Form labels, captions, small UI annotations. Consistent visual rhythm.

### Named Rules

**The Serif-Serif-Sans Rule.** Serif (DM Serif Display) carries numbers and titles; sans (DM Sans) carries instruction and instruction. Mixing within a surface breaks the visual contract.

## Layout

The grid is two-column at desktop (sidebar 300px fixed, main flexible) and stacks to single-column at max-width 820px. Sidebar holds controls; main holds results. Gutter is 40px (header) or 32px (body sections).

- **Header:** 28px vertical padding, 40px horizontal, 1px bottom border (subtle divider).
- **Sidebar:** 300px fixed, 32px padding, 1px right border. Left-aligned controls: label above, input below. Spacing: 28px between control groups, 10–14px within groups.
- **Main content:** Flexible, 32px padding, 24px section gap. Results card has 20px padding, 12px border radius.
- **Mobile breakpoint (≤820px):** Sidebar moves below header, full width. Layout switches to single column; sidebar padding → 20px, main padding → 20px. Mini-KPIs switch from column to row.
- **Spacing rhythm:** 2px (xs) / 8px (sm) / 12px (md) / 16px (lg) / 20px (xl) / 24px (xxl) / 28px (hero) / 32px (section).

### Named Rules

**The Two-Column Desktop Rule.** Sidebar-plus-main is the canonical layout. Sidebar is 300px and does not resize; it contains all input controls. Main results flex to fill.

**The Controlled Density Rule.** Every component has consistent internal padding. Cards: 20px. Inputs: 8–12px. This consistency makes the interface feel intentional.

## Elevation & Depth

The system is **tonal/flat by default** with minimal shadow use. Depth is conveyed through color layering (card backgrounds step up) and borders (subtle 1px dividers). Shadows appear only on floating elements (popovers, tooltips).

### Shadow Vocabulary

- **Tooltip/Popover Shadow** (`box-shadow: 0 8px 24px rgba(0,0,0,.4)`): Appears on `.tip-bubble` and floating panels when hovered. Signals detachment from baseline.
- **Spinner Border:** Animated border (2.5px, amber top) creates depth on loading state without shadow.

### Named Rules

**The Flat-By-Default Rule.** Surfaces are tonal, not shadowed. Layers are distinguished by background color steps (dark → card → elevated). Shadows appear only on floating interactive elements (tooltips, modals, dropdowns).

## Shapes

Corners use two radii: 8px (small, compact UI) and 12px (medium, containers and cards). Inputs and small buttons use 8px; cards and major containers use 12px. No sharp corners in the system.

- **Segmented buttons:** 8px border-radius on container, 6px on individual buttons.
- **Cards and containers:** 12px.
- **Range slider thumb:** 50% (circle).
- **Badge/pill shapes:** 100px border-radius (rounded pill).

### Named Rules

**The Two-Radius Rule.** Use 8px for tight UI (buttons, inputs, small surfaces). Use 12px for breathing room (cards, panels, major containers). Do not invent a third radius.

## Components

### Segmented Control
- **Style:** Dark card background, subtle border, buttons flex-fill.
- **Default button:** Semi-transparent text, hover → bg-hover, subtle contrast.
- **Active button:** Amber background (#e8b84b), dark text (#0d0a00), 8px radius.
- **Size:** 7px vertical / 6px horizontal padding per button.
- **Use:** Class selection (Alta / Media / Baja / No sé), income source selection (Privado / Público / Informal).

### Toggle Button (Rounded Pill)
- **Style:** Transparent background, 100px border-radius, light text, 5px v-pad / 12px h-pad.
- **Hover:** bg-hover.
- **Active state:** Blue tint background + blue text + blue border.
- **Use:** "Toggle components" in chart header, collapsible sections.

### Info Tooltip (Circular Icon)
- **Style:** 14px diameter circle, subtle border, "?" text centered. 
- **Hover/focus:** Amber background-dim + amber text + popover appears.
- **Popover:** Card-hi background, 1px border, 8px padding, tooltip arrow below, box-shadow. 220px width. Appears on hover with fade + slight shift.
- **Accessibility:** `tabindex="0"`, focus-visible styling.

### Card Container
- **Style:** bg-card, 1px border (border-default), 12px radius, 20px padding.
- **Inner spacing:** 12–16px between elements.
- **Use:** Chart cards, result containers, major panels.

### Input: Month
- **Style:** bg-card, 1px border (border-default), 12px radius, 8px padding, dark color-scheme, sans-serif font.
- **Focus:** Border shifts to amber-tinted color (rgba(232,184,75,.4)).
- **Cursor:** Pointer.

### Input: Range Slider
- **Track:** 4px height, subtle border background, 2px radius.
- **Thumb:** 16px diameter, amber background, 50% radius (circle).
- **Hover:** Thumb scales to 1.2x.
- **Cursor:** Pointer.

### Counter (±/Quantity)
- **Style:** Three-part layout (minus button | centered value | plus button).
- **Buttons:** 32px square, bg-card-hi, 1px border, flex-center, sans font.
- **Value field:** Same height, border on left & right, bg-card, centered text.
- **Hover:** Buttons → bg-hover.
- **Radius:** Left button 8px-left, right button 8px-right, center flat.

### Spinner (Loading)
- **Style:** 36px square, 2.5px border, top border amber (#e8b84b), 50% radius (circle).
- **Animation:** Continuous 360° rotation, 0.7s linear.

### KPI Number
- **Style:** DM Serif Display, 6rem (desktop) / 4rem (mobile), serif, tight tracking (–0.04em), tabular-nums.
- **Color:** Conditional (gain → green, loss → red, neutral → primary text).
- **Transition:** 0.5s ease on color change.

### Trend Badge
- **Gain:** green signal background, green text, 2px v-pad / 8px h-pad, 100px radius, flexbox (icon + text).
- **Loss:** red signal background, red text, same padding.
- **Flat/Neutral:** border-default bg, secondary text color.

### Buttons (Action)
- Not extensively used in current implementation. When needed:
  - Follow segmented/toggle style above.
  - Amber for primary, blue for secondary.
  - Consistent padding and radius (8–12px).

## Do's and Don'ts

### Do:
- **Do** use amber for primary interactive affordances only (active states, top-level KPI callouts).
- **Do** use dark backgrounds (bg-dark, bg-card) as the structural foundation.
- **Do** pair signal colors (green/red) with directional icons (↑ / ↓) for accessibility.
- **Do** maintain the 300px fixed sidebar on desktop. It is the control center.
- **Do** use DM Serif Display for numbers and headlines. Its authority carries financial rigor.
- **Do** keep tooltips and popovers floating above the baseline (shadow, elevated color background).
- **Do** respond to user input with immediate visual feedback (button active states, color transitions).
- **Do** use the spacing rhythm (8/12/16/20/24/28/32px). Do not invent new gaps.
- **Do** ensure accessible color contrast (WCAG AA minimum on all text). Test with color-blindness simulators.

### Don't:
- **Don't** use amber on more than 10% of any surface. Its rarity is its authority.
- **Don't** mix serif and sans randomly. Serif is for display/headlines; sans is for body/UI.
- **Don't** introduce a third border-radius. Stick to 8px (small) and 12px (medium).
- **Don't** add shadows to non-floating elements. No shadow on cards; only tonal layers.
- **Don't** use color alone to communicate state (esp. gain/loss). Always pair with icon.
- **Don't** stack more than three levels of text hierarchy on one screen.
- **Don't** break the two-column sidebar layout at desktop without explicit product reason.
- **Don't** use sans serif for KPI numbers. Display font is serif-only for magnitude and gravitas.
