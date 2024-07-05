from fpdf import FPDF

#creating class for pdf

class PDF(FPDF):  # Creating class with name -> PDF that extending FPDF properties
    
    #Creating a method for Headers
    def  header(self):
        #Image insertion
        #self.image('fox_face.png',10,8,25)   # X-co-ordinates and Y - Cooodinates and float
        #setting font
        self.set_font('times','B',20)
        # Cell padding
        self.cell(3.8)
        # Title
        self.cell(1.0,0.5,"Title",border=True,ln=1,align='C')   #30,10 are the cell dimensions,ln=1 --> print to nextline,centre alignmnet
        #line break
        self.ln(0.25)  # Title to line gap  mm
    
    #Creating method for footer
    def footer(self):
        #setting position of footer
        self.set_y(-0.40)  # from bottom it should be 15 mm gap
        #setting font for page number
        self.set_font('times','I',8)
        #page Number
        self.cell(0,0.3,f'page {self.page_no()}/{{nb}}',align = 'C')
        

# Creating PDF Object

pdf = PDF("P",'in','Letter')

# getting total no of page numbers
pdf.alias_nb_pages()

#set auto page break
pdf.set_auto_page_break(auto = True, margin = 0.35)

#Add page
pdf.add_page()

#specify font
pdf.set_font('times','BIU',16)

pdf.set_font('times','',12)

for i in range(1,41):
    pdf.cell(0,0.4,f'This is line {i} :D, we are printing samples text', ln =1)
    
pdf.output('pdf_2.pdf')

        