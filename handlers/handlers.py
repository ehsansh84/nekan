from base_handler import BaseHandler
from publics import ExceptionLine
from log_tools import log

class Login(BaseHandler):
    def init_method(self):
        self.required = {
            # 'post': ['field1']
        }
        # self.multilingual = ['field2']
        self.inputs = {
            # 'post': ['field1', 'field2', 'field3'],
            # 'put': ['field1', 'field2', 'field3']
        }
        self.tokenless = True


    def before_post(self):
        try:
            log.debug(self.params)
            log.debug(self.params['username'] == 'admin')
            log.debug(self.params['password'] == '1')
            if self.params['username'] == 'admin' and self.params['password'] == '1':
                self.success()
            else:
                self.fail()
        except:
            log.error(f'An error occurred! {ExceptionLine()}')

    