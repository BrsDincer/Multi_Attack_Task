def reading_url_pdf(url_name=str,saving_file_name=str):
    try:
        if ".pdf" in url_name and ".pdf" in saving_file_name:
            req_url = requests.get(url_name,stream=True)
            save_file = open(saving_file_name,"wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        elif ".pdf" not in url_name and ".pdf" not in saving_file_name:
            req_url = requests.get(url_name+".pdf",stream=True)
            save_file = open(saving_file_name+".pdf","wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        elif ".pdf" in url_name and ".pdf" not in saving_file_name:
            req_url = requests.get(url_name,stream=True)
            save_file = open(saving_file_name+".pdf","wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        elif ".pdf" not in url_name and ".pdf" in saving_file_name:
            req_url = requests.get(url_name+".pdf",stream=True)
            save_file = open(saving_file_name,"wb")
            for ch_file in req_url.iter_content(2000):
                save_file.write(ch_file)
            save_file.close()
        else:
            print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
            print("\n")
            time.sleep(0.8)
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION AND PARAMETERS")
        print("\n")
        time.sleep(0.8)
        pass
