# TUIOS Workbench

> **Work in progress.** It works, but the preview is an approximation and some settings are only partly emulated. Expect rough edges.

A click-through configuration wizard for [TUIOS](https://github.com/Gaurav-Gosain/tuios) 0.11. Pick settings, watch a live mock-up of the TUIOS screen change, and export the result as:

- a **prompt for Claude Code** that merges the settings into your existing config, runs `tuios config apply` and checks for key conflicts,
- a **`config.toml`** with only the keys that differ from the defaults,
- **`tuios set-config` commands** to try the settings in a running session.

## Use it

Open `index.html` in a browser. It is one self-contained file with no build step needed to run it. Your choices are kept in the browser's local storage.

## What it covers

| Step | Settings |
|---|---|
| Theme | 11 example themes, light-terminal theme, border colors and gradients, glyph set |
| Windows | border style, gap, shared borders, title bar, window buttons, dimming, zen mode, scrollbar |
| Layout | BSP / master-stack / scrolling / floating, tiling scheme, master side and ratio, zoom, startup |
| Dock | position, compact, pill caps, workspace tabs, clock format, CPU/RAM, which component sits where |
| Rail | side, width, row and header style, section order and shares, subagent rows, files |
| Keys | keybind preset (tuios, tmux, screen, zellij), leader key, which-key popup |
| Behavior | mouse and focus, motion, agents, notifications, screen saver |
| All settings | every scalar option from `tuios list-options`, searchable |

The preview is a 112×34 character grid drawn in the browser. TUIOS's Nerd Font icons appear as plain Unicode symbols.

## Data

- `data/options.json` comes from `tuios list-options --json` (tuios 0.11.1): path, type, default, allowed values, range and description for each option.
- `data/themes.json` holds 11 themes exported with `tuios theme export <id>`.
- Dock components, keybind presets and which-key entries come from the TUIOS docs and `tuios keybinds list`.

## Build

`index.html` is generated from `src/template.html` and the data files:

```sh
python3 build.py
```

## Known gaps

- Only 11 of the 345 built-in themes are included.
- Title placement for `window_title_align = "auto"` and the scrollbar look are best guesses from the docs.
- The screen and zellij presets list only the keys the docs spell out.
- Settings that are tables (keybinding sections, custom dock cells, hooks) are not editable beyond the dock lists, preset and leader.

## Related

TUIOS docs: <https://github.com/Gaurav-Gosain/tuios/tree/main/docs>
