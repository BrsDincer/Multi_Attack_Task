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
