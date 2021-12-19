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
