def possible_port_mine(socket_func): # GET PORT - global [Possible_Port_Connect]
    try:
        global Possible_Port_Connect
        Possible_N,Possible_Port_Connect = socket_func.getsockname()
    except:
        print("PLEASE CHECK YOUR INTERNET CONNECTION")
        print("\n")
        time.sleep(0.8)
        pass
