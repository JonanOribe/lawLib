class Article:
    def __init__(self, case_ref,article_data:str):
        self.case_ref:str = case_ref
        self.articles:list[str] = article_data['ARTICULOS']