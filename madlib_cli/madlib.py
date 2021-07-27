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
y=read_template('assets/dark_and_stormy_night_template.txt')
print(y)    










      