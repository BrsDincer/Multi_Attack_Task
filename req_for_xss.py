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
