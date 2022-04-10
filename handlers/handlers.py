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
            self.allow_action = False
        except:
            log.error(f'An error occurred! {ExceptionLine()}')


class Student(BaseHandler):
    def init_method(self):
        self.required = {
            'post': ['name', 'family', 'passport_no', 'gender', 'country']
        }
        self.inputs = {
            # 'post': ['field1', 'field2', 'field3'],
            # 'put': ['field1', 'field2', 'field3']
        }
        self.tokenless = True


    def before_post(self):
        try:
            log.debug(self.params)
            return True
        except:
            log.error(f'An error occurred! {ExceptionLine()}')


class Country(BaseHandler):
    def init_method(self):
        self.required = {
            # 'post': ['name', 'family', 'passport_no', 'gender', 'country']
        }
        self.inputs = {
            # 'post': ['field1', 'field2', 'field3'],
            # 'put': ['field1', 'field2', 'field3']
        }
        self.tokenless = True

    def before_get(self):
        try:
            # log.debug(self.params)
            self.output['data']['list'] = [
                {'id': 1, 'name': 'Iran'},
                {'id': 2, 'name': 'Afghanistan'},
                {'id': 3, 'name': 'USA'},
                {'id': 4, 'name': 'Germany'}
            ]
            self.allow_action = False
            return True
        except:
            log.error(f'An error occurred! {ExceptionLine()}')

