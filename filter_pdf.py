from PyPDF2 import PdfReader, PdfWriter
import re
import pandas as pd

pdf_file = "results_MC.pdf"
out_file = "results_MC_filtered.pdf"
student_list = "401-0643-00L 2024S Prüfungseinsicht am 30.09. 1215 - 1400(1).txt"

df = pd.read_csv(student_list, sep="\t").assign(found=False)
df["regex"] = df.apply(
    # This matches `Last, First` or `Last, First Middle`
    lambda x: fr"{re.escape(x['Nachname'])},\s[A-Za-z]*\s?{re.escape(x['Vorname'])}",
    axis=1
)

reader = PdfReader(pdf_file)
writer = PdfWriter()

for page in reader.pages:
    text = page.extract_text() 
    for idx, row in df.iterrows():
        if re.search(row.regex, text) is not None:
            writer.add_page(page)
            df.loc[idx, "found"] = True

for idx, row in df.iterrows():
    if not row.found:
        print(f"Student {row.Vorname} {row.Nachname} not found")

with open(out_file, "wb") as out:
    writer.write(out)

