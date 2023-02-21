class Case:
    def __init__(self, case_data:str):
        self.resolution_type:str = case_data['TIPO_RESOLUCION']
        self.resolution_number:int = case_data['NUMERO_RESOLUCION']
        self.resolution_year:int = case_data['ANNO_RESOLUCION']
        self.resolution_BIS:bool = case_data['BIS_RESOLUCION']
        
        self.registration_date:str = case_data['FECHA_REGISTRO']
        self.numeric_type:str = case_data['TIPO_NUMERADO']
        self.register_type:str = case_data['NUMERO_REGISTRO']
        self.language:str = case_data['IDIOMA']
        
        self.descriptive_synthesis:str = case_data['SINTESIS_DESCRIPTIVA']
        self.analytic_synthesis:str = case_data['SINTESIS_ANALITICA']
        self.boe_number:int = case_data['NUMERO_BOE']
        self.boe_date:str = case_data['FECHA_BOE']

        self.green_tome_number:int = case_data['NUMERO_TOMO_VERDE']
        self.signature_date:str = case_data['FECHA_FIRMA']
        self.boe_reference:str = case_data['REFERENCIA_BOE']
        self.xml_boe_corrections:str = case_data['XML_CORRECCIONES_BOE']

        self.last_update:str = case_data['ULTIMA_ACTUALIZACION']
        self.content_irrelevant_for_internet:bool = case_data['CONTENIDO_IRRELEVANTE_PARA_INTERNET']
        self.cache_date:str = case_data['FECHA_CACHE']

