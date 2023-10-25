A few bash commands to convert files to PDF (for access etc.)

*Finds all .doc (or .txt or .vtt) files in current directory and subdirectories and convert to PDF* 

* **DOC to PDF:**

```bash
for f in $(find ./ -name '*.doc'); do lowriter --headless --convert-to pdf "$f"; done
```

* **.txt or .vtt to PDF:**

```bash
for f in $(find ./ -name '*.txt'); do soffice --convert-to pdf "$f"; done
```