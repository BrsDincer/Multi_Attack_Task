import socket, os, requests, json, time, random, threading
from bs4 import BeautifulSoup
from optparse import OptionParser as OPTp
from os import name
from queue import Queue


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
    

def possible_port_mine(socket_func): # GET PORT - global [Possible_Port_Connect]
    try:
        global Possible_Port_Connect
        Possible_N,Possible_Port_Connect = socket_func.getsockname()
    except:
        print("PLEASE CHECK YOUR INTERNET CONNECTION")
        print("\n")
        time.sleep(0.8)
        pass


def tcp_or_udp_check(port_number=int):
    try:
        Port_Result_TCP = socket.getservbyport(port_number,"tcp")
        Result_Port = Port_Result_TCP
        return Result_Port + " " +"TCP"
    except:
        pass
    try:
        Port_Result_UDP = socket.getservbyport(port_number,"udp")
        Result_Port = Port_Result_UDP
        return Result_Port + " " +"UDP"
    except:
        Result_Port = "NOT FOUND"
        return Result_Port
        pass
    

def user_agent_get(): # GET USER AGENT - global [all_list_agent]
    try:
        global all_list_agent
        Json_Tar="user_agent_all.json"
        f_op = open(Json_Tar)
        j_op = json.loads(f_op.read())
        all_list_agent = []
        for x_value in j_op["user_agents"]:
            for ix_values in j_op["user_agents"][x_value]:
                for ixl_values in j_op["user_agents"][x_value][ix_values]:
                    for ixlp_values in j_op["user_agents"][x_value][ix_values][ixl_values]:
                        all_list_agent.append(ixlp_values)
    except:
        print("PLEASE CHECK YOUR INTERNET CONNECTION OR FILE DIRECTORY")
        print("\n")
        time.sleep(0.8)
        pass


def read_file_from(file_name=str):
    try:
        global x_file
        with open(file_name,"r") as file_tar:
            x_file = []
            for line_x in file_tar:
                try:
                    ext_tar = line_x.strip()
                    x_file.append(ext_tar)
                except:
                    pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION OR DIRECTORIES")
        print("\n")
        time.sleep(0.8)
        pass
            

def read_file_xss(file_name=str):
    try:
        global x_file
        with open(file_name,"r",errors="replace") as file_tar:
            x_file = []
            for line_x in file_tar:
                try:
                    ext_tar = line_x.strip()
                    x_file.append(ext_tar)
                except:
                    pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION OR DIRECTORIES")
        print("\n")
        time.sleep(0.8)
        pass
            

def check_status_code(url_x=str):
    try:
        global Status_Response
        user_agent_get()
        User_Header = {
                "User-Agent":f"{random.choice(all_list_agent)}"
                }
        Status_Response = requests.get(url_x,headers=User_Header,timeout=22).status_code
        if Status_Response == 200:
            print("\033[1;32m%s\x1b[0m -- %s" % (url_x,Status_Response))
        elif Status_Response == 404:
            print("\033[1;33m%s\x1b[0m -- %s" % (url_x,Status_Response))
        elif Status_Response == 403:
            print("\033[1;31m%s\x1b[0m -- %s" % (url_x,Status_Response))
        elif Status_Response == 503:
            print("\033[1;36m%s\x1b[0m -- %s" % (url_x,Status_Response))
        elif Status_Response == 501:
            print("\033[1;37m%s\x1b[0m -- %s" % (url_x,Status_Response))
        else:
            print("%s -- \033[1;38m%s\x1b[0m" % (url_x,Status_Response))
    except:
        print("NOT IN POOL: "+url_x)
        pass   


def get_proxies(): # GET PROXY - global [IP_L,PR_L]
    try:
        global IP_L,PR_L
        Rand_Url_Main = "https://free-proxy-list.net/"
        user_agent_get()
        user_agent_all = {"User-Agent":f"{random.choice(all_list_agent)}"}
        Soup_Main = BeautifulSoup(requests.get(Rand_Url_Main,headers=user_agent_all).content, "html.parser")
        IP_L = []
        PR_L = []
        i_count_spoof = 0
        for tab_all in Soup_Main.find("table",class_="table table-striped table-bordered"):
            tr_all = tab_all.find_all("tr")
            for x_tr in tr_all:
                td_all = x_tr.find_all("td")
                for x_td in td_all:
                    i_count_spoof += 1
                    if i_count_spoof == 1:
                        IP_M = x_td.text
                        IP_L.append(str(IP_M))
                    elif i_count_spoof == 2:
                        PR_M = x_td.text
                        PR_L.append(str(PR_M))
                i_count_spoof = 0
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION")
        print("\n")
        time.sleep(0.8)
        pass


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
    

