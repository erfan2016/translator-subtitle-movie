'''
Sarzamin Danesh Academy
Erfan Mahigir
2024 February 23
insta: @sarzamin.danesh
site: www.Lssc.ir
'''

import random
from googletrans import Translator
import os

class TranslateSrt:
    __name_split_file = ''
    def __init__(self, path:str) -> None:
        self.path = path

    def get_name(self)->str:
        name = (self.path.split('/'))[-1]
        name = name.split('.')
        return name[0]
    
    def generate_random_name(self)->str:
        pattern = 'abcdefghijklmnopqrstuvywzABCDEFGHIJKLMNOPQRSTUVYWZ0123456789'
        name_file = ''
        for count in range(8):
            index = random.randint(0, len(pattern)-1)
            name_file += pattern[index]
        return f"{name_file}.csv"
    
    def split_srt(self)->None:
        self.__name_split_file = self.generate_random_name()
        with open(self.__name_split_file, '+a') as csv, open(self.path, 'r') as srt:
            data_file = srt.readlines()
            for line in data_file:
                if line != "\n":
                    line = line.splitlines()
                    text = line[0].replace(',', '.')
                    csv.write(f"{text},")
                else:
                    csv.write(line)

    def translate_srt(self, src_language = 'en', dest_language='fa')->bool:
        self.split_srt()
        file_translate = f"{self.get_name()}_{dest_language}.srt"
        translator = Translator()
        model = 'abcdefghijklmnopqrstuvywzABCDEFGHIJKLMNOPQRSTUVYWZ[]"'
        try:
            with open(file_translate, '+a', encoding='utf-8') as srt, open(self.__name_split_file, 'r') as csv:
                data_file = csv.readlines()
                for line in data_file:
                    li_line = line.split(',')
                    for item in li_line:
                        print(item)
                        if item != "\n" and len(item) > 0:
                            if str(item)[0] in model:
                                result = translator.translate(str(item), dest_language, src_language)
                                text_trans = str(result.text)
                                srt.write(f"{text_trans}\n")
                            else:
                                if '.' in item:
                                    srt.write(f"{item.replace('.', ',')}\n")
                                else:
                                    srt.write(f"{item[0]}\n")
                        else:
                            srt.write(f"{item}\n")
            os.remove(self.__name_split_file)
            return True
        except:
            return False
        

print("Please waite....")  
test = TranslateSrt("12.srt")
if test.translate_srt():
    print("OK, success create file translate...")
else:
    print("Opps! Can not create file translate...")