except zipfile.BadZipFile:
    print(f"[ERROR] Failed to unzip: Bad zip file '{zip_path}'")
except PermissionError:
    print(f"[ERROR] Permission denied while extracting to '{destination}'")
except FileNotFoundError:
    print(f"[ERROR] File not found: '{zip_path}'")
except Exception:
    print("[ERROR] An unexpected error occurred.")
