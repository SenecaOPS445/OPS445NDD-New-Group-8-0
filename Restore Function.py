if not os.path.exists(source):
    print(f"[ERROR] Source path '{source}' does not exist.")
    return

if zipfile.is_zipfile(source):
    zip_path = source
elif os.path.isdir(source):
    zip_path = find_zip_in_directory(source)
    if zip_path is None:
        print("[ERROR] No zip file found in the directory.")
        return
else:
    print("[ERROR] Source must be a .zip file or a directory containing one.")
    return
