# YouTube Audio Downloader

A robust Command Line Interface (CLI) tool built with Python to download and convert YouTube videos to high-quality MP3 files. It is specifically designed to bypass modern bot detection (Sign-in/Signature errors) by utilizing the Android API spoofing technique.

---

## Features

- **High Quality:** Automatically extracts the best available audio and converts it to 192kbps MP3.
- **Bot-Detection Bypass:** Uses the `android` player client to avoid "Signature solving" and "Sign-in to confirm you're not a bot" errors.
- **Cookie Support:** Optionally uses cookies from your local browser (Firefox) to maintain session integrity.

---

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.12+** (Recommended for stability).
- **FFmpeg:** Required for audio conversion.
  - *Arch Linux:* `sudo pacman -S ffmpeg`
- **Node.js:** Recommended as a JavaScript runtime for signature solving.
  - *Arch Linux:* `sudo pacman -S nodejs`

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd audio_downloader
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Environment:**
   - **For Fish Shell:**
     ```fish
     source venv/bin/activate.fish
     ```
   - **For Bash/Zsh:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Prepare your links:** Open `links.txt` and paste the YouTube URLs you want to download (one per line).
   - *Note: For best results, use clean video links (avoid long playlist/mix parameters).*

2. **Run the script:**
   ```bash
   python src/main.py
   ```

3. **Check Output:** Your files will be saved in the `downloads/` folder.

---

## Project Structure

```text
.
├── src/
│   ├── main.py          # Application entry point
│   ├── file_handler.py  # Input/Output logic
│   └── downloader.py    # yt-dlp core configuration
├── downloads/           # Processed MP3 files
├── links.txt            # Input URLs
└── requirements.txt     # Python dependencies
```

---

## Troubleshooting

If you encounter a `Signature solving failed` or `Requested format is not available` error:

1. Ensure **Node.js** is installed on your system.
2. The script is currently configured to use `player_client=android`. If a specific video fails, you can modify the `downloader.py` configuration to test different clients or update your local `yt-dlp` package via:
   ```bash
   pip install -U yt-dlp
   ```
