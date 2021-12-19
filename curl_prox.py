def curl_get_prox(tar_url=str,prox_dom=str):
    try:
        global status_reading
        command_prob = os.popen("curl -k -s --proxy %s %s -m %s" % (prox_dom, tar_url, 30))
        status_reading = command_prob.read()
        print(status_reading)
    except:
        pass

    
def curl_get_norm(tar_url=str):
    try:
        global status_reading
        command_prob = os.popen("curl -k -s %s -m %s" % (tar_url,30))
        status_reading = command_prob.read()
        print(status_reading)
    except:
        pass