def get_access_to_site(site_tar=str): # ACCESS - global [proxy_main]
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        print("\n")
        time.sleep(0.8)
        global proxy_main
        get_proxies()
        user_agent_get()
        i_value_stop = 0
        if i_value_stop == 0:
            for x_ip, x_pr in zip(IP_L,PR_L):    
                proxy_dict_new = {"http":f"http://{x_ip}"+":"+f"{x_pr}",
                                              "https":f"https://{x_ip}"+":"+f"{x_pr}"}
                User_Header_List = {
                                        "User-Agent":f"{random.choice(all_list_agent)}"
                                        }
                print("\n")
                print("%s \033[1;34m%s\x1b[0m : \033[1;34m%s\x1b[0m" % ("CHECKING PROXY TO CONNECT",x_ip, x_pr))
                try:
                    if "http://" in site_tar or "https://" in site_tar:
                        print("YOUR SITE: ",site_tar)
                        REQ_URL = requests.get(site_tar, proxies=proxy_dict_new, headers=User_Header_List, timeout=32)
                        if REQ_URL.status_code == 200: 
                            # print("PROXY IS ACTIVE")
                            proxy_main = {"http":proxy_dict_new.get("http"),
                                                                  "https":proxy_dict_new.get("https")}
                            html_content = REQ_URL.text
                            # print(html_content)
                            i_value_stop += 1
                            f_open = open("text_target.html","w")
                            f_open.write(html_content)
                            print("\n")
                            print("\033[1;32m%s\x1b[0m" % ("CONNECTED AND SAVED"))
                            time.sleep(0.8)
                            print("PLEASE CHECK THE FOLDER")
                            print("YOUR CURRENT DIRECTORY: ",os.getcwd())
                            time.sleep(0.8)
                            f_open.close()
                            print("USE TO CONNECT LOCALY IF YOU NEED: ",x_ip + ":" + x_pr)
                            print("\n")
                            time.sleep(0.8)
                            break
                        else:     
                            print("\033[1;34m%s\x1b[0m" % ("NOT CONNECTED, PASSING FOR NEXT"))
                            print("\n")
                            pass
                    elif "http://" not in site_tar and "https://" not in site_tar:
                        site_tar = "http://" + site_tar
                        print("YOUR SITE: ",site_tar)
                        REQ_URL = requests.get(site_tar, proxies=proxy_dict_new, headers=User_Header_List, timeout=42)
                        if REQ_URL.status_code == 200: 
                            proxy_main = {"http":proxy_dict_new.get("http"),
                                                                  "https":proxy_dict_new.get("https")}
                            html_content = REQ_URL.text
                            i_value_stop += 1
                            f_open = open("tex_gh.html","w")
                            f_open.write(html_content)
                            print("\n")
                            print("\033[1;32m%s\x1b[0m" % ("CONNECTED AND SAVED"))
                            time.sleep(0.8)
                            print("PLEASE CHECK THE FOLDER")
                            print("YOUR CURRENT DIRECTORY: ",os.getcwd())
                            time.sleep(0.8)
                            f_open.close()
                            print("USE TO CONNECT LOCALY IF YOU NEED: ",x_ip + ":" + x_pr)
                            print("\n")
                            time.sleep(0.8)
                            break
                        else:     
                            print("\033[1;34m%s\x1b[0m" % ("NOT CONNECTED, PASSING FOR NEXT"))
                            print("\n")
                            pass
                    else:
                        pass
                except:
                    print("\033[1;34m%s\x1b[0m" % ("NOT CONNECTED, PASSING FOR NEXT"))
                    time.sleep(0.8)
                    pass
        if i_value_stop == 0:
            print("CHECK THE SITE THAT YOU SPECIFIED OR INTERNET CONNECTION")
            print("MAYBE THE WEBSITE IS NOT ACTIVE")
            print("\n")
        else:
            pass
    except:
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
    

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
    

