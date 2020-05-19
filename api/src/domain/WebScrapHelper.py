import SeleniumHelper

FILE_FOLDER_LOCAL_PATH = 'repository\\file\\'

KW_API = 'api'
KW_NAME = 'name'
KW_MAIN_URL = 'main-url'


class WebScrapHelper(SeleniumHelper.SeleniumHelper):

    DATASET_FILE_NAME = 'dataset'
    FAILED_DATASET_FILE_NAME = 'failed-dataset'

    def __init__(self,globals,**kwargs):
        SeleniumHelper.SeleniumHelper.__init__(self,globals,**kwargs)
        self.name = self.globals.getApiSetting(f'{KW_API}.{KW_NAME}')
        self.mainUrl = self.globals.getApiSetting(f'{KW_API}.{KW_MAIN_URL}')

    def run(self,commandList):
        self.globals.debug(f'[{self.globals.apiName}] run() method not implemented')

    def accessMainUrl(self):
        return self.accessUrl(self.mainUrl)
