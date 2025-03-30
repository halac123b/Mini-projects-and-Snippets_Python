def get_datadir():
    for konlpydir in data.path:
        if (os.path.exists(konlpydir) and is_writable(konlpydir)):
            return konlpydir