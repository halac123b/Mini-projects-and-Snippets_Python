import typing

# Cung cấp define cho các type để dùng trong type-hint của function
def run_ffmpeg(args: typing.List[str]) -> bool:
    if args.len() > 0:
        return True
    return False