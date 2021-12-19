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
