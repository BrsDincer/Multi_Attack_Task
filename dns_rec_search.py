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
