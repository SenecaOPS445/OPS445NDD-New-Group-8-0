if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Restore a zip file to a specified location.")
    parser.add_argument("source", help="Path to the zip file or a directory containing a zip file")
    parser.add_argument("destination", help="Destination folder to extract the zip contents")
    args = parser.parse_args()

    restore_zip(args.source, args.destination)
