from input_module import take_input
from process_module import process
from output_module import output
from system.screen_text import asci_banner
import assistant_details
import welcome
import os 
os.system("clear")

#welcome message
asci_banner(assistant_details.get_name())
welcome.greet()

while(True):
    i = take_input()
    o = process(i)
    output(o)