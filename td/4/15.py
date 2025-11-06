import os
import datetime

# 1.

def lister_logfiles(path="system_logs"):
    if not (os.path.exists(path)):
        raise FileNotFoundError("folder system_logs existe pas")

    logfiles = os.listdir(path)
    for f in logfiles:
        if f.endswith(".log"):
            print(f)
            return f

lister_logfiles()

# 2. 

if not (os.path.exists("logs_clean")):
    os.makedirs("logs_clean")

# 3.

def read_line_by_line(path="system_logs"):
    if not (os.path.exists(path)):
        raise FileNotFoundError("folder system_logs existe pas")

    logfiles = os.listdir(path)
    for f in logfiles:
        if f.endswith(".log"):
            with open(path + "/" + f, "r") as file:
                for line in file:
                    if line.strip() != "":
                        print(line.strip())

read_line_by_line()

# 4. 

def count_total_lines(path="system_logs"):
    if not (os.path.exists(path)):
        raise FileNotFoundError("folder system_logs existe pas")

    logfiles = os.listdir(path)
    list_cleaned_lines = []
    for f in logfiles:
        if f.endswith(".log"):
            with open(path + "/" + f, "r") as file:
                for line in file:
                    if line.strip() != "":
                        list_cleaned_lines.append(line.strip())
    print(len(list_cleaned_lines))

count_total_lines()

# 5. 

def detect_errors(path="system_logs"):
    if not (os.path.exists(path)):
        raise FileNotFoundError("folder system_logs existe pas")

    logfiles = os.listdir(path)
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                i=0
                for line in file:
                    i+=1
                    if line.strip() != "":
                        splitted = line.strip().split('|')
                        if splitted[1].strip() == "ERROR":
                            with open('erreurs.txt', 'a') as errfile:
                                errfile.write(f"erreur ligne {i} dans {filepath}\n")

detect_errors()

# 6. 

def detect_date_errors(path="system_logs"):
    if not (os.path.exists(path)):
        raise FileNotFoundError("folder system_logs existe pas")

    logfiles = os.listdir(path)
    result = set()
    for f in logfiles:
        filepath = path + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                for line in file:
                    if line.strip() != "":
                        splitted = line.strip().split('|')
                        if splitted[1].strip() == "ERROR":
                            result.add(splitted[0])
    result_list = list(result)
    print(result_list)
    print(max(result_list, key=lambda x: result_list.count(x)))

detect_date_errors()

# 7.

def resume_logs(path="system_logs"):
    if not (os.path.exists(path)):
        raise FileNotFoundError("folder system_logs existe pas")

    logfiles = os.listdir(path)
    with open("resume_logs.txt", "w") as resumefile:
        for f in logfiles:
            if f.endswith(".log"):
                filepath = path + "/" + f
                total_lines=0
                error_count=0

                with open(filepath, "r") as file:
                    for line in file:
                        total_lines+=1
                        if line.strip() != "":
                            splitted = line.strip().split('|')
                            if splitted[1].strip() == "ERROR":
                                error_count+=1

                resumefile.write(f"{f}: lignes = {total_lines}, erreurs = {error_count}\n")

resume_logs()

# 8.

def move_to_archives(path="system_logs", path_arc="archives"):
    if not (os.path.exists(path)):
        raise FileNotFoundError("folder system_logs existe pas")
    
    if not os.path.exists(path_arc):
        os.makedirs(path_arc)

    logfiles = os.listdir(path)
    for f in logfiles:
        filepath = path + "/" + f
        filepath_arc = path_arc + "/" + f

        if f.endswith(".log"):
            with open(filepath, "r") as file:
                i=0
                for line in file:
                    i+=1
                    if line.strip() != "":
                        splitted = line.strip().split('|')
                        if splitted[1].strip() == "ERROR":
                            file_content = file.readlines()
                            with open(filepath_arc, "w") as arcfile:
                                arcfile.write(f"{str(file_content)}\n")
                                arcfile.write(str(datetime.datetime.now()))

move_to_archives()

# 9.

def rapport_global(path="logs_clean"):
    if not os.path.exists(path):
        raise FileNotFoundError("log_clean existe pas")
    
    logfiles = os.listdir(path)
    filepath = path + "/" + "rapport_global.log"
    with open(filepath, "a") as reportfile:
        for f in logfiles:
            if f.endswith(".log"):
                logfile_path = path + "/" + f
                with open(logfile_path, "r") as logfile:
                    for line in logfile:
                        if line.strip() != "":
                            reportfile.write(f"{str(datetime.datetime.now())}\n")
                            reportfile.write(line.strip() + "\n")

rapport_global()

# 10. 

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            with open("erreurs_execution.log", "a") as error_log:
                error_log.write(f"{datetime.datetime.now()} - FileNotFoundError: {str(e)}\n")
        except PermissionError as e:
            with open("erreurs_execution.log", "a") as error_log:
                error_log.write(f"{datetime.datetime.now()} - PermissionError: {str(e)}\n")
        except Exception as e:
            with open("erreurs_execution.log", "a") as error_log:
                error_log.write(f"{datetime.datetime.now()} - Exception: {str(e)}\n")
    return wrapper