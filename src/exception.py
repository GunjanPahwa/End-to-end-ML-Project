import sys #used to manipulate different parts of python runtime env
import logging
from src.logger import logging

def error_message_details(error,error_detail:sys):#whenever i get an error i want my custom error message, error detail would be oresent inside sys
    _,_,exc_tb=error_detail.exc_info() #exc_info would give me 3 details out of which the first two i am not interested in
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
