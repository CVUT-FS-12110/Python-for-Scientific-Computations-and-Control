"""
This file contains multiple examples divided by docsrings. 

Uncomment the block of code you want to run before you run the code.

Warning, if you are unable to run server examples because of "the port is occupied error", use different port - 8001, 8002...

"""



"""
HTTP server - simple example

This is simple localy running server on http://127.0.0.1:8000 - this server is serving folder from where the script si running.

"""
# import http.server
# import socketserver
#
# PORT = 8000
# ADDRESS = "127.0.0.1"
#
# Handler = http.server.SimpleHTTPRequestHandler
# httpd = socketserver.TCPServer((ADDRESS, PORT), Handler)
#
# print("Serving at port", PORT)
# httpd.serve_forever()



"""
Server test:

You can test the server with following code (run it from different console while the server is up).
"""
# import requests

# r = requests.get("http://127.0.0.1:8000/")

# print(r.status_code)
# print(r.text)




"""
Server that returns web pages.


The next server example serve simple webpages.
"""
# import http.server
# import socketserver
#
# class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
#
#     def do_GET(self):
#         """Respond to a GET request."""
#         if self.path == "/":
#             self.send_response(200)
#             self.send_header("Content-type", "text/html")
#             self.end_headers()
#             message = "This is the main page."
#         elif self.path in ["/help/", "/help"]:
#             self.send_response(200)
#             self.send_header("Content-type", "text/html")
#             self.end_headers()
#             message = "This is page with help."
#         else:
#             self.send_response(404)
#             self.send_header("Content-type", "text/html")
#             self.end_headers()
#             message = "Page not found. See /help/ for help."
#         # write message
#         self.wfile.write(message.encode())
#
#
# PORT = 8001
# ADDRESS = "127.0.0.1"
#
# httpd = socketserver.TCPServer((ADDRESS, PORT), MyRequestHandler)
#
# print("Serving at port", PORT)
# httpd.serve_forever()



"""
Server example with POST handler


This server is able to handle POST request and process it.
"""
# import http.server
# import socketserver
# import cgi
#
# class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
#
#     def do_POST(self):
#         # get params send as data
#         form = cgi.FieldStorage(
#             fp=self.rfile,
#             headers=self.headers,
#             environ={'REQUEST_METHOD':'POST',
#                         'CONTENT_TYPE':self.headers['Content-Type'],
#             })
#         query_dict = {key: form.getvalue(key) for key in form.keys()}
#         # prepare response
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         self.wfile.write(("Parameters sent:"+str(query_dict)).encode())
#
#     def do_GET(self):
#         """Respond to a GET request."""
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         html_form = """
#         <form method="post" action="/">
#           <input type="text" name="a" value="1"><br>
#           <input type="submit" value="Send">
#         </form>
#         """
#         self.wfile.write(html_form.encode())
#
# PORT = 8002
# ADDRESS = "127.0.0.1"
#
# httpd = socketserver.TCPServer((ADDRESS, PORT), MyRequestHandler)
#
# print("Serving at port", PORT)
# httpd.serve_forever()

"""
POST test

This sample can be used to test the POST handling server (you need to keep the server running).
"""
# import requests
#
# parameters = {
#     "a": 2,
#     "b": 3,
#     "c": 4,
# }
#
# r = requests.post("http://127.0.0.1:8000/", data=parameters)
#
# print(r.status_code, r.text)
