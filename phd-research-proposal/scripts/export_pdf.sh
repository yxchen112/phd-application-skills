#!/bin/zsh
# Export .docx files to PDF with Microsoft Word (macOS), so the layout can be checked page by page.
# Word is sandboxed: files are copied into its container, exported there, then copied back.
# Usage: export_pdf.sh file1.docx [file2.docx ...]   -> writes file1.pdf next to file1.docx
set -e
D="$HOME/Library/Containers/com.microsoft.Word/Data"
for f in "$@"; do
  src="$(cd "$(dirname "$f")" && pwd)/$(basename "$f")"
  base="rp_export_$$_$(basename "${f%.*}" | tr -cd 'A-Za-z0-9_')"
  cp "$src" "$D/$base.docx"; rm -f "$D/$base.pdf"
  osascript <<EOF
tell application "Microsoft Word"
  open POSIX file "$D/$base.docx"
  set d to active document
  save as d file name "$D/$base.pdf" file format format PDF
  close d saving no
end tell
EOF
  cp "$D/$base.pdf" "${src%.*}.pdf"
  rm -f "$D/$base.docx" "$D/$base.pdf"
  pages=$(python3 -c "import re,sys;s=open(sys.argv[1],'rb').read();print(len(re.findall(rb'/Type\s*/Page[^s]',s)))" "${src%.*}.pdf")
  echo "exported ${src%.*}.pdf ($pages pages)"
done
