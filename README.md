
# Knowledge of Data Compression, Archiving, Marshalling, Cryptography and Networking


**Problem Definition**

Define Client and Server using Python Networking
Client should read data from the file, serialize the data and write into another file.
Encrypt the file using Python Cryptography module.
Transfer compressed database file over the network using Python code.
Server should decrypt the file and deserialize the data and Read data send by client

**Python Networking**
- What is Networking?

Computer Networking aims to study and analyze the communication process among various computing devices or computer systems that are linked, or networked together to exchange information and share resources.

- Internet Protocol

Mainly, we will be dealing with two major protocols over the internet:

1. User Datagram Protocol(UDP): UDP is a connectionless protocol. In this protocol data is sent over the internet as datagrams.
2. Transmission Control Protocol(TCP) : TCP is a connection oriented protocol.

- Socket API Overview

The primary socket API functions and methods in this module are:

- socket()
- bind()
- listen()
- accept()
- connect()
- connect_ex()
- send()
- recv()
- close()

![alt text](https://files.realpython.com/media/sockets-tcp-flow.1da426797e37.jpg)

**Python Cryptography**

*We will be using symmetric encryption, which means the same key we used to encrypt data, is also usable for decryption. There are a lot of encryption algorithms out there, the library we gonna use is built on top of AES algorithm.*

- Encryption : Encryption is the process of encoding an information in such a way that only authorized parties can access it. It is critically important because it allows you to securely protect data that you don't want anyone to see or access it.

            pip3 install cryptography
            from cryptography.fernet import Fernet
            
**Marshalling/Serialization**

- Object serialization is the process of converting state of an object into byte stream. This byte stream can further be stored in any file-like object such as a disk file or memory stream. It can also be transmitted via sockets etc. Deserialization is the process of reconstructing the object from the byte stream.

- Python refers to serialization and deserialization by terms pickling and unpickling respectively. The 'pickle' module bundled with Python’s standard library defines functions for serialization (dump() and dumps()) and deserialization (load() and loads()).

    - dumps() : returns a byte like object my marshalling a Python object. Only objects of standard data types are supported for marshalling. Unsupported types raise ValueError exception.

    - loads() : This function converts the byte like object to corresponding Python object. If the conversion doesn’t result in valid Python object, ValueError or TypeError may be raised.
    
    
**References**
-----------------------------------------
- [Real Python](https://realpython.com/)
- [StudyTonight](https://www.studytonight.com/)
- [knowledgehut](https://www.knowledgehut.com/)