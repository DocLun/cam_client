import cv2
import socket
import pickle
import struct

def send_stream(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    capture = cv2.VideoCapture(0)

    try:
        while True:
            ret, frame = capture.read()
            frame_data = pickle.dumps(frame)

            msg_size = struct.pack(">L", len(frame_data))
            client_socket.sendall(msg_size + frame_data)

            if cv2.waitKey(1) == ord('q'):
                break

    finally:
        capture.release()
        client_socket.close()
        cv2.destroyAllWindows()

# Запускаем клиент для отправки трансляции
send_stream('192.168.43.242', 8000)  # Замените на IP-адрес и порт сервера


