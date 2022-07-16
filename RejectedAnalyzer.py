import os

def rejected_counter(path_folder):
    tot=0
    for folder in os.listdir(path_folder):
        c=0
        for item in os.listdir(os.path.join(path_folder,folder)):
            c+=1
        tot+=c
        print("Rejected in folder "+path_folder+folder+": ", c)
    print("Rejected tot: ",tot)


if __name__ == '__main__':
    path_rejected_folder=""
    rejected_counter(path_rejected_folder)