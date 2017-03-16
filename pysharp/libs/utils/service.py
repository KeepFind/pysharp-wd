# coding:utf-8

class PageCalculator():
    '''分页索引值计算'''

    def start(self,pindex: int, psize: int) -> int:
        return (pindex - 1) * psize

    def end(self,pindex: int, psize: int) -> int:
        return pindex * psize


pagecal = PageCalculator()


# service_result = {'data': '', 'ruleviolations': []}
#
# rule_violation = {'parametername': '', 'errormessage': ''}



class ServiceResult:
    def __init__(self):
        self._data = ''
        self._ruleviolations = []

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def ruleviolations(self):
        return self._ruleviolations


class RuleViolation:
    def __init__(self, parametername, errormessage):
        self.parametername = parametername
        self.errormessage = errormessage


def is_empty(value):
    return len(value) == 0
