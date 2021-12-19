def ping_start(host_tar=str):
    try:
        get_info_mine()
        print("\n")
        print("SESSION HAS BEEN CREATED")
        print("YOUR IP: ",Get_My_IP)
        print("\n")
        time.sleep(1.2)
        if "http://" in host_tar or "https://" in host_tar:
            n_host_tar = host_tar.replace("http://","").replace("https://","")
            print("\n")
            att_ping = int(input("SPECIFY PING NUMBER TO SEND: "))
            print("PLEASE WAIT FOR THE PROCESS")
            print("\n")
            time.sleep(1.2)
            print("\n")
            if att_ping > 0:
                if name == "nt":
                    com_ping = f"ping {n_host_tar} -n {att_ping}"
                    response_com = os.popen(com_ping)
                    for x_l_r in response_com.readlines():
                        if x_l_r.count("TTL"):
                            print("%s -- \033[1;32m%s\x1b[0m" % (n_host_tar,"GOT RESPONSE - OK"))
                            print(x_l_r)
                        else:
                            pass
                else:
                    com_ping = f"ping {n_host_tar} -c {att_ping}"
                    response_com = os.popen(com_ping)
                    for x_l_r in response_com.readlines():
                        if x_l_r.count("TTL"):
                            print("%s -- \033[1;32m%s\x1b[0m" % (n_host_tar,"GOT RESPONSE - OK"))
                            print(x_l_r)
                        else:
                            pass
            else:
                print("VALUE MUST BE SUPPLIED")
                print("\n")
                pass
        else:
            print("\n")
            att_ping = int(input("SPECIFY PING NUMBER TO SEND: "))
            print("\n")
            if att_ping > 0:
                if name == "nt":
                    com_ping = f"ping {host_tar} -n {att_ping}"
                    response_com = os.popen(com_ping)
                    for x_l_r in response_com.readlines():
                        if x_l_r.count("TTL"):
                            print("%s -- \033[1;32m%s\x1b[0m" % (host_tar,"GOT RESPONSE: OK"))
                            print(x_l_r)
                        else:
                            pass
                else:
                    com_ping = f"ping {host_tar} -c {att_ping}"
                    response_com = os.popen(com_ping)
                    response_com = os.popen(com_ping)
                    for x_l_r in response_com.readlines():
                        if x_l_r.count("TTL"):
                            print("%s -- \033[1;32m%s\x1b[0m" % (host_tar,"GOT RESPONSE: OK"))
                            print(x_l_r)
                        else:
                            pass
            else:
                print("VALUE MUST BE SUPPLIED")
                print("\n")
                pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