def reading_url_pdf(url_name=str,saving_file_name=str):
    try:
        if ".pdf" in url_name and ".pdf" in saving_file_name:
            req_url = requests.get(url_name,stream=True)
            save_file = open(saving_file_name,"wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        elif ".pdf" not in url_name and ".pdf" not in saving_file_name:
            req_url = requests.get(url_name+".pdf",stream=True)
            save_file = open(saving_file_name+".pdf","wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        elif ".pdf" in url_name and ".pdf" not in saving_file_name:
            req_url = requests.get(url_name,stream=True)
            save_file = open(saving_file_name+".pdf","wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        elif ".pdf" not in url_name and ".pdf" in saving_file_name:
            req_url = requests.get(url_name+".pdf",stream=True)
            save_file = open(saving_file_name,"wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        else:
            print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
            print("\n")
            time.sleep(0.8)
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
             
    
def bind_process(ip_host=str,listen_c=int,reverse_p=False):
    try:
        if reverse_p == False:
            Socket_B = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            Socket_B.setblocking(1)
            Socket_B.bind((ip_host,0))
            possible_port_mine(Socket_B)
            Socket_B.listen(listen_c)
            print("\n")
            print("SESSION HAS BEEN CREATED")
            print("\n")
            get_info_mine()
            Result_Port = tcp_or_udp_check(Possible_Port_Connect)
            print('YOUR IP ADDRESS: ',Get_My_IP)
            print('YOUR CONNECTION DEVICE: ',Get_My_Host)
            print('YOUR PORT TO CONNECT: ',Possible_Port_Connect)
            print('PORT INFORMATION: ',Result_Port)
            print("\n")
            time.sleep(1.2)
            recv_f_size = 1024
            cur_dir_name = os.getcwd()
            process_id = os.getpid()
            print("YOUR CURRENT DIRECTORY: ",cur_dir_name)
            print("YOUR PROCESS ID: ",process_id)
            time.sleep(1.2)
            print("\n")
            save_to_name = str(input("[TYPE] YOUR NEW FILE NAME: "))
            print("\n")
            print("PLEASE WAIT FOR CONNECTION")
            print("\n")
            while True:
                conn_c,add_c = Socket_B.accept()
                print(f"USER HAS BEEN CONNECTED - INFO: {add_c}")
                time.sleep(1.2)
                get_user_input_format = conn_c.recv(recv_f_size).decode()
                get_user_input_format = str(get_user_input_format).upper().replace(" ","")
                print("YOU GOT RESPONSE FROM CONNECTION")
                print("YOU WILL GET THIS FORMAT: ",get_user_input_format)
                print("\n")
                time.sleep(1.2)
                if get_user_input_format == "PDF":
                    bt_read = conn_c.recv(recv_f_size).decode()
                    reading_url_pdf(bt_read,save_to_name)
                    conn_c.close()
                    Socket_B.close()
                    break
                elif get_user_input_format == "TXT":
                    f_read = open(f"{save_to_name}.txt","w")
                    bt_read = conn_c.recv(recv_f_size).decode()
                    print("RECEIVED")
                    time.sleep(1.2)
                    reading_q = str(input("YOU WANT TO SEE YOUR MESSAGE ON THE CONSOLE [Y/N]: ")).upper().replace(" ","")
                    print("\n")
                    time.sleep(1.2)
                    if reading_q == "Y":
                        print(bt_read)
                        print("\n")
                        if not bt_read:
                            print("EMPTY FILE, CHECK YOUR CONNECTION OR PROCESS")
                            print("\n")
                            time.sleep(0.8)
                            break
                        f_read.write(bt_read)
                        print("PROCESS HAS BEEN DONE SUCCESSFULLY, CHECK YOUR FILE")
                        print("\n")
                        f_read.close()
                        conn_c.close()
                        Socket_B.close()
                        time.sleep(0.8)
                        break
                    else:
                        if not bt_read:
                            print("EMPTY FILE, CHECK YOUR CONNECTION OR PROCESS")
                            print("\n")
                            break
                        f_read.write(bt_read)
                        print("PROCESS HAS BEEN DONE SUCCESSFULLY, CHECK YOUR FILE")
                        print("\n")
                        f_read.close()
                        conn_c.close()
                        Socket_B.close()
                        time.sleep(0.8)
                        break   
                else:
                    conn_c.close()
                    Socket_B.close()
                    time.sleep(0.8)
                    break
        elif reverse_p == True:
            Socket_B = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            Socket_B.setblocking(1)
            Socket_B.bind((ip_host,0))
            possible_port_mine(Socket_B)
            Socket_B.listen(listen_c)
            print("\n")
            print("SESSION HAS BEEN CREATED")
            print("\n")
            get_info_mine()
            Result_Port = tcp_or_udp_check(Possible_Port_Connect)
            print('YOUR IP ADDRESS: ',Get_My_IP)
            print('YOUR CONNECTION DEVICE: ',Get_My_Host)
            print('YOUR PORT TO CONNECT: ',Possible_Port_Connect)
            print('PORT INFORMATION: ',Result_Port)
            print("\n")
            time.sleep(1.2)
            recv_f_size = 1024
            cur_dir_name = os.getcwd()
            process_id = os.getpid()
            print("YOUR CURRENT DIRECTORY: ",cur_dir_name)
            print("YOUR PROCESS ID: ",process_id)
            time.sleep(1.2)
            print("\n")
            print("PLEASE WAIT FOR CONNECTION")
            print("\n")
            while True:
                conn_c,add_c = Socket_B.accept()
                print(conn_c.recv(recv_f_size).decode() + " HAS BEEN STARTED")
                time.sleep(0.8)
                print("\n")
                command_type = str(input("TYPE YOUR COMMAND TO SEND: "))
                print("\n")
                conn_c.send(command_type.encode())
                print(conn_c.recv(recv_f_size).decode())
                print("\n")
                time.sleep(1.5)
                print("PROCESS HAS BEEN DONE SUCCESSFULLY")
                print("\n")
                conn_c.close()
                Socket_B.close()
                time.sleep(0.8)
                break
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
    

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
            

def run_port_sc(tar_in_user):
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        time.sleep(1.2)
        print("THIS SECTION IS FOR FAST SCANNING. PLEASE MAKE SURE ABOUT PROCESSES.")
        time.sleep(1.2)
        print("\n")
        th_l = threading.Lock()
        if "http://" in tar_in_user or "https://" in tar_in_user:
            new_h = tar_in_user.replace("http://","").replace("https://","")
            first_range_pt = int(input("FIRST PORT OF RANGE YOU DESIRE: "))
            second_range_pt = int(input("SECOND PORT OF RANGE YOU DESIRE: "))
            tar_IP = socket.gethostbyname(new_h)
            print("\n")
            print('SITE ON: ', new_h)
            print('IP ON: ', tar_IP)
        else:
            first_range_pt = int(input("FIRST PORT OF RANGE YOU DESIRE: "))
            second_range_pt = int(input("SECOND PORT OF RANGE YOU DESIRE: "))
            tar_IP = socket.gethostbyname(tar_in_user)
            print("\n")
            print('SITE ON: ', tar_in_user)
            print('IP ON: ', tar_IP)
        time.sleep(1.2)
        print("\n")
        time.sleep(1.2)
        def port_scan_main(port_tar=int):
            socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_main.settimeout(5)
            try:
              conn_main = socket_main.connect((tar_IP, port_tar))
              with th_l:
                  print(port_tar, 'OPEN')
              conn_main.close()
            except:
                pass
        def threader_running():
            while True:
              w_paid = q.get()
              port_scan_main(w_paid)
              q.task_done()
        q = Queue()
        time_s = time.time()
        for x in range(100):
            t_main = threading.Thread(target = threader_running)
            t_main.daemon = True
            t_main.start()
        for x_l in range(first_range_pt, second_range_pt+1):
            q.put(x_l)
        q.join()
        print("\n")
        print('PROCESS IS DONE ', "%.2f" % (time.time() - time_s), " TIME")
        print("\n")
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION OR PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
    

def dns_rec_search(tar_site=str):
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        print("\n")
        time.sleep(0.8)
        note_message ="""
        
        [G]ENERAL --> On the most preferred
        [L]ONG --> On detailed parameters
        [A]LL --> On all possibilities
        
        
        """ 
        file_name_dic = {"general":"dns_name.txt",
                         "long":"dns_long.txt",
                         "all":"dns_all.txt"}
        print("\n")
        print(note_message)
        time.sleep(1.2)
        print("\n")
        ask_pross_con = str(input("HOW DO YOU WANT TO PERFORM A SEARCH [G]/[L]/[A]: ")).upper().replace(" ","")
        print("\n")
        if ask_pross_con == "G":
            read_file_from(file_name_dic.get("general"))
            if "http://" in tar_site or "https://" in tar_site:
                new_tar = tar_site.replace("http://","").replace("https://","").replace("www.","")
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+new_tar
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = new_tar.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
            elif "www." in tar_site:
                new_tar = tar_site.replace("http://","").replace("https://","").replace("www.","")
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+new_tar
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = new_tar.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
            else:
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+tar_site
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = tar_site.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass    
        elif ask_pross_con == "L":
            read_file_from(file_name_dic.get("long"))
            if "http://" in tar_site or "https://" in tar_site:
                new_tar = tar_site.replace("http://","").replace("https://","").replace("www.","")
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+new_tar
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = new_tar.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
            elif "www." in tar_site:
                new_tar = tar_site.replace("http://","").replace("https://","").replace("www.","")
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+new_tar
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = new_tar.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
            else:
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+tar_site
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = tar_site.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
        elif ask_pross_con == "A":
            read_file_from(file_name_dic.get("all"))
            if "http://" in tar_site or "https://" in tar_site:
                new_tar = tar_site.replace("http://","").replace("https://","").replace("www.","")
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+new_tar
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = new_tar.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
            elif "www." in tar_site:
                new_tar = tar_site.replace("http://","").replace("https://","").replace("www.","")
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+new_tar
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = new_tar.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
            else:
                for x_sub in x_file:
                    ex_tar = "http://"+str(x_sub)+"."+tar_site
                    print("\n")
                    check_status_code(ex_tar)
                    try:
                        s_main = tar_site.split("/")
                        print(str(x_sub)+"."+s_main[0])
                        Get_S_IP = socket.gethostbyname(str(x_sub)+"."+s_main[0])
                        print("IP FOUND: \033[1;32m%s\x1b[0m" % (Get_S_IP))
                        print("\n")
                    except:
                        pass
        else:
            print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION")
            print("\n")
            time.sleep(0.8)
            pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION")
        print("\n")
        time.sleep(0.8)
        pass
    

def simple_request_prox(prox_dict=dict):
    try:
        global Status_Response
        user_agent_get()
        User_Header = {
            "User-Agent":f"{random.choice(all_list_agent)}"
            }
        Status_Response = requests.get('https://ipinfo.io/json',headers=User_Header,proxies=prox_dict,timeout=22).status_code
    except:
        pass
    

def curl_get_prox(tar_url=str,prox_dom=str):
    try:
        global status_reading
        command_prob = os.popen("curl -k -s --proxy %s %s -m %s" % (prox_dom, tar_url, 30))
        status_reading = command_prob.read()
        print(status_reading)
    except:
        pass

    
def curl_get_norm(tar_url=str):
    try:
        global status_reading
        command_prob = os.popen("curl -k -s %s -m %s" % (tar_url,30))
        status_reading = command_prob.read()
        print(status_reading)
    except:
        pass
    

def head_curl_hunter(tar_site=str):
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        print("\n")
        time.sleep(0.8)
        get_proxies()
        i_value_stop = 0
        if "http://" in tar_site or "https://" in tar_site:
            new_exp = tar_site.replace("http://","").replace("https://","").replace("www.","")
            tar_exp = "https://"+new_exp
            print("\n")
            print("TARGET SITE: ",tar_exp)
            print("\n")
            if i_value_stop == 0:
                for x_ip,x_pr in zip(IP_L,PR_L):
                    try:
                        proxy_dict_new = {"http":f"http://{x_ip}"+":"+f"{x_pr}",
                                          "https":f"https://{x_ip}"+":"+f"{x_pr}"}
                        simple_request_prox(proxy_dict_new)
                        if Status_Response == 200:
                            curl_get_prox(tar_exp,str(proxy_dict_new['http']))
                            if len(status_reading) != 0 and status_reading != None and "301" not in status_reading:
                                print("\n")
                                print("\033[1;32m%s\x1b[0m" % ("FOUND"))
                                print("\n")
                                file_ext = open("target_site.html","w")
                                file_ext.write(status_reading)
                                file_ext.close()
                                i_value_stop += 1
                                break
                        else:
                            pass
                    except:
                        print("\033[1;33m%s\x1b[0m" % ("TRYING TO CONNECT, PLEASE WAIT"))
            else:
                tar_exp = "https://"+tar_site
                print("\n")
                print("TARGET SITE: ",tar_exp)
                print("\n")
                if i_value_stop == 0:
                    for x_ip,x_pr in zip(IP_L,PR_L):
                        try:
                            proxy_dict_new = {"http":f"http://{x_ip}"+":"+f"{x_pr}",
                                              "https":f"https://{x_ip}"+":"+f"{x_pr}"}
                            simple_request_prox(proxy_dict_new)
                            if Status_Response == 200:
                                curl_get_prox(tar_exp,str(proxy_dict_new['http']))
                                if len(status_reading) != 0 and status_reading != None and "301" not in status_reading:
                                    print("\n")
                                    print("\033[1;32m%s\x1b[0m" % ("FOUND"))
                                    print("\n")
                                    file_ext = open("target_site.html","w")
                                    file_ext.write(status_reading)
                                    file_ext.close()
                                    i_value_stop += 1
                                    break
                            else:
                                pass
                        except:
                            print("\033[1;33m%s\x1b[0m" % ("TRYING TO CONNECT, PLEASE WAIT"))
        else:
            print("\n")
            print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
            print("\n")
            time.sleep(0.8)
            pass
    except:
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
    

def search_val_dir(url_x=str): # USE FOR DIRECTORIES
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        print("\n")
        time.sleep(0.8)
        if "http://" in url_x or "https://" in url_x:
            if url_x.endswith("/") == True:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = url_x + str(x_dir_v)
                    check_status_code(new_t_s)
            elif url_x.endswith("/") == False:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = url_x + "/" +str(x_dir_v)
                    check_status_code(new_t_s)
            else:
                pass
        else:
            new_t_u = "http://"+url_x
            if new_t_u.endswith("/") == True:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = new_t_u + str(x_dir_v)
                    check_status_code(new_t_s)
            elif new_t_u.endswith("/") == False:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = new_t_u + "/" +str(x_dir_v)
                    check_status_code(new_t_s)
            else:
                pass
    except:
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)


def search_dork_dir(url_x=str): # USE FOR DIRECTORIES
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        print("\n")
        time.sleep(0.8)
        if "http://" in url_x or "https://" in url_x:
            if url_x.endswith("/") == True:
                read_file_xss("host_dork.txt")
                for x_dir_v in x_file:
                    try:
                        new_t_s = url_x + str(x_dir_v)
                        check_status_code(new_t_s)
                    except:
                        pass
            elif url_x.endswith("/") == False:
                read_file_xss("host_dork.txt")
                for x_dir_v in x_file:
                    try:
                        new_t_s = url_x + "/" +str(x_dir_v)
                        check_status_code(new_t_s)
                    except:
                        pass
            else:
                pass
        else:
            new_t_u = "http://"+url_x
            if new_t_u.endswith("/") == True:
                read_file_xss("host_dork.txt")
                for x_dir_v in x_file:
                    try:
                        new_t_s = new_t_u + str(x_dir_v)
                        check_status_code(new_t_s)
                    except:
                        pass
            elif new_t_u.endswith("/") == False:
                read_file_xss("host_dork.txt")
                for x_dir_v in x_file:
                    try:
                        new_t_s = new_t_u + "/" +str(x_dir_v)
                        check_status_code(new_t_s)
                    except:
                        pass
            else:
                pass
    except Exception as err:
        print(str(err))
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)


def requests_for_xss_get(xss_par,url_x=str):
    try:
        print("\n")
        print("------------------------")
        print("FOR [GET], PLEASE WAIT")
        print("""
-----------------
              -->
              """)
        time.sleep(1.5)
        user_agent_get()
        User_Header = {
                "User-Agent":f"{random.choice(all_list_agent)}"
                }
        Response_F_XSS = requests.get(url_x,headers=User_Header,timeout=22)
        if xss_par in Response_F_XSS.text:
            print("\n")
            print("[*] \033[1;32m%s\x1b[0m" % ("CODE IN HEADER - CHECK"))
            print("\n")
            print(url_x)
            time.sleep(1.8)
            print("\n")
        else:
            print("\n")
            print("%s \033[1;31m%s\x1b[0m" % ("NO RESPONSE FOR ",xss_par))
            print("SEARCH CONTINUES")
            pass
    except:
        pass
    
    
def requests_for_xss_post(xss_par,url_x=str):
    try:
        print("\n")
        print("------------------------")
        print("FOR [POST], PLEASE WAIT")
        print("""
-----------------
              -->
              """)
        time.sleep(1.5)
        user_agent_get()
        User_Header = {
                "User-Agent":f"{random.choice(all_list_agent)}"
                }
        Response_F_XSS = requests.post(url_x,headers=User_Header,timeout=22,data=xss_par)
        if xss_par in Response_F_XSS.text:
            print("\n")
            print("[*] \033[1;32m%s\x1b[0m" % ("CODE IN HEADER - CHECK"))
            print("\n")
            print("\033[1;32m%s\x1b[0m" % (url_x))
            time.sleep(1.8)
            print("\n")
        else:
            print("\n")
            print(url_x)
            print("%s \033[1;31m%s\x1b[0m" % ("NO RESPONSE FOR ",xss_par))
            print("SEARCH CONTINUES")
            pass
    except:
        pass


def xss_search(url_set=str): # ONLY SEARCH FOR XSS
    try:
        if "http://" in url_set or "https://" in url_set:
            print("\n")
            print("XSS HAS BEEN STARTED")
            print("THIS PROCESS CAN TAKE A LONG TIME")
            print("\n")
            if url_set.endswith("/") == True:
                read_file_xss("all_type_huge.txt")
                for xss_x in x_file:
                    new_xss_u = url_set + xss_x
                    requests_for_xss_get(xss_x,new_xss_u)
                    requests_for_xss_post(xss_x,url_set)
            elif url_set.endswith("/") == False:
                next_u = url_set + "/"
                read_file_xss("all_type_huge.txt")
                for xss_x in x_file:
                    new_xss_u = next_u + xss_x
                    requests_for_xss_get(xss_x,new_xss_u)
                    requests_for_xss_post(xss_x,url_set)
            else:
                pass
        else:
            new_t_u = "http://"+url_set
            print("\n")
            print("XSS HAS BEEN STARTED")
            print("THIS PROCESS CAN TAKE A LONG TIME")
            print("\n")
            if new_t_u.endswith("/") == True:
                read_file_xss("all_type_huge.txt")
                for xss_x in x_file:
                    new_xss_u = new_t_u + xss_x
                    requests_for_xss_get(xss_x,new_xss_u)
                    requests_for_xss_post(xss_x,new_t_u)
            elif new_t_u.endswith("/") == False:
                next_u = new_t_u + "/"
                read_file_xss("all_type_huge.txt")
                for xss_x in x_file:
                    new_xss_u = next_u + xss_x
                    requests_for_xss_get(xss_x,new_xss_u)
                    requests_for_xss_post(xss_x,new_t_u)
            else:
                pass
    except:
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)


def xss_define_search(url_set=str,status_set=int):
    try:
        if "http://" in url_set or "https://" in url_set:
            if status_set == 200:
                print("\n")
                print("XSS HAS BEEN STARTED")
                print("\n")
                if url_set.endswith("/") == True:
                    read_file_xss("all_type_huge.txt")
                    for xss_x in x_file:
                        new_xss_u = url_set + xss_x
                        requests_for_xss_get(xss_x,new_xss_u)
                        requests_for_xss_post(xss_x,url_set)
                elif url_set.endswith("/") == False:
                    next_u = url_set + "/"
                    read_file_xss("all_type_huge.txt")
                    for xss_x in x_file:
                        new_xss_u = next_u + xss_x
                        requests_for_xss_get(xss_x,new_xss_u)
                        requests_for_xss_post(xss_x,url_set)
                else:
                    pass
        else:
            new_t_u = "http://"+url_set
            if status_set == 200:
                print("\n")
                print("XSS HAS BEEN STARTED")
                print("\n")
                if new_t_u.endswith("/") == True:
                    read_file_xss("all_type_huge.txt")
                    for xss_x in x_file:
                        new_xss_u = new_t_u + xss_x
                        requests_for_xss_get(xss_x,new_xss_u)
                        requests_for_xss_post(xss_x,new_t_u)
                elif new_t_u.endswith("/") == False:
                    next_u = new_t_u + "/"
                    read_file_xss("all_type_huge.txt")
                    for xss_x in x_file:
                        new_xss_u = next_u + xss_x
                        requests_for_xss_get(xss_x,new_xss_u)
                        requests_for_xss_post(xss_x,new_t_u)
                else:
                    pass
    except:
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
    
    
def search_dir_xss(url_x=str):
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        print("\n")
        time.sleep(0.8)
        if "http://" in url_x or "https://" in url_x:
            if url_x.endswith("/") == True:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = url_x + str(x_dir_v)
                    check_status_code(new_t_s)
                    xss_define_search(new_t_s,Status_Response)
                        
            elif url_x.endswith("/") == False:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = url_x + "/" +str(x_dir_v)
                    check_status_code(new_t_s)
                    xss_define_search(new_t_s,Status_Response)
            else:
                pass
        else:
            new_t_u = "http://"+url_x
            if new_t_u.endswith("/") == True:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = new_t_u + str(x_dir_v)
                    check_status_code(new_t_s)
                    xss_define_search(new_t_s,Status_Response)
            elif new_t_u.endswith("/") == False:
                read_file_from("val_dir.txt")
                for x_dir_v in x_file:
                    new_t_s = new_t_u + "/" +str(x_dir_v)
                    check_status_code(new_t_s)
                    xss_define_search(new_t_s,Status_Response)
            else:
                pass
    except:
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)


