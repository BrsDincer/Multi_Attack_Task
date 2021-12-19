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
