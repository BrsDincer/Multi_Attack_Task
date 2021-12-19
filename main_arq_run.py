def main_arq_process():
    try:
        Arq_Process = OPTp(add_help_option=False,epilog="P2P AND CENSORSHIP CRACKER")
        Arq_Process.add_option("-C",
                               "--cracker",
                               help="check censored site and save html file",
                               type="string",
                               dest="x_cracker")
        Arq_Process.add_option("-R",
                               "--p2prun",
                               help="connect p2p and send file",
                               action="store_true",
                               dest="x_p2prun")
        Arq_Process.add_option("-S",
                               "--reverseto",
                               help="reverse shell for client connection",
                               action="store_true",
                               dest="x_reverse")
        Arq_Process.add_option("-P",
                               "--checkport",
                               help="check port to connect",
                               action="store_true",
                               dest="x_port")
        Arq_Process.add_option("-A",
                               "--scanipport",
                               help="check ip range with port",
                               action="store_true",
                               dest="x_iport")
        Arq_Process.add_option("-F",
                               "--fastscan",
                               help="fast scan port range",
                               type="string",
                               dest="x_fsport")
        Arq_Process.add_option("-D",
                               "--searchsub",
                               help="check subdomains with ip",
                               type="string",
                               dest="x_subip")
        Arq_Process.add_option("-O",
                               "--pingto",
                               help="send ping, check alive or not",
                               action="store_true",
                               dest="x_ping")
        Arq_Process.add_option("-T",
                               "--curlhunter",
                               help="check censored site with curl and save html file",
                               type="string",
                               dest="x_curlh")
        Arq_Process.add_option("-X",
                               "--searchdir",
                               help="search for directories",
                               type="string",
                               dest="x_sdir")
        Arq_Process.add_option("-N",
                               "--searchxssdir",
                               help="check cross site scripting with directories",
                               type="string",
                               dest="x_xssd")
        Arq_Process.add_option("-M",
                               "--searchxss",
                               help="check cross site scripting with directories",
                               type="string",
                               dest="x_xss")
        Arq_Process.add_option("-G",
                               "--searchdorkies",
                               help="search dork directories",
                               type="string",
                               dest="x_sdork")
        Arq_Process.add_option("-H",
                               "--help",
                               help="how to use",
                               action="store_true",
                               dest="x_help")
        arq_run,arq_add = Arq_Process.parse_args()
        if arq_run.x_cracker:
            time.sleep(1.2)
            site_target = str(arq_run.x_cracker).replace(" ","")
            get_access_to_site(site_target)
        elif arq_run.x_fsport:
            time.sleep(1.2)
            site_target = str(arq_run.x_fsport).replace(" ","")
            run_port_sc(site_target)
        elif arq_run.x_subip:
            time.sleep(1.2)
            site_target = str(arq_run.x_subip).replace(" ","")
            dns_rec_search(site_target)
        elif arq_run.x_curlh:
            time.sleep(1.2)
            site_target = str(arq_run.x_curlh).replace(" ","")
            head_curl_hunter(site_target)
        elif arq_run.x_sdir:
            time.sleep(1.2)
            site_target = str(arq_run.x_sdir).replace(" ","")
            search_val_dir(site_target)
        elif arq_run.x_sdork:
            time.sleep(1.2)
            site_target = str(arq_run.x_sdork).replace(" ","")
            search_dork_dir(site_target)
        elif arq_run.x_xssd:
            time.sleep(1.2)
            site_target = str(arq_run.x_xssd).replace(" ","")
            search_dir_xss(site_target)
        elif arq_run.x_xss:
            time.sleep(1.2)
            site_target = str(arq_run.x_xss).replace(" ","")
            xss_define_search(site_target)
        elif arq_run.x_p2prun:
            time.sleep(1.2)
            get_info_mine()
            bind_process(Get_My_IP,1)
        elif arq_run.x_reverse:
            time.sleep(1.2)
            get_info_mine()
            bind_process(Get_My_IP,1,reverse_p=True)
        elif arq_run.x_ping:
            time.sleep(1.2)
            print("\n")
            try:
                ask_host_user = str(input("TYPE YOUR HOST TO PING: ")).replace(" ","")
                time.sleep(1.2)
                ping_start(ask_host_user)
            except:
                print("INVALID ENTRY, CANCELED")
                time.sleep(1.2)
                print("\n")
        elif arq_run.x_port:
            time.sleep(1.2)
            ask_user = str(input("DO YOU WANT TO CONTROL [G]ENERAL PORTS OR DO YOU WANT TO [S]PECIFY ('/' to exit): ")).upper().replace(" ","")
            time.sleep(0.8)
            try:
                if ask_user == "G":
                    check_common_port_status(set_port=False)
                elif ask_user == "S":
                    check_common_port_status(set_port=True)
                elif ask_user == "/":
                    print("CANCELED")
                    print("\n")
                    time.sleep(1.2)
                    pass
                else:
                    print("INVALID ENTRY, CANCELED")
                    print("\n")
                    time.sleep(1.2)
                    pass
            except:
                print("INVALID ENTRY, CANCELED")
                print("\n")
                time.sleep(1.2)
                print("\n")
        elif arq_run.x_iport:
            time.sleep(1.2)
            try:
                print("\n")
                ask_ip_user_first = str(input("TYPE YOUR FIRST SECTION OF IP RANGE: ")).replace(" ","")
                time.sleep(0.8)
                ask_ip_user_second = str(input("TYPE YOUR SECOND SECTION OF IP RANGE: ")).replace(" ","")
                time.sleep(0.8)
                ask_port_user_first = int(input("TYPE YOUR FIRST SECTION OF PORT RANGE: "))
                time.sleep(0.8)
                ask_port_user_second = int(input("TYPE YOUR SECOND SECTION OF PORT RANGE: "))
                time.sleep(1.2)
                print("\n")
                scan_ip_range(ask_ip_user_first,ask_ip_user_second,ask_port_user_first,ask_port_user_second)
            except:
                print("INVALID ENTRY, CANCELED")
                time.sleep(1.2)
                print("\n")
        elif arq_run.x_help:
            time.sleep(1.2)
            show_info()
            pass
        else:
            time.sleep(0.8)
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
        


if __name__ == "__main__":
    try:
        main_arq_process()
    except:
        pass
