import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def convert_flac_to_mp3(flac_path, mp3_path):
    try:
        os.makedirs(os.path.dirname(mp3_path), exist_ok=True)
        command = [
            'ffmpeg',
            '-i', flac_path,
            '-codec:a', 'libmp3lame',
            '-b:a', '320k',
            '-y',  # Overwrite output file if it exists
            mp3_path
        ]
        result = subprocess.run(command, check=True, capture_output=True, encoding='utf-8', errors='replace')
        return True, None
    except subprocess.CalledProcessError as e:
        return False, f"Error converting {flac_path}: {e.stderr}"
    except Exception as e:
        return False, f"Unexpected error converting {flac_path}: {str(e)}"

def process_directory(input_dir, output_dir, max_workers=4):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    flac_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.flac'):
                flac_path = os.path.join(root, file)
                relative_path = os.path.relpath(flac_path, input_dir)
                mp3_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + '.mp3')
                flac_files.append((flac_path, mp3_path))

    errors = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(convert_flac_to_mp3, flac, mp3) for flac, mp3 in flac_files]
        for future in tqdm(as_completed(futures), total=len(flac_files), desc="Converting"):
            success, error = future.result()
            if not success:
                errors.append(error)

    return errors

if __name__ == "__main__":
    input_dir = "M:\\"  # Change this to your input directory
    output_dir = "M:\\mp3Converted"  # Change this to your desired output directory

    print(f"Input directory: {input_dir}")
    print(f"Output directory: {output_dir}")

    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
    else:
        errors = process_directory(input_dir, output_dir)
        if errors:
            print("\nThe following errors occurred during conversion:")
            for error in errors:
                print(error)
        else:
            print("\nConversion complete with no errors!")

    print("\nPress Enter to exit...")
    input()