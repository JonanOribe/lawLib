class Header:
    def __init__(self, case_ref,header_data:str):
        self.case_ref:str = case_ref
        self.text:str = header_data['COMPONENTES']