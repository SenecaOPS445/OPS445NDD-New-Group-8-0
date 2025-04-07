def find_zip_in_directory(directory):
    """Searches for the first .zip file in a directory."""
    for item in os.listdir(directory):
        if item.endswith(".zip"):
            return os.path.join(directory, item)
    return None
