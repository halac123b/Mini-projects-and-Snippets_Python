from pathlib import Path

# cwd(): current working directory
# glob(): find all files matching a pattern (txt)
for file_path in Path.cwd().glob("*.txt"):
    # Path("archive"): full path to the archive directory in cwd
    # / : divide override for Path, to append path
    # file_path.name: name of the file in Path
    new_path = Path("archive") / file_path.name
    # move file to new path
    file_path.replace(new_path)
