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
