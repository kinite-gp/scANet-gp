from library import banner
import pyperclip

def about():
    banner.banner()
    print("""
           Thank you for using this tool.

              While reading this text,
   my github link has been copied in your system and
    you  can  use  it  and  give  us  encouragement.

         We are happy for you to submit your
          opinion with a star or a message

                     kinite-gp


                   press a key...
    """)  
    pyperclip.copy('https://github.com/kinite-gp')
    input()


