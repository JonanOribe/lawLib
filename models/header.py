class Header:
    def __init__(self, case_ref,header_data:str):
        self.header_id:str = case_ref+'-'+str(header_data['ID'])
        self.case_ref:str = case_ref
        self.text:str = header_data['COMPONENTES']