def get_status_ip_port(ip_tar=str,port_tar=int): # GET IP STATUS - global [Get_IP_S]
    try:
        global Get_IP_S
        Socket_F = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        Get_IP_S = Socket_F.connect_ex((ip_tar,port_tar))
        Socket_F.close()
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION")
        print("\n")
        time.sleep(0.8)
        pass
