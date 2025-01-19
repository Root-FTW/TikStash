import subprocess
import os
import csv
import json
import re
import time
import sys

# ASCII Art for TikStash
ascii_art = r"""
████████╗██╗██╗  ██╗███████╗████████╗ █████╗ ███████╗██╗  ██╗
╚══██╔══╝██║██║ ██╔╝██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║  ██║
   ██║   ██║█████╔╝ ███████╗   ██║   ███████║███████╗███████║
   ██║   ██║██╔═██╗ ╚════██║   ██║   ██╔══██║╚════██║██╔══██║
   ██║   ██║██║  ██╗███████║   ██║   ██║  ██║███████║██║  ██║
   ╚═╝   ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
           💾 Backup • Archive • Preserve Your TikTok Content 📦
                   [Channel Videos • Info • Metadata]
"""

def get_video_info(tiktok_url):
    """Retrieves TikTok video information in JSON format."""
    try:
        result = subprocess.run(
            ["yt-dlp", "-j", tiktok_url],
            capture_output=True,
            text=True,
            check=True,
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving video information: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding video information: {e}")
        return None

def download_tiktok_videos(tiktok_url, channel_name, csv_writer, videos_backup_dir):
    """Downloads all videos from a TikTok channel and saves the information to a CSV file."""
    try:
        # Get the list of videos without downloading them
        result = subprocess.run(
            ["yt-dlp", "-j", "--flat-playlist", tiktok_url],
            capture_output=True,
            text=True,
            check=True,
        )
        video_list = [json.loads(line) for line in result.stdout.strip().splitlines()]

        for video in video_list:
            video_url = video.get('url')
            if not video_url:
                print(f"Could not get URL for video: {video.get('id')}")
                continue

            video_info = get_video_info(video_url)
            if video_info:
                # Download the video to the "Videos Backup" directory
                subprocess.run(
                    [
                        "yt-dlp",
                        "-f",
                        "bestvideo+bestaudio/best",
                        "-o",
                        os.path.join(videos_backup_dir, f"%(view_count)s_%(upload_date)s_{channel_name}_video_%(id)s.%(ext)s"),
                        video_url,
                    ],
                    check=True,
                )

                # Write the information to the CSV file
                csv_writer.writerow(
                    [
                        channel_name,
                        video_info.get("view_count", ""),
                        video_info.get("upload_date", ""),
                        video_info.get("id", ""),
                        video_info.get("description", "").replace("\n", " "),
                        video_info.get("track", "")
                        or video_info.get("title", "")
                        or video_info.get("description", "").split(" ")[0],
                        # Add more fields here if needed
                    ]
                )

    except subprocess.CalledProcessError as e:
        print(f"Error downloading videos: {e}")

if __name__ == "__main__":
    print(ascii_art)
    # Prompt for the TikTok channel URL or username
    tiktok_input = input("Enter the TikTok channel URL or username: ")

    # Determine if a URL or username was entered
    if tiktok_input.startswith("https://"):
        tiktok_url = tiktok_input
        # Extract the username from the URL using a regular expression
        match = re.search(r"@([a-zA-Z0-9_.-]+)", tiktok_url)
        if match:
            channel_name = match.group(1)
        else:
            print("Could not extract username from URL.")
            exit()
    else:
        channel_name = tiktok_input
        tiktok_url = f"https://www.tiktok.com/@{channel_name}"

    # Create "Videos Backup" and "MetaData Backup" directories if they don't exist
    videos_backup_dir = "Videos Backup"
    metadata_backup_dir = "MetaData Backup"
    os.makedirs(videos_backup_dir, exist_ok=True)
    os.makedirs(metadata_backup_dir, exist_ok=True)

    # CSV filename
    csv_filename = os.path.join(metadata_backup_dir, f"{channel_name}_datainfo.csv")

    # Open the CSV file in write mode
    with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
        # Create the CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        csv_writer.writerow(
            [
                "Channel Name",
                "Views",
                "Upload Date",
                "Video ID",
                "Description",
                "Song/Sound Name",
                # Add more headers here if needed
            ]
        )

        # Get total number of videos with loading animation
        print("Retrieving channel information, please wait", end="")
        sys.stdout.flush()
        start_time = time.time()
        animation_chars = ["-", "\\", "|", "/"]
        i = 0

        # Ejecutar yt-dlp en un proceso separado
        process = subprocess.Popen(
            ["yt-dlp", "--get-filename", "-o", "%(id)s", tiktok_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Mostrar la animación mientras yt-dlp se ejecuta
        while process.poll() is None:
            print(f"\rRetrieving channel information, please wait {animation_chars[i % len(animation_chars)]}", end="")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

        # Obtener la salida de yt-dlp
        stdout, stderr = process.communicate()
        total_videos = len(stdout.strip().split("\n"))

        # Borrar la línea de la animación
        print("\r" + " " * (40), end="\r")
        sys.stdout.flush()

        print(f"The channel {tiktok_url} has a total of {total_videos} videos.")

        # Download the videos and write the information to the CSV
        download_tiktok_videos(tiktok_url, channel_name, csv_writer, videos_backup_dir)

    print(f"Download finished. Video information has been saved to '{csv_filename}'.")