def show_info():
    try:
        print("""
              
              
         IIIIIIIIIIIIIIIIIIII        PPPPPPPPPPPPPPPPP        VVVVVVVV           VVVVVVVV
         I::::::::II::::::::I        P::::::::::::::::P       V::::::V           V::::::V
         I::::::::II::::::::I        P::::::PPPPPP:::::P      V::::::V           V::::::V
         II::::::IIII::::::II        PP:::::P     P:::::P     V::::::V           V::::::V
           I::::I    I::::I            P::::P     P:::::P      V:::::V           V:::::V 
           I::::I    I::::I            P::::P     P:::::P       V:::::V         V:::::V  
           I::::I    I::::I            P::::PPPPPP:::::P         V:::::V       V:::::V   
           I::::I    I::::I            P:::::::::::::PP           V:::::V     V:::::V    
           I::::I    I::::I            P::::PPPPPPPPP              V:::::V   V:::::V     
           I::::I    I::::I            P::::P                       V:::::V V:::::V      
           I::::I    I::::I            P::::P                        V:::::V:::::V       
           I::::I    I::::I            P::::P                         V:::::::::V        
         II::::::IIII::::::II        PP::::::PP                        V:::::::V         
         I::::::::II::::::::I ...... P::::::::P                         V:::::V          
         I01000110II00110100I .::::. P01000110P                          V:::V     --> CREATED FOR FREE NET 
         IIIIIIIIIIIIIIIIIIII ...... PPPPPPPPPP                           VVV      --> open-source culture
              
             ############################################################################################################
             ############################################################################################################
             -------------------------------------------------------------------------------------
             
             py IIPV_CRACK_C.py -C https://example.com  [or] py IIPV_CRACK_C.py --cracker       https://example.com 
             py IIPV_CRACK_C.py -F https://example.com  [or] py IIPV_CRACK_C.py --fastscan      https://example.com 
             py IIPV_CRACK_C.py -D https://example.com  [or] py IIPV_CRACK_C.py --searchsub     https://example.com
             py IIPV_CRACK_C.py -T https://example.com  [or] py IIPV_CRACK_C.py --curlhunter    https://example.com
             py IIPV_CRACK_C.py -X https://example.com  [or] py IIPV_CRACK_C.py --searchdir     https://example.com
             py IIPV_CRACK_C.py -N https://example.com  [or] py IIPV_CRACK_C.py --searchxssdir  https://example.com
             py IIPV_CRACK_C.py -M https://example.com  [or] py IIPV_CRACK_C.py --searchxss     https://example.com
             py IIPV_CRACK_C.py -G https://example.com  [or] py IIPV_CRACK_C.py --searchdorkies     https://example.com
             py IIPV_CRACK_C.py -R                      [or] py IIPV_CRACK_C.py --p2prun                                           
             py IIPV_CRACK_C.py -P                      [or] py IIPV_CRACK_C.py --checkport
             py IIPV_CRACK_C.py -A                      [or] py IIPV_CRACK_C.py --scanipport
             py IIPV_CRACK_C.py -O                      [or] py IIPV_CRACK_C.py --pingto
             py IIPV_CRACK_C.py -S                      [or] py IIPV_CRACK_C.py --reverseto
    
             -------------------------------------------------------------------------------------
             ############################################################################################################
             ############################################################################################################
              
              -------------------------------------------------------------------------------------
              ####   -H    --help             how to use   ####
              
              [ -C ]  --cracker         -> check censored site and save html file
              [ -T ]  --curlhunter      -> check censored site with curl and save html file
              [ -R ]  --p2prun          -> connect p2p and send file
              [ -P ]  --checkport       -> check port to connect
              [ -A ]  --scanipport      -> check ip range with port
              [ -F ]  --fastscan        -> fast scan port range
              [ -D ]  --searchsub       -> check subdomains with ip information
              [ -X ]  --searchdir       -> search for directories
              [ -N ]  --searchxssdir    -> check cross site scripting with directories
              [ -M ]  --searchxss       -> check cross site scripting with single target
              [ -G ]  --searchdorkies   -> search dork directories
              [ -S ]  --reverseto       -> reverse shell for client connection
              [ -O ]  --pingto          -> send ping, check alive or not
              -------------------------------------------------------------------------------------
              
              
              <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
              -------------------------------------------------------------------------------------
              [NOTED - IMPORTANT]
              + If you get an unexpected error, please check your firewall and anti-virus settings.
              + You need the 'client' file for P2P connection.
              + Forward the 'client' file to the target machine and follow the instructions in order.
              -------------------------------------------------------------------------------------
              >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
              
              
              """)
    except:
        pass


