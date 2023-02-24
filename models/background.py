class Background:
    def __init__(self, case_ref,background_data:str):
        self.background_id:str = case_ref+'-'+str(background_data['ID'])
        self.case_ref:str = case_ref
        self.text:str = background_data.get('TEXTO','')