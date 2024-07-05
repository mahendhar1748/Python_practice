from fpdf import FPDF

# create FPDF object
# Layout ('P','L') --P--> Portrait, L-> Landscape
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))

# Object creation & Page layout
pdf = FPDF('P','mm','Letter')


#Adding page
pdf.add_page()

#Specifying font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
pdf.set_font('times','',18)  # We are using times new roman with 18 font

#Adding text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)
pdf.set_text_color(220,50,50)   # adding colors
pdf.cell(40,10,"Hello world, this is first pdf text from Python",border=True)

#Printing another text
pdf.set_font('times', '', 12)
pdf.cell(80, 10, 'Good Bye World!')


#output PDF
pdf.output('pdf_1.pdf')