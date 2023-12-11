import requests
from LxmlSoup import LxmlSoup

class ParseInformation:
       def __init__(self, input_word, url="https://ru.wikipedia.org/wiki/"):
              
              self.input_word = input_word
              self.url = url
              if url == "https://ru.wikipedia.org/wiki/":
                     self.url = url + self.input_word
              
              self.get = requests.get(self.url)
              html = self.get.text
              self.soup = list(LxmlSoup(html).text())

              self.text = ""
              self.result_status = ""
              self.result_status2 = ""

              self.run = False
              self.list_ = []
              self.main_data = []

              self.status = self.get.status_code
              self.trys = 0
              self.num = 0
       

       def Parse(self):
              for i in range(len(self.soup)):
                     i_t = i + 1
                     if i != len(self.soup) - 1:
                            if self.soup[i] + self.soup[i_t] != ". ":
                                  self.text = self.text + self.soup[i]

                            else:      
                                  self.list_.append(self.text)
                                  self.text = ""    

              for g in self.list_:
                     for k in list(g):
                            if k == "\n":
                                   self.num += 1
                     
                     if g.find(self.input_word.lower()) != -1 or g.find(self.input_word) != -1 and len(g) >= 20 and self.num < 4:
                                   if g.find(';') == -1:
                                          if g.find('↑') == -1:
                                                 if g.find("[править | править код]") == -1:
                                                        self.main_data.append(g)

              
              if self.status == 200:
                     self.result_status = " Connection: <site accepted connection>\n"
              
              if self.status != 200:
                     self.result_status = " Connection: <site didn't accepted connection>\n"

              if self.main_data == []:
                     self.result_status2 = " Error: <word not found>"
              
              return self.main_data
       
              