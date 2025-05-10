# FLAC to MP3 Converter

This Python script converts FLAC (Free Lossless Audio Codec) files to MP3 format while maintaining a high bitrate of 320kbps. It's designed to handle large music libraries efficiently by using multi-threading and providing a progress bar for the conversion process!

## Features

- Converts FLAC files to MP3 format (320kbps)
- Maintains original folder structure in the output directory
- Uses multi-threading for faster processing
- Provides a progress bar to track conversion status
- Handles Unicode characters in file names and paths
- Detailed error reporting for failed conversions

## Requirements

- Python 3.6 or higher
- FFmpeg (must be installed and accessible from the command line)
- `tqdm` Python package (for progress bar)

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.

2. Install FFmpeg:
   - **Windows**: Download from [FFmpeg official website](https://ffmpeg.org/download.html) and add it to your system PATH.
   - **macOS**: Use Homebrew: `brew install ffmpeg`
   - **Linux**: Use your distribution's package manager, e.g., `sudo apt-get install ffmpeg` for Ubuntu.

3. Install the required Python package:
   ```
   pip install tqdm
   ```

4. Download the `flac-to-mp3-converter.py` script to your local machine.

## Usage

1. Open the `flac-to-mp3-converter.py` file in a text editor.

2. Modify the `input_dir` and `output_dir` variables at the bottom of the script to match your desired input and output directories:

   ```python
   input_dir = "path/to/your/flac/files"
   output_dir = "path/to/your/output/mp3/files"
   ```

3. Run the script from the command line:

   ```
   python flac-to-mp3-converter.py
   ```

4. The script will display a progress bar and convert all FLAC files in the input directory (including subdirectories) to MP3 format.

## Examples

### Basic Usage

Convert all FLAC files in `D:\Music` to MP3 and save them in `D:\Converted_Music`:

```python
input_dir = "D:\\Music"
output_dir = "D:\\Converted_Music"
```

### Network Drive Usage

Convert FLAC files from a mapped network drive `M:\` to a local folder:

```python
input_dir = "M:\\"
output_dir = "C:\\Users\\YourUsername\\Music\\Converted"
```

### Adjusting Worker Count

If you want to change the number of parallel conversions (e.g., to 2), modify the `process_directory()` call:

```python
errors = process_directory(input_dir, output_dir, max_workers=2)
```

## Troubleshooting

If you encounter issues while running the script, try the following:

1. **FFmpeg not found**: Ensure FFmpeg is correctly installed and added to your system's PATH.

2. **Permission errors**: Check that you have read access to the input directory and write access to the output directory.

3. **Unicode errors**: If you see Unicode-related errors, try running the script in a terminal that supports Unicode (e.g., PowerShell on Windows).

4. **Performance issues**: If your system is struggling, reduce the number of workers by setting `max_workers` to a lower value in the `process_directory()` function call.

5. **Specific file errors**: If certain files consistently cause errors, check if they are corrupted or if FFmpeg supports their specific FLAC format.

## Limitations

- The script doesn't preserve metadata (tags) from the original FLAC files. If preserving metadata is crucial, consider using a different tool or modifying the script to use FFmpeg's metadata copying features.
- While the MP3 files are encoded at 320kbps, which is considered "high quality" for MP3, there will still be some loss of audio quality compared to the original FLAC files due to the nature of lossy compression.

## Contributing

Contributions to improve the script are welcome! Please feel free to submit a Pull Request or open an Issue on the GitHub repository.

## License

This script is released under the MIT License. See the LICENSE file for details.
