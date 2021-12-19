def read_file_from(file_name=str):
    try:
        global x_file
        with open(file_name,"r") as file_tar:
            x_file = []
            for line_x in file_tar:
                try:
                    ext_tar = line_x.strip()
                    x_file.append(ext_tar)
                except:
                    pass
    except:
        print("SOMETHING IS WRONG, PLEASE CHECK YOUR INTERNET CONNECTION OR DIRECTORIES")
        print("\n")
        time.sleep(0.8)
        pass
