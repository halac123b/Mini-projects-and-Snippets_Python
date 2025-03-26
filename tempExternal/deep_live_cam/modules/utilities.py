import os
import platform
import ssl
import subprocess
from typing import List
import modules.globals

TEMP_DIRECTORY = "temp"
TEMP_FILE = "temp.mp4"

# monkey patch ssl for mac
if platform.system().lower() == "darwin":
    ssl._create_default_https_context = ssl._create_unverified_context

def run_ffmpeg(args: List[str]) -> bool:
    commands = [
        "ffmpeg",
        "-hide_banner",
        "-hwaccel",
        "auto",
        "-loglevel",
        modules.globals.log_level,
    ]
    commands.extend(args)
    try:
        subprocess.check_output(commands, stderr=subprocess.STDOUT)
        return True
    except Exception:
        pass
    return False

def detect_fps(target_path: str) -> float:
    command = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=r_frame_rate",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        target_path,
    ]
    output = subprocess.check_output(command).decode().strip().split("/")
    try:
        numerator, denominator = map(int, output)
        return numerator / denominator
    except Exception:
        pass
    return 30.0

def extract_frames(target_path: str) -> None:
    temp_directory_path = get_temp_directory_path(target_path)
    run_ffmpeg(
        [
            "-i",
            target_path,
            "-pix_fmt",
            "rgb24",
            os.path.join(temp_directory_path, "%04d.png"),
        ]
    )

def create_video(target_path: str, fps: float = 30.0) -> None:
    temp_output_path = get_temp_output_path(target_path)
    


def get_temp_directory_path(target_path: str) -> str:
    """Chèn thêm temp vào filepath"""
    target_name, _ = os.path.splitext(os.path.basename(target_path))
    target_directory_path = os.path.dirname(target_path)
    return os.path.join(target_directory_path, TEMP_DIRECTORY, target_name)

def get_temp_output_path(target_path: str) -> str:
    temp_directory_path = get_temp_directory_path(target_path)
    return os.path.join(temp_directory_path, TEMP_FILE)