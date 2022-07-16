import os
import cv2


path_dataset=""

def find_min_size(path):
    min_dimension=16384
    min_couple=(128,128)
    for folder in os.listdir(path):
        for item in os.listdir(path+"/"+folder):
            image = cv2.imread(os.path.join(path+"/"+folder,item))

            annotated_image=image.copy()
            h,w,c=annotated_image.shape

            current_dimension=h*w
            current_couple=(h,w)

            if(current_dimension<min_dimension):
                min_dimension=current_dimension
                min_couple=current_couple

    return min_dimension,min_couple[0],min_couple[1]

def find_max_size(path):
    max_dimension=0
    max_couple=(0,0)
    for folder in os.listdir(path):
        for item in os.listdir(path+"/"+folder):
            image = cv2.imread(os.path.join(path+"/"+folder,item))

            annotated_image=image.copy()
            h,w,c=annotated_image.shape

            current_dimension=h*w
            current_couple=(h,w)

            if(current_dimension>max_dimension):
                max_dimension=current_dimension
                max_couple=current_couple

    return max_dimension,max_couple[0],max_couple[1]


if __name__ == '__main__':

    #cerco in tutto il dataset la più piccola dimensione l'altezza e la larghezza ad essa associata
    smallest_dimension, smallest_h, smallest_w=find_min_size(path_dataset)
    print("dimensione minore:",smallest_dimension,"smallest h:", smallest_h, "smallest w:", smallest_w)


    #cerco in tutto il dataset la più grande dimensione l'altezza e la larghezza ad essa associata
    biggest_dimension, biggest_h, biggest_w=find_max_size(path_dataset)
    print("dimensione maggiore:",biggest_dimension,"biggest h:", biggest_h, "biggest w:", biggest_w)