import os

# 1.

def merge_logs(path="log"):
    if not (os.path.exists(path)):
        os.makedirs(path)

    logfiles = os.listdir(path)
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip() != "":
                        print(line.strip())

#merge_logs()

# 2. 

def merge_logs_horodatage(path="log"):
    if not (os.path.exists(path)):
        os.makedirs(path)

    logfiles = os.listdir(path)
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip() != "":
                        print(line.strip().split('|')[0])

#merge_logs_horodatage()

# 3.

def merge_logs_into_master(path="log"):
    if not (os.path.exists(path)):
        os.makedirs(path)

    logfiles = os.listdir(path)
    result = []
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip() != "":
                        with open("master.log", "w") as master:
                            result.append(line.strip())
                            result_propre = ' '.join(result)
                            master.write(result_propre)                  

#merge_logs_into_master()

# 4.

def merge_logs_horodatage_trier(path="log"):
    if not (os.path.exists(path)):
        os.makedirs(path)

    logfiles = os.listdir(path)
    result = set([])
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip() != "":
                        result.add(line.strip().split('|')[0])
    result = sorted(result)
    print(result)
                        
#merge_logs_horodatage_trier()

# 5.

def merge_logs_horodatage_trier(path="log"):
    if not (os.path.exists(path)):
        os.makedirs(path)

    logfiles = os.listdir(path)
    result = set([])
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip() != "":
                        result.add(line.strip().split('|')[0])
    result = sorted(result)
    print(result)

# 6. 

def merge_logs_horodatage_trier(path="log"):
    if not (os.path.exists(path)):
        os.makedirs(path)

    logfiles = os.listdir(path)
    result = set([])
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip() != "":
                        result.add(line.strip().split('|')[0])
    result = sorted(result)
    print(result)