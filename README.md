# File Converters
A colllection of file converter scripts that I find useful. I have written each script to work/be used simularaly and to be able to be used from anywhere in 
your terminal.


<details>
<summary><code>TSV to CSV file converter</code></summary>

### To use
- For easy use, add the below alias to your `.bashrc` file:
    ```bash
    alias tsv_to_csv='python3 <path to file location>/File_Converters/tsv_to_csv.py'
    ```
- Now you can run the script from anywhere in your terminal:
    ```bash
    TSV_FILE="file-name.tsv"
    tsv_to_csv ${TSV_FILE}
    ```

The `TSV_FILE` must be located in your `Downloads` directory for this to work correctly, and the script will save the CSV file to `Downloads` too.

```bash
✅ CSV saved to: /Users/ashleyedge/Downloads/example.csv
```
Or you will get an error message
```bash
❌ Source file not found.
ℹ️  Please check the file name or move the file to the Downloads directory.
🔍 Expected file: /Users/ashleyedge/Downloads/example.tsv
```
---
</details>

<details>
<summary><code>TSV to XML file converter</code></summary>

### To use
- For easy use, add the below alias to your `.bashrc` file
    ```bash
    alias tsv_to_xml='python3 <path to file location>/File_Converters/tsv_to_xml.py'
    ```
- Now you can run the script from anywhere in your terminal.
    ```bash
    TSV_FILE="file-name.tsv"
    tsv_to_xml ${TSV_FILE}
    ```
The `TSV_FILE` must be located in your `Downloads` directory for this to work correctly and the script will save the CSV file to `Downloads` too.
```bash
✅ XML saved to: /Users/ashleyedge/Downloads/example.xml
```
Or you will get an error message
```bash
❌ Source file not found.
ℹ️  Please check the file name or move the file to the Downloads directory.
🔍 Expected file: /Users/ashleyedge/Downloads/example.tsv
```
---
</details>