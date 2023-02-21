#!/usr/bin/env python3
''' http test '''
import unittest
import urllib.request


def http_connection(server, port):
    ''' web request '''
    return urllib.request.urlopen('http://'+server+':'+port)


class TestHTTP(unittest.TestCase):
    ''' test web server on port 8000 '''
    def test_webserver(self):
        ''' fail if http request fails'''
        self.assertTrue(http_connection("localhost", "8000"))


if __name__ == '__main__':
    unittest.main()
