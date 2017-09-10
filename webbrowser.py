from __future__ import absolute_import
import webbrowser
from urlparse import urlparse

from kalliope import Utils
from kalliope.core.NeuronModule import (
    NeuronModule,
    MissingParameterException,
    InvalidParameterException)

OPTIONS = {
    'current': 0,
    'new': 1,
    'tab': 2
}

class Webbrowser(NeuronModule):
    def __init__(self, **kwargs):
        super(Webbrowser, self).__init__(**kwargs)

        self.url = kwargs.get('url', None)
        self.option = kwargs.get('option', 'tab')

        if self._is_parameters_ok():
            webbrowser.open(self.url, OPTIONS[self.option])

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron.
        :return: True if parameters are ok, raise an exception otherwise.

        .. raises:: MissingParameterException, InvalidParameterException
        """
        if self.url is None:
            raise MissingParameterException("Webbrowser needs an url")
        if self.url_check(self.url) is False:
            raise InvalidParameterException("Webbrowser: invalid url")
        if self.option not in OPTIONS:
            raise InvalidParameterException("Webbrowser: invalid option")
        return True

    def url_check(self, url):
        try:
            result = urlparse(url)
            if all([result.scheme, result.netloc]):
                return True
            else:
                return False
        except:
            return False