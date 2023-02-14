class Magistrate:
    def __init__(self, case_ref,magistrate_data:str):
        self.case_ref:str = case_ref
        self.name:str = magistrate_data['MAGISTRADOS']['NOMBRE_PRESENTACION']