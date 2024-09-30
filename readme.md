# Filter pdfs for the Prüfungseinsicht

Step 1: Set up a Python environment with `pandas` and `PyPDF2`. E.g., with
```
conda env create --file environment.yml 
```

Step 2: Store `results_MC.pdf` from sfs-grading in the working directory.
If this has a different name, adjust the line in `filter_pdf.py`.

Step 3: Download the csv of students attending the exam review (e.g., from moodle) and save it as `student_list.txt`.
This should have columns `Nachname` and `Vorname`.

Step 4: Run `python filter_pdf.py`.
This filters the pdf's pages by those containing `Last, First` or `Last, Middle First` for `First`, `Last` as `Vorname`, `Nachname` in the `student_list.txt`.
It also prints names of students from `student_list.txt` not found in the pdf.
This is typically due to the moodle output not containing special characters.
A quick fix is to correct the `student_list.txt` entries.

Step 5: Print the newly created `results_MC_filtered.pdf` (one-sided!). You'll also need to bring the original answer sheets, some question sheets, and copies of the grading scheme.