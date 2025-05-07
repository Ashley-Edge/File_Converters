import pandas as pd
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

def convert_tsv_to_xml(tsv_file):
    # Set the directory to Downloads
    downloads_dir = Path("~/Downloads").expanduser()

    input_file = downloads_dir / tsv_file
    # Remove "output-" from the XML filename to avoid duplication
    output_file = downloads_dir / f"{tsv_file.stem}.xml"

    if not input_file.exists():
        print("❌ Source file not found.")
        print(f"ℹ️  Please check the file name or move the file to the Downloads directory.")
        print(f"🔍 Expected file: {input_file.resolve()}")
        sys.exit(1)

    try:
        df = pd.read_csv(input_file, sep="\t")

        # Convert to XML using ElementTree (built-in)
        root = ET.Element("data")

        for _, row in df.iterrows():
            record = ET.SubElement(root, "record")
            for col, val in row.items():
                field = ET.SubElement(record, col)
                field.text = str(val)

        # Save the generated XML to file
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding="utf-8", xml_declaration=True)

        print(f"✅ XML saved to: {output_file}")
    except Exception as e:
        print(f"❌ Failed to convert TSV to XML: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 tsv_to_xml.py filename.tsv")
        sys.exit(1)

    tsv_file = Path(sys.argv[1])
    convert_tsv_to_xml(tsv_file)
