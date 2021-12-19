def check_common_port_status(set_port=False): # CHECK COMMON PORT - print
    try:
        if set_port == False:
            get_info_mine()
            Port_List = [20,21,22,23,25,53,65,67,
                          68,69,80,101,102,105,107,
                          109,110,111,113,115,117,119,
                          123,137,138,139,143,161,162,
                          163,164,174,177,178,179,389,
                          443,444,500,535,611,631,636,
                          765,767,873,989,990,992,993,3389,
                          994,995,1433,1521,2049,2081,2083,2086,
                          3306,3389,5432,5500,5800,8200,8000,8080]
            for s_port in Port_List:
                get_status_ip_port(Get_My_IP,s_port)
                if Get_IP_S == 0:
                    print("STATUS \033[1;32m%s\x1b[0m %s -- PORT %s" % ("OPEN",Get_IP_S,s_port))
                else:
                    print("STATUS \033[1;31m%s\x1b[0m %s -- PORT %s" % ("RESULT",Get_IP_S,s_port))
        elif set_port == True:
            get_info_mine()
            try:
                port_user = str(input("TYPE YOUR PORT TO CHECK ('/' to exit): "))
                time.sleep(1.2)
                if port_user == "/":
                    print("CANCELED")
                    time.sleep(0.8)
                    pass
                else:
                    int_port = int(port_user)
                    get_status_ip_port(Get_My_IP,int_port)
                    if Get_IP_S == 0:
                        print("STATUS \033[1;32m%s\x1b[0m %s -- PORT %s" % ("OPEN",Get_IP_S,port_user))
                    else:
                        print("STATUS \033[1;31m%s\x1b[0m %s -- PORT %s" % ("RESULT",Get_IP_S,port_user))
            except:
                print("CHECK YOUR INPUT, IT MUST BE A VALID PORT")
                print("\n")
                time.sleep(0.8)
                pass
        else:
            pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