def main_arq_process():
    try:
        Arq_Process = OPTp(add_help_option=False,epilog="P2P AND CENSORSHIP CRACKER")
        Arq_Process.add_option("-C",
                               "--cracker",
                               help="check censored site and save html file",
                               type="string",
                               dest="x_cracker")
        Arq_Process.add_option("-R",
                               "--p2prun",
                               help="connect p2p and send file",
                               action="store_true",
                               dest="x_p2prun")
        Arq_Process.add_option("-S",
                               "--reverseto",
                               help="reverse shell for client connection",
                               action="store_true",
                               dest="x_reverse")
        Arq_Process.add_option("-P",
                               "--checkport",
                               help="check port to connect",
                               action="store_true",
                               dest="x_port")
        Arq_Process.add_option("-A",
                               "--scanipport",
                               help="check ip range with port",
                               action="store_true",
                               dest="x_iport")
        Arq_Process.add_option("-F",
                               "--fastscan",
                               help="fast scan port range",
                               type="string",
                               dest="x_fsport")
        Arq_Process.add_option("-D",
                               "--searchsub",
                               help="check subdomains with ip",
                               type="string",
                               dest="x_subip")
        Arq_Process.add_option("-O",
                               "--pingto",
                               help="send ping, check alive or not",
                               action="store_true",
                               dest="x_ping")
        Arq_Process.add_option("-T",
                               "--curlhunter",
                               help="check censored site with curl and save html file",
                               type="string",
                               dest="x_curlh")
        Arq_Process.add_option("-X",
                               "--searchdir",
                               help="search for directories",
                               type="string",
                               dest="x_sdir")
        Arq_Process.add_option("-N",
                               "--searchxssdir",
                               help="check cross site scripting with directories",
                               type="string",
                               dest="x_xssd")
        Arq_Process.add_option("-M",
                               "--searchxss",
                               help="check cross site scripting with directories",
                               type="string",
                               dest="x_xss")
        Arq_Process.add_option("-G",
                               "--searchdorkies",
                               help="search dork directories",
                               type="string",
                               dest="x_sdork")
        Arq_Process.add_option("-H",
                               "--help",
                               help="how to use",
                               action="store_true",
                               dest="x_help")
        arq_run,arq_add = Arq_Process.parse_args()
        if arq_run.x_cracker:
            time.sleep(1.2)
            site_target = str(arq_run.x_cracker).replace(" ","")
            get_access_to_site(site_target)
        elif arq_run.x_fsport:
            time.sleep(1.2)
            site_target = str(arq_run.x_fsport).replace(" ","")
            run_port_sc(site_target)
        elif arq_run.x_subip:
            time.sleep(1.2)
            site_target = str(arq_run.x_subip).replace(" ","")
            dns_rec_search(site_target)
        elif arq_run.x_curlh:
            time.sleep(1.2)
            site_target = str(arq_run.x_curlh).replace(" ","")
            head_curl_hunter(site_target)
        elif arq_run.x_sdir:
            time.sleep(1.2)
            site_target = str(arq_run.x_sdir).replace(" ","")
            search_val_dir(site_target)
        elif arq_run.x_sdork:
            time.sleep(1.2)
            site_target = str(arq_run.x_sdork).replace(" ","")
            search_dork_dir(site_target)
        elif arq_run.x_xssd:
            time.sleep(1.2)
            site_target = str(arq_run.x_xssd).replace(" ","")
            search_dir_xss(site_target)
        elif arq_run.x_xss:
            time.sleep(1.2)
            site_target = str(arq_run.x_xss).replace(" ","")
            xss_define_search(site_target)
        elif arq_run.x_p2prun:
            time.sleep(1.2)
            get_info_mine()
            bind_process(Get_My_IP,1)
        elif arq_run.x_reverse:
            time.sleep(1.2)
            get_info_mine()
            bind_process(Get_My_IP,1,reverse_p=True)
        elif arq_run.x_ping:
            time.sleep(1.2)
            print("\n")
            try:
                ask_host_user = str(input("TYPE YOUR HOST TO PING: ")).replace(" ","")
                time.sleep(1.2)
                ping_start(ask_host_user)
            except:
                print("INVALID ENTRY, CANCELED")
                time.sleep(1.2)
                print("\n")
        elif arq_run.x_port:
            time.sleep(1.2)
            ask_user = str(input("DO YOU WANT TO CONTROL [G]ENERAL PORTS OR DO YOU WANT TO [S]PECIFY ('/' to exit): ")).upper().replace(" ","")
            time.sleep(0.8)
            try:
                if ask_user == "G":
                    check_common_port_status(set_port=False)
                elif ask_user == "S":
                    check_common_port_status(set_port=True)
                elif ask_user == "/":
                    print("CANCELED")
                    print("\n")
                    time.sleep(1.2)
                    pass
                else:
                    print("INVALID ENTRY, CANCELED")
                    print("\n")
                    time.sleep(1.2)
                    pass
            except:
                print("INVALID ENTRY, CANCELED")
                print("\n")
                time.sleep(1.2)
                print("\n")
        elif arq_run.x_iport:
            time.sleep(1.2)
            try:
                print("\n")
                ask_ip_user_first = str(input("TYPE YOUR FIRST SECTION OF IP RANGE: ")).replace(" ","")
                time.sleep(0.8)
                ask_ip_user_second = str(input("TYPE YOUR SECOND SECTION OF IP RANGE: ")).replace(" ","")
                time.sleep(0.8)
                ask_port_user_first = int(input("TYPE YOUR FIRST SECTION OF PORT RANGE: "))
                time.sleep(0.8)
                ask_port_user_second = int(input("TYPE YOUR SECOND SECTION OF PORT RANGE: "))
                time.sleep(1.2)
                print("\n")
                scan_ip_range(ask_ip_user_first,ask_ip_user_second,ask_port_user_first,ask_port_user_second)
            except:
                print("INVALID ENTRY, CANCELED")
                time.sleep(1.2)
                print("\n")
        elif arq_run.x_help:
            time.sleep(1.2)
            show_info()
            pass
        else:
            time.sleep(0.8)
            print("\n")
            print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
            print("\n")
            time.sleep(0.8)
            pass
    except:
        print("\n")
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
        


if __name__ == "__main__":
    try:
        main_arq_process()
    except:
        pass
