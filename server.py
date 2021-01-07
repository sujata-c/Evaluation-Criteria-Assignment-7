
import pickle, socket, os
from cryptography.fernet import Fernet
import tqdm

def deserialize_file(file_name):
    with open(file_name, 'rb') as file_object:
        raw_data = file_object.read()
        deserialized = pickle.loads(raw_data)
    print(deserialized)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
        print("Encrypted data :  ", encrypted_data)
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    print("Decrypted data :  ", decrypted_data)

    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def recieve():
    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
    PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
    BUFFER_SIZE = 4096
    """arguments passed to socket() specify the address 
    family and socket type. AF_INET is the Internet address 
    family for IPv4. SOCK_STREAM is the socket type for TCP"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        SEPARATOR = "<SEPARATOR>"
        s.bind((HOST, PORT))  # bind() is used to associate the socket with a specific network interface and port number
        s.listen()             # listen() enables a server to accept() connections
        conn, addr = s.accept() # accept() blocks and waits for an incoming connection
        # if below code is executed, that means the sender is connected
        with conn:
            print('Connected by', addr)
            #data = conn.recv(1024)
            received = conn.recv(BUFFER_SIZE).decode()
            filename, filesize = received.split(SEPARATOR)
                # remove absolute path if there is
            filename = os.path.basename(filename)
            # convert to integer
            filesize = int(filesize)
            print("recieved file: ",filename)
            #if not data:
             #       break
              #  conn.sendall(data)
        '''progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            for _ in progress:
                # read 1024 bytes from the socket (receive)
                bytes_read = conn.recv(BUFFER_SIZE)
                if not bytes_read:
                    # nothing is received
                    # file transmitting is done
                    break
                # write to the file the bytes we just received
                f.write(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))'''

        return filename

if __name__ == "__main__":
    file_name =recieve()
    print("key load")
    key = load_key()
    print(key)
    decrypt(file_name, key)
    deserialize_file(file_name)

