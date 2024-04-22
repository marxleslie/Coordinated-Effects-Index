# -*- coding: utf-8 -*-

from __future__ import absolute_import, print_function, unicode_literals
from wolframclient.evaluation import WolframCloudSession

def call(x):
    """ Call the API using function input parameter values.
    If the API was deployed with an export formats set to JSON or WXF, the result is often a native Python type.
    """
    with WolframCloudSession() as session:
        api_response = session.call('https://www.wolframcloud.com/obj/6cb9674a-3203-40af-9a5d-1efd7e36a642', {'x' : x})
        return api_response.get()

print(call(2))
    

