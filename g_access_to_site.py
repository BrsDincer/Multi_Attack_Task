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
