from html.parser import HTMLParser
html = ""
class MyHTMLParser(HTMLParser):
    def handle_comment(self,data):
        print(">>> Multi-line Comment")  if('\n' in data) else print(">>> Single-line Comment")
        print(data)
    def handle_data(self,data):
        if(data != '\n'):
            print(">>> Data")
            print(data)
             
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
#print(html)    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
  