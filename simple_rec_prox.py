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
