# agent.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import platform


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/shutdown':
            self.execute_command('shutdown')
        elif self.path == '/restart':
            self.execute_command('restart')
        elif self.path == '/sleep':
            self.execute_command('sleep')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Unknown command')

    def execute_command(self, command):
        os_name = platform.system()

        if os_name == 'Windows':
            if command == 'shutdown':
                os.system("shutdown /s /t 1")
            elif command == 'restart':
                os.system("shutdown /r /t 1")
            elif command == 'sleep':
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif os_name == 'Linux':
            if command == 'shutdown':
                os.system("shutdown now")
            elif command == 'restart':
                os.system("reboot")
            elif command == 'sleep':
                os.system("systemctl suspend")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"{command} command executed".encode())


def run():
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
