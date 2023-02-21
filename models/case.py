class Case:
    def __init__(self, case_data:str):
        self.resolution_type:str = case_data.get('TIPO_RESOLUCION','')
        self.resolution_number:int = case_data.get('NUMERO_RESOLUCION','')
        self.resolution_year:int = case_data.get('ANNO_RESOLUCION','')
        self.resolution_BIS:bool = case_data.get('BIS_RESOLUCION','')
        
        self.registration_date:str = case_data.get('FECHA_REGISTRO','')
        self.numeric_type:str = case_data.get('TIPO_NUMERADO','')
        self.register_type:str = case_data.get('NUMERO_REGISTRO','')
        self.language:str = case_data.get('IDIOMA','')
        
        self.descriptive_synthesis:str = case_data.get('SINTESIS_DESCRIPTIVA','')
        self.analytic_synthesis:str = case_data.get('SINTESIS_ANALITICA','')
        self.boe_number:int = case_data.get('NUMERO_BOE','')
        self.boe_date:str = case_data.get('FECHA_BOE','')

        self.green_tome_number:int = case_data.get('NUMERO_TOMO_VERDE','')
        self.signature_date:str = case_data.get('FECHA_FIRMA','')
        self.boe_reference:str = case_data.get('REFERENCIA_BOE','')
        self.xml_boe_corrections:str = case_data.get('XML_CORRECCIONES_BOE','')

        self.last_update:str = case_data.get('ULTIMA_ACTUALIZACION','')
        self.content_irrelevant_for_internet:bool = case_data.get('CONTENIDO_IRRELEVANTE_PARA_INTERNET','')
        self.cache_date:str = case_data.get('FECHA_CACHE','')

