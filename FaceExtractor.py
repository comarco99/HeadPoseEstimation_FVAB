import os
import cv2
import mediapipe as mp
import numpy

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

#path immagini da caricare
path_images = ""

#path immagini scartate da mediapipe
path_rejected_image=""

#path cartella con rilevazioni
path_detectd_face=""

#path cartella con estrazioni
path_extracted_face=""

#counter per numero di file
count = 0
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

#inizializzo il modello a 1 e il livello di confidence a 0.5
with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.50) as face_detection:

    for file in os.listdir(path_images):
        image = cv2.imread(os.path.join(path_images,file))

        #converti BGR in RGB prima di processare.
        results2 = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # controllo se trovo un volto nell'immagine
        if( not results2.detections):
            #salva questa immagine non rilevata in una cartella specifica
            cv2.imwrite(path_rejected_image+str(file),image)
            continue

        annotated_image = image.copy()

        #contatore per numero di volti rilevati
        faces=0
        #seleziono l'area del volto
        for detection in results2.detections:
            faces+=1

            #salvo in una lista le coordinate in alto a sx e in basso a dx di ogni volto identificato
            h, w, c = annotated_image.shape

            #estraggo le coordinate della box contenente il volto
            bbox = detection.location_data.relative_bounding_box
            bbox_points = {
                "xmin": int(bbox.xmin * w),
                "ymin": int(bbox.ymin * h),
                "xmax": int(bbox.width * w + bbox.xmin * w),
                "ymax": int(bbox.height * h + bbox.ymin * h)
            }

            #quantifico i padding per altezza e larghezza affinchè raggiungano 128
            padding_min = 128 - (bbox_points['xmax'] - bbox_points['xmin'])#larghezza
            padding_max = 128 - (bbox_points['ymax'] - bbox_points['ymin'])#altezza

            #adatto la bounding box alla dimensione di 128x128
            scarto=int(padding_min/2)
            xmin = bbox_points['xmin']-scarto
            ymin = bbox_points['ymin']-scarto
            scarto2=int(padding_max/2)
            ymax = bbox_points['ymax']+scarto2
            xmax = bbox_points['xmax']+scarto2

            larghezza_nuova=xmax-xmin
            altezza_nuova=ymax-ymin

            #controllo se l'altezza o la larghezza sforano o sono al di sotto di 128 per adattare il quadrato
            diff=0
            if(larghezza_nuova>128):
                diff=larghezza_nuova-128
                xmax=xmax-diff
            if(altezza_nuova>128):
                diff=altezza_nuova-128
                ymax=ymax-diff
            if(larghezza_nuova<128):
                diff=128-larghezza_nuova
                xmax=xmax+diff
            if(altezza_nuova<128):
                diff=128-altezza_nuova
                ymax=ymax+diff

            #ritaglio l'area del viso
            cropped_image=annotated_image[ymin:ymax,xmin:xmax]

            #salvo l'area dell'immagine interessata
            try:
                cv2.imwrite(path_extracted_face+str(file), cropped_image)
            except:
                cv2.imwrite(path_rejected_image+str(file), annotated_image)

            #se rileva più di un volto in background, prendi solo quello in primo piano
            if(faces>=1):
                break

        #delinea l'area del volto attraverso una box 128x128
        cv2.rectangle(annotated_image,(xmin,ymin),(xmax,ymax),(255,255,0),2)

        #salvo la foto con l'area del volto identificata
        cv2.imwrite(path_detectd_face+str(file), annotated_image)
        count = count+1
