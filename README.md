# Moirae

Scripted terminal demo video pipeline. Write a YAML screenplay, get a polished MP4 with camera zoom/pan, skin theming, and background compositing.

[![Moirae demo](demo.gif)](https://x.com/peterom/status/2033675452036886969)

## Give This to Your Agent

Copy-paste this into your AI coding agent (Claude Code, Cursor, etc.) to install Moirae:

```
Install Moirae, a scripted terminal demo video pipeline.

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

3. Test it works:

   python -m moirae moirae/scripts/example.yaml

   This should preview a demo in your terminal. To render an MP4:

   python -m moirae moirae/scripts/example.yaml -o demo.mp4

4. Read SKILL.md for the full screenplay YAML schema, scene types,
   camera directives, theme system, and CLI options.
```

## Examples

- [`moirae/scripts/example.yaml`](moirae/scripts/example.yaml) — basic conversation
- [`moirae/scripts/example_with_camera.yaml`](moirae/scripts/example_with_camera.yaml) — camera zoom/pan
