class Abstract:
    def __init__(self, case_ref,abstract_data:str):
        self.abstract_id:str = case_ref+'-'+str(abstract_data['ID'])
        self.case_ref:str = case_ref
        self.text:str = abstract_data['TEXTO']
        self.ffjj:str = abstract_data['FFJJ']