#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random


class Servidor (webapp.webApp):
    def parse(self, request):
        return None

    def process(self, parsedRequest):
        return("200 OK", "<html><body><h1>Hola</h1>" +
               "<a href='" + str(random.randrange(10000000)) +
               "'>Dame otra</a>" + "</body></html>")

if __name__ == "__main__":
    serv = Servidor("localhost", 1234)
