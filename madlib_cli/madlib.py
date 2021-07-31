def welcome_msg():
  print("""
  **   Welcome User!   **
  
  A number of questions will be asked. 
  Please answer all questions. 
  """)



def read_template(filepath: str) -> str:
    if filepath!="assets/dark_and_stormy_night_template.txt":
        raise FileNotFoundError('no path found')
    file_content=''
    with open(filepath, 'r') as file:
   
        file_content = file.read()
    return file_content.strip()



import re


def parse_template(text : str)-> tuple :
    string = tuple(re.findall('{(.*?)}',text)) 
    new_text = re.sub('{.*?}','{}',text)
    return new_text,string

def input (replaced_words):
    user_input=[]
    for i in replaced_words:
         user_input.append(input(f'enter {i}:'))
    return( user_input)



def merge(new_text,input_words):

    return (re.sub(r'{[^}]*}','{}',new_text)).format(*input_words)


if __name__ == "__main__":
    y=read_template('assets/dark_and_stormy_night_template.txt')
    print(y)    







      