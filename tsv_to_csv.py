import pandas as pd
import sys
from pathlib import Path

def convert_tsv_to_csv(tsv_file):
    # Set the directory to Downloads
    downloads_dir = Path("~/Downloads").expanduser()

    input_file = downloads_dir / tsv_file
    # Save the output as a CSV file (without the 'output-' prefix)
    output_file = downloads_dir / f"{tsv_file.stem}.csv"

    if not input_file.exists():
        print("❌ Source file not found.")
        print(f"ℹ️  Please check the file name or move the file to the Downloads directory.")
        print(f"🔍 Expected file: {input_file.resolve()}")
        sys.exit(1)

    try:
        # Read the TSV file
        df = pd.read_csv(input_file, sep="\t")

        # Save the dataframe to CSV format
        df.to_csv(output_file, index=False)

        print(f"✅ CSV saved to: {output_file}")
    except Exception as e:
        print(f"❌ Failed to convert TSV to CSV: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tsv_to_csv.py filename.tsv")
        sys.exit(1)

    tsv_file = Path(sys.argv[1])
    convert_tsv_to_csv(tsv_file)
