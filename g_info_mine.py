def get_info_mine(): # GET IP - global [Get_My_IP,Get_My_Host]
    try:
        global Get_My_IP,Get_My_Host
        Get_My_Host = socket.gethostname()
        Get_My_IP = socket.gethostbyname(Get_My_Host)
    except:
        print("PLEASE CHECK YOUR INTERNET CONNECTION")
        print("\n")
        time.sleep(0.8)
        pass
