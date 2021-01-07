
import pickle, os
from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def file_read_serialize_and_wite(file_name1, file_name2):

    with open(file_name1, 'rb') as fin:
        with open(file_name2, "wb") as fout:
            for line in fin:
                pickle.dump(line, fout)
                #fout.write(line)

def encryption(file_name2):
    # generate and write a new key
    write_key()
    # load the previously generated key
    key = load_key()
    f = Fernet(key)
    with open(file_name2, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(file_name2, "wb") as file:
        file.write(encrypted_data)


import socket

def send(file_name2):
    SEPARATOR = "<SEPARATOR>"
    HOST = '127.0.0.1'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    filesize = os.path.getsize(file_name2)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"[+] Connecting to {HOST}:{PORT}")
        s.connect((HOST, PORT))
        print("[+] Connected.")

        #s.sendall(b'Hello, world')
        # send the filename and filesize
        s.send(f"{file_name2}{SEPARATOR}{filesize}".encode())
        data = s.recv(1024)
    print('Received', repr(data))

if __name__ == '__main__':
    print("1. Read data from a file, serialize it  and write to another file")
    file_name1 = str(input("Enter file name to read from(eg. abc.txt):  "))
    file_name2 = str(input("Enter file name to write into(eg. abc.txt):  "))
    file_read_serialize_and_wite(file_name1, file_name2)

    print("2. Encryption of th file")
    encryption(file_name2)
    print("3. send encrypted file from client to server")
    send(file_name2)