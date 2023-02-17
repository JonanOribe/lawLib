class Dictum:
    def __init__(self, case_ref,dictum_data:str):
        self.case_ref:str = case_ref
        self.title:str = dictum_data['TITULO']
        self.header:str = dictum_data['CABECERA']
        self.entry:str = dictum_data['ENTRADA']
        self.text:str = dictum_data['TEXTO']
