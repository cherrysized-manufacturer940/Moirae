# Moirae

Scripted terminal demo video pipeline. Write a YAML screenplay, get a polished MP4 with camera zoom/pan, skin theming, and background compositing.

<video src="https://ujlwuvkrxlvoswwkerdf.supabase.co/storage/v1/object/public/videos/moirae/hermes_capabilities.mp4" controls width="100%"></video>

## Give This to Your Agent

Copy-paste this into your AI coding agent (Claude Code, Cursor, etc.) to install Moirae and set up the skill:

```
Install Moirae, a scripted terminal demo video pipeline, and set it up as a skill.

1. Check prerequisites are installed:

   which asciinema agg ffmpeg

   If any are missing:
   - asciinema: brew install asciinema (or pip install asciinema)
   - agg: cargo install --git https://github.com/asciinema/agg
   - ffmpeg: brew install ffmpeg

2. Clone and install Moirae:

   git clone https://github.com/peteromallet/Moirae.git
   cd Moirae
   pip install pillow numpy pyyaml pydantic rich

3. Install the skill doc (if using Hermes Agent):

   mkdir -p ~/.hermes/skills/media/demo-video
   cp SKILL.md ~/.hermes/skills/media/demo-video/SKILL.md

4. Test it works:

   python -m moirae moirae/scripts/example.yaml

   This should preview a demo in your terminal. To render an MP4:

   python -m moirae moirae/scripts/example.yaml -o demo.mp4

5. To create your own demo, write a YAML screenplay following the format in
   moirae/scripts/example.yaml and the full schema in README.md or SKILL.md.
```

## Quick Start

```bash
# Preview in terminal
python -m moirae moirae/scripts/example.yaml

# Record and render to MP4
python -m moirae moirae/scripts/example.yaml -o demo.mp4

# With a specific skin
python -m moirae moirae/scripts/example.yaml -o demo.mp4 --skin ares
```

## Prerequisites

- `asciinema` — terminal recording
- `agg` — [asciinema GIF renderer](https://github.com/asciinema/agg)
- `ffmpeg` — video encoding
- Python: `pillow`, `numpy`, `pyyaml`, `pydantic`, `rich`

## How It Works

```
YAML screenplay → asciinema record → agg render (GIF) → composite + camera crop → MP4
```

1. **Record** — runs a scripted terminal session inside asciinema
2. **Render** — agg converts the `.cast` to a high-res GIF with the skin's terminal theme
3. **Composite** — Python reads GIF frames, applies camera zoom/pan, blends backgrounds, pipes to ffmpeg

## Screenplay Format

```yaml
title: "My Demo"
skin: "default"           # default, ares, mono, slate, poseidon, sisyphus, charizard
typing_speed: 0.04

output:
  width: 2560             # Render at 2x for sharp text
  height: 1440
  final_width: 1280       # Output at 720p
  final_height: 720
  fps: 30
  font_size: 22
  font_family: "Menlo"
  theme: "github-light"   # agg theme override (omit to use skin default)
  bg_image: "bg.jpg"      # optional background image
  bg_color: "#fdf1de"     # optional background fill
  bg_opacity: 0.85        # terminal opacity over background

scenes:
  - action: clear

  - action: type_command
    prefix: "~ $ "
    command: "hermes"

  - action: banner
    model: "deephermes-3-llama-3.1-8b"
    context: "128K"
    session_id: "d8f2a1c4"
    tools_count: 24
    skills_count: 42

  - user: "Search for the latest AI agent frameworks"
    thinking_time: 3.0
    camera:
      zoom: 1.8
      y: 0.15
      at: "user_start"
      duration: 0.8
    tools:
      - icon: "🔍"
        verb: "search"
        detail: '"AI agent frameworks 2026"'
        duration: "1.8s"
    camera_response:
      zoom: 1.4
      y: 0.65
      at: "response_start"
      duration: 0.5
    response: |
      Here are the top frameworks...
```

## CLI Options

| Flag | Description |
|------|-------------|
| `script` | Path to YAML screenplay (required) |
| `-o, --output` | Output MP4 path (omit for terminal preview) |
| `--play` | Preview in terminal without recording |
| `--skin NAME` | Override skin |
| `--typing-speed FLOAT` | Override typing speed (sec/char) |
| `--dry-run` | Print commands without executing |
| `--debug-camera` | Print resolved camera keyframes |

## Theme System

Terminal theme comes from the skin's `terminal_theme` field. Override per-video with `output.theme` in the YAML.

The compositor's background detection color is derived automatically from the theme — no manual RGB tuning needed.

Available agg themes: `asciinema`, `dracula`, `github-dark`, `github-light`, `kanagawa`, `kanagawa-dragon`, `kanagawa-light`, `monokai`, `nord`, `solarized-dark`, `solarized-light`, `gruvbox-dark`

## Examples

- [`moirae/scripts/example.yaml`](moirae/scripts/example.yaml) — basic conversation
- [`moirae/scripts/example_with_camera.yaml`](moirae/scripts/example_with_camera.yaml) — camera zoom/pan
