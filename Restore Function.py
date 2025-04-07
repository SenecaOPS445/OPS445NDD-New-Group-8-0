    if os.path.exists(destination) == False:
        os.makedirs(destination)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destination)
            print(f"[SUCCESS] Restored contents of '{zip_path}' to '{destination}'")
