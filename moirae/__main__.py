"""CLI entry point: python -m moirae script.yaml [-o out.mp4] [--play] [--skin ares]."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog="python -m moirae",
        description="Moirae — scripted terminal demo video pipeline",
    )
    parser.add_argument(
        "script", help="Path to YAML screenplay file",
    )
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output video path (e.g. output.mp4). If omitted, defaults to --play mode.",
    )
    parser.add_argument(
        "--play", action="store_true",
        help="Preview in terminal (no recording)",
    )
    parser.add_argument(
        "--skin", default=None,
        help="Override skin name (e.g. ares, mono, slate)",
    )
    parser.add_argument(
        "--typing-speed", type=float, default=None,
        help="Override base typing speed (seconds per character)",
    )
    parser.add_argument(
        "--timing", type=Path, default=None,
        help="Write timing manifest JSON to this path (used internally by pipeline)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print pipeline commands without executing them",
    )
    parser.add_argument(
        "--debug-camera", action="store_true",
        help="Print resolved camera keyframe timeline with visible row/col ranges",
    )
    args = parser.parse_args()

    # If neither --output nor --play, default to --play
    if args.output is None and not args.play:
        args.play = True

    # Load screenplay
    from moirae.player import load_screenplay
    screenplay = load_screenplay(
        args.script,
        skin_override=args.skin,
        typing_speed_override=args.typing_speed,
    )

    if args.debug_camera and args.output is None:
        # Debug-only mode: use existing timing/cast files to print camera report
        from moirae.camera import debug_camera_report
        from moirae.pipeline import _resolve_camera_keyframes
        stem = Path(args.script).stem
        timing_path = args.timing or Path(f"{stem}_timing.json")
        cast_path = Path(f"{stem}.cast")
        if not timing_path.exists():
            print(f"No timing file found at {timing_path}")
            print("Run with -o first to generate timing data, or pass --timing <path>")
            sys.exit(1)
        rows, cols = 80, 200
        gif_path = Path(f"{stem}.gif")
        out = screenplay.output
        keyframes = _resolve_camera_keyframes(screenplay, timing_path, total_rows=rows)
        print(debug_camera_report(
            keyframes, total_rows=rows, total_cols=cols,
            cast_path=cast_path, gif_path=gif_path,
            output_w=out.final_width, output_h=out.final_height,
        ))
        sys.exit(0)

    if args.play:
        # Terminal preview mode
        from moirae.player import play
        try:
            play(screenplay, timing_path=args.timing)
        except KeyboardInterrupt:
            sys.stdout.write("\033[0m\n")
            sys.exit(0)
    else:
        # Full pipeline mode
        from moirae.pipeline import run_pipeline
        run_pipeline(
            screenplay=screenplay,
            output_path=args.output,
            skin_override=args.skin,
            typing_speed_override=args.typing_speed,
            dry_run=args.dry_run,
            debug_camera=args.debug_camera,
        )


if __name__ == "__main__":
    main()
