import aspose.words as aw
# load the PDF file
doc = aw.Document("20CE105_3SemMarksheet.pdf")
# convert PDF to Word DOCX format
doc.save("20CE105_3SemMarksheet.docx")
# Load word document
doc = aw.Document("20CE105_3SemMarksheet.docx")
# Save as PDF
doc.save("20CE105_3SemMarksheet.pdf")