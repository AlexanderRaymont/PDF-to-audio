import pypdf
from pypdf import PdfReader

reader = PdfReader("example.pdf")


class PDFmanager():
    def __init__(self,file_name):
        self.chapters = []
        self.chapter_destinations = []
        self.fName = file_name
        self.setup()
        
    
    def get_chapters(self,clist):
        for i in clist:
            if(type(i) is list):
                self.get_chapters(i)
            else:
                self.chapter_destinations.append(i)
                self.chapters.append(i['/Title'])
        return self.chapters

    def show_chapters(self):
        if(len(self.chapters) == 0):
            print("ERROR: NO CHAPTERS")
            exit(1)
        print("Chapters: ")
        for i in range(0,len(self.chapters)):
            print(str(i+1)+". "+self.chapters[i])

    def setup(self):
        reader = PdfReader(self.fName)
        self.get_chapters(reader.outline)

    def get_section_content(self,begin_location,end = -1):
        reader = PdfReader(self.fName)
        page_number = reader.get_num_pages() -1
        begin_location_page_number = reader.get_destination_page_number(self.chapter_destinations[begin_location])
        end_flag = 1
        #print(len(self.chapters))
        if(begin_location == len(self.chapters)-1 and end == -1):
            end = page_number
            end_location_page_number = page_number
            end_flag = 0
        elif(end == -1):
            end = begin_location+1
            end_location_page_number = reader.get_destination_page_number(self.chapter_destinations[end])
        else:
            end_location_page_number = reader.get_destination_page_number(self.chapter_destinations[end])
        
        #print(begin_location_page_number,end_location_page_number)
        text=""
        for i in range(begin_location_page_number,end_location_page_number+1):
            page = reader.pages[i]
            page_content = page.extract_text()
            if(i == begin_location_page_number):
                page_content = page_content.split(self.chapters[begin_location].split(" ")[0])[1]
                if(i == end_location_page_number and end_flag == 1):
                    page_content = page_content.split(self.chapters[end].split(" ")[0])[0]
            elif(i == end_location_page_number and end_flag == 1):
                page_content = page_content.split(self.chapters[end].split(" ")[0])[0]
            text += page_content
        text = text.replace('\n',' ')
        splittext = []
        counter1=0
        counter2=0
        prevList = ["q"]
        for counter2 in range (0,len(text)):
            if(text[counter2]=='.' and (text[counter2-1] not in prevList)):
                splittext.append(text[counter1+1:counter2])
                counter1=counter2
        if(counter1 != counter2):
            splittext.append(text[counter1:counter2])
        #[print(i) for i in splittext]
        #print(text)




#manager = PDFmanager("example.pdf")
#manager.get_section_content(4)
#manager.show_chapters()