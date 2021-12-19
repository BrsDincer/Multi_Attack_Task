def run_port_sc(tar_in_user):
    try:
        print("\n")
        print("THE PROCESS HAS BEEN STARTED, PLEASE WAIT")
        time.sleep(1.2)
        print("THIS SECTION IS FOR FAST SCANNING. PLEASE MAKE SURE ABOUT PROCESSES.")
        time.sleep(1.2)
        print("\n")
        th_l = threading.Lock()
        if "http://" in tar_in_user or "https://" in tar_in_user:
            new_h = tar_in_user.replace("http://","").replace("https://","")
            first_range_pt = int(input("FIRST PORT OF RANGE YOU DESIRE: "))
            second_range_pt = int(input("SECOND PORT OF RANGE YOU DESIRE: "))
            tar_IP = socket.gethostbyname(new_h)
            print("\n")
            print('SITE ON: ', new_h)
            print('IP ON: ', tar_IP)
        else:
            first_range_pt = int(input("FIRST PORT OF RANGE YOU DESIRE: "))
            second_range_pt = int(input("SECOND PORT OF RANGE YOU DESIRE: "))
            tar_IP = socket.gethostbyname(tar_in_user)
            print("\n")
            print('SITE ON: ', tar_in_user)
            print('IP ON: ', tar_IP)
        time.sleep(1.2)
        print("\n")
        time.sleep(1.2)
        def port_scan_main(port_tar=int):
            socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket_main.settimeout(5)
            try:
              conn_main = socket_main.connect((tar_IP, port_tar))
              with th_l:
                  print(port_tar, 'OPEN')
              conn_main.close()
            except:
                pass
        def threader_running():
            while True:
              w_paid = q.get()
              port_scan_main(w_paid)
              q.task_done()
        q = Queue()
        time_s = time.time()
        for x in range(100):
            t_main = threading.Thread(target = threader_running)
            t_main.daemon = True
            t_main.start()
        for x_l in range(first_range_pt, second_range_pt+1):
            q.put(x_l)
        q.join()
        print("\n")
        print('PROCESS IS DONE ', "%.2f" % (time.time() - time_s), " TIME")
        print("\n")
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION OR PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
