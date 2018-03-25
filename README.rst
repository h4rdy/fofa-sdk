FOFA SDK
========

The fofa SDK written in python3 makes it easy for developers to call fofa's API interface.

Installation
------------

``pip install pyfofa``
 
Only Python 3.6 is supported.
 
Example
-------

.. code-block:: pycon
    
    import pyfofa
    email = 'with.h4rdy@gmail.com'
    key = 'xxxxxxx'
    search = pyfofa.FofaAPI(email, key)
    for host, ip in search.get_data('cert="baidu.com"', 1, "host,ip")['results']:
        print(host, ip)