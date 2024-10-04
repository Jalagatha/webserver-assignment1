# Mugisha Ivan Jalagatha 24/HD05/22104U 
import socket
import os

def create_server_socket(port):
    """Create and configure a server socket to listen on the specified port."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', port))
    server_socket.listen(5)
    print(f"Server listening on port http://localhost:{port}' ")
    return server_socket

def handle_client_request(client_socket, server_socket):
    """Process client request, serve files or shutdown server based on the request."""
    try:
        request = client_socket.recv(1024).decode('utf-8')
        request_line = request.split('\n')[0]
        filename = request_line.split()[1]

        if filename in ['/shutdown.html', '/close_server.html']:
            send_response(client_socket, "Server is shutting down...", 200)
            client_socket.close()
            server_socket.close()
            print("Server shutdown initiated by client request.")
            return False

        # Default to serving 'index.html' if root is requested
        if filename == '/':
            filename = '/index.html'

        # Attempt to open and send the requested file
        file_path = os.path.join('htdocs', filename.lstrip('/'))
        with open(file_path, 'rb') as file:
            content = file.read()
            send_response(client_socket, content, 200)
    except FileNotFoundError:
        send_response(client_socket, "<h1>404 Not Found</h1>", 404)
    except Exception as e:
        print(f"Error handling request: {e}")
        send_response(client_socket, "<h1>500 Internal Server Error</h1>", 500)

    client_socket.close()
    return True

def send_response(client_socket, content, status_code):
    """Send an HTTP response to the client!."""
    status_messages = {
        200: "200 OK",
        404: "Page Not Found",
        500: "Internal Server Error"
    }
    response = f"HTTP/1.1 {status_messages[status_code]}\r\n"
    response += "Content-Type: text/html; charset=utf-8\r\n\r\n"
    response += content if isinstance(content, str) else content.decode('utf-8')
    client_socket.sendall(response.encode('utf-8'))

def run_server(port=8080):
    """Run the server and accept incoming connections."""
    server_socket = create_server_socket(port)
    continue_running = True
    while continue_running:
        client_socket, _ = server_socket.accept()
        continue_running = handle_client_request(client_socket, server_socket)

if __name__ == "__main__":
    run_server(8080)
