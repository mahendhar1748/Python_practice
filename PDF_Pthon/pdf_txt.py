from fpdf import FPDF

#Book title  ---> Comes in header part
title = '20,000 Leagues under the Sea'

class PDF(FPDF):
    
    def header(self):
        self.set_font('times','B',15)
        
        #calculating width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        
        # Colors of frame,background and text
        self.set_draw_color(0,80,180)  #border = blue
        self.set_fill_color(230,230,0) # background = yellow
        self.set_text_color(220,50,50) #text = red
        
        #Thick ness of frame (border)
        self.set_line_width(1)
        
        #title
        self.cell(title_w,10,border=1,ln=1,align='C',fill=1)
        
        #Line break from title to text
        self.ln(10)
        
    def footer(self):
        self.set_y(-15)
        self.set_font('times','I',8)
        self.set_text_color(169,169,169)
        self.cell(0,10,f'page {self.page_no()}', align='C')
    
    # chapter title comes in pages    
    def chapter_title(self,ch_num,ch_title):
        self.set_font('times','',12)
        self.set_fill_color(200,220,255)
        chapter_title = f'Chapter {ch_num} : {ch_title}'
        self.cell(0,5,chapter_title,ln=1,fill=1)
        self.ln()
        
    #chapter content
    def chapter_body(self,name):
        # read text file
        with open(name,'rb') as fh:
            txt = fh.read().decode('latin-1')
        #set the font
        self.set_font('times','I',12)
        #inserting text
        self.multi_cell(0,5,txt)
        self.ln()
        self.set_font('times','I',12)
        self.cell(0,5,'END OF CHAPTER')
        
    def print_chapter(self,ch_num,ch_title,name):
        self.add_page()
        self.chapter_title(ch_num, ch_title)
        self.chapter_body(name)
        
#creating PDF object

pdf = PDF('P','mm','A4')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto = True, margin = 15)

# Add Page
pdf.add_page()


pdf.print_chapter(1, 'A RUNAWAY REEF', 'chp1.txt')
pdf.print_chapter(2, 'THE PROS AND CONS', 'chp2.txt')

pdf.output('pdf_3.pdf')

 
        
        
        