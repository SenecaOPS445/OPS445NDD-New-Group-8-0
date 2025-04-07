def restore_zip(source, destination):
    """Restores (unzips) a .zip file from the source to the destination."""
    if os.path.exists(source) == False:
        print(f"[ERROR] Source path '{source}' does not exist.")
        return
