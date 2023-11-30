class Dictum:
    def __init__(self, case_ref,dictum_data:str):
        self.dictum_id:str = case_ref+'-'+str(dictum_data['ID'])
        self.case_ref:str = case_ref
        self.title:str = dictum_data.get('TITULO','')
        self.header:str = dictum_data.get('CABECERA','')
        self.entry:str = dictum_data.get('ENTRADA','')
        self.text:str = dictum_data.get('TEXTO','')
