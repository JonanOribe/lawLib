class Fundamentals:
    def __init__(self, case_ref,fundamental_data:str):
        self.fundamental_id:str = case_ref+'-'+str(fundamental_data['ID'])
        self.case_ref:str = case_ref
        self.text:str = fundamental_data['TEXTO']