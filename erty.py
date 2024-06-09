import os
from dotenv import load_dotenv
import google.generativeai as genai
import flet as ft

# Load environment variables

def summaro(inp_txt):
    load_dotenv()

    my_api_key="AIzaSyBLziIatEVaqWFu7gXyLW_NNalGtQVrxiI"
    # Configure the generative AI model
    genai.configure(api_key=my_api_key)

    #prompt = """You are a report summarizer. You will take the input text containing PE features
    #and summarize the entire report, providing the important summary in points
    #within 250 words. Please provide the summary of the features according to malware presence given here: """

    prompt = """You are a report summarizer. You will take the input text containing PE features
    and summarize the entire report, providing the important summary in points
    within 250 words. Don't repeat the input pairs .Please provide the summary of the features given here: """

    #def generate_gemini_content(transcript_text, prompt):
    #model = genai.GenerativeModel("gemini-pro")
    #response = model.generate_content(prompt + transcript_text)
        #return response.text

    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + inp_txt)
    answer=response.text

    #print(answer)

    return answer


stringu="""{'optcksum': 0, 'ohs': 16096768, 'codesize': 12790784, 'majssver': 6, 'minssver': 0, 'char': 34, 'majlv': 14, 'mach': 34404, 'ss': 2,
        'majiver': 0, 'minlv': 27, 'dllch': 33120, 'sosr': 1048576, 'nsec': 7, 'exehdradr': 296, 'adrentpt': 11777164, 'sig': 17744, 'tds': 0,
        'majosver': 6, 'Text_entro ': 6.468409447932529, 'Text_mscfaddr': 12790324, 'Text_ptrrawdat': 1024, 'cbase': 5368713216, 'Text_byteaddr': 4096,
        'Text_secsize': 12790784, 'Text_datsize': 12790324, 'Data_secsize': 178688, 'Data_entro': 4.964032734613655, 'Data_ptrrawdat': 15114752, 'dbase': 5383831552,
        'Data_byteaddr': 15122432, 'Data_datsize': 208248, 'Data_mscfaddr': 208248, 'Data_char': 3221225536, 'Rsrc_secsize': 173568, 'Rsrc_entro': 2.211841991090834,
        'Rsrc_mscfaddr': 173200, 'Rsrc_datsize': 173200}"""

#summaro(stringu)
