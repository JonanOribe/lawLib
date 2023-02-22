class Article:
    def __init__(self, case_ref,article_data:str):
        self.article_id:str = case_ref+'-'+str(article_data['ID'])
        self.case_ref:str = case_ref
        self.articles:list[str] = article_data['ARTICULOS']