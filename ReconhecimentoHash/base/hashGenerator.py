#import numpy as np;
import hashlib
from data_path import FilePath as fp


class HashGenerator:

    def __init__(self, file: list, output_path: str) -> None:
        self._file =  file
        self.output_file = output_path

    def  convertTo(self) -> int:
        pass   

    def extract_characteristic(self, hash: str):
        pass 

    def writeInFile(self, word: str, label: str, path: str):
        with open(path, "a") as file:
            file.write(f"{word}, {label}\n")
    
class MD5T(HashGenerator):

    def __init__(self, file: list) -> None:
        super().__init__(file, fp.MD5_HASH.value)

    def convertTo(self) -> int:
        try:
            for word in self._file:
                word = word.strip()
                word_md5 = hashlib.md5(word.encode('utf-8'))
                self.writeInFile(word_md5.hexdigest(), "MD5", fp.MD5_HASH.value ) 
            else:
                return 1
        except Exception as e:
            print(f"Falha ao converter {e}" )
            return 0

    def extract_characteristic(self, hash_md5: str):
        size: int = len(hash_md5)
        ocurrency: int = np.zeros(16)


class SHA1(HashGenerator):
    
    def __init__(self, file: list):
        super().__init__(file, fp.SHA_1.value)
    
    def convertTo(self) -> int:
        try:
            for word in self._file:
                word = word.strip()
                word_md5 = hashlib.sha1(word.encode('utf-8'))
                self.writeInFile(word_md5.hexdigest(), "SHA1", fp.SHA_1.value ) 
            else:
                return 1
        except Exception as e:
            print(f"Falha ao converter {e}" )
            return 0



with open(fp.RAW_DATA.value, "r", encoding='utf-8', errors='ignore') as file:    
    # data5 = MD5T(file.readlines())
    # data5.convertTo()

    dataSHA = SHA1(file.readlines())
    dataSHA.convertTo()


