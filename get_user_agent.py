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
