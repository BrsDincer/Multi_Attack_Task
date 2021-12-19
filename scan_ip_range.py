def scan_ip_range(ip_start=str,ip_end=str,port_start=int,port_end=int):
    try:
        get_info_mine()
        print("\n")
        print("SESSION HAS BEEN CREATED")
        print("\n")
        print("YOUR IP: ",Get_My_IP)
        print("\n")
        ip_all_sp = ip_start.split(".")
        sp_start = ip_start.split(".")[-1]
        start_indeed = ip_all_sp[0]+"."+ip_all_sp[1]+"."+ip_all_sp[2]
        sp_end = ip_end.split(".")[-1]
        for x_in_ip in range(int(sp_start),int(sp_end)+1):
            print("\n")
            print("TARGET IP: ",start_indeed+"."+str(x_in_ip))
            print("\n")
            time.sleep(0.8)
            for x_in_pr in range(port_start,port_end):
                try:
                    print("PORT: ",x_in_pr)
                    socket_main = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    res_stat = socket_main.connect((start_indeed+"."+str(x_in_ip),x_in_pr))
                    socket_main.settimeout(15)
                    if res_stat == 0:
                        print("\033[1;32m%s\x1b[0m" % ("OK"))
                        print("\n")
                        socket_main.close()
                    else:
                        print("UNEXPECTED: ", str(res_stat))
                        print("\n")
                        socket_main.close()
                except:
                    print("\033[1;31m%s\x1b[0m" % ("NOT CONNECTED - CLOSED"))
                    print("\n")
                    socket_main.close()
                    pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
