import cv2
import easyocr

cap = cv2.VideoCapture("text_detect.mp4")

#check if the video is opened correctly
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
    
if not cap.isOpened():
    raise IOError("Cannot open video")

while True:
    ret, frame = cap.read()
    
    reader = easyocr.Reader(['en'], gpu=False)
    
    result = reader.readtext(frame, detail=1, paragraph=False)
    # details are location of bounding boxes, string, probability
    
    for(bbox, text, prob) in result:
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]))
        tr = (int(tr[0]), int(tr[1]))
        br = (int(br[0]), int(br[1]))
        bl = (int(bl[0]), int(bl[1]))
        
        text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        
        cv2.rectangle(frame, tl, br, (0, 255, 0), 2) 
        
        cv2.putText(frame, text, (tl[0],tl[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

        
    cv2.imshow('Output-Image',frame)   
    
    for i in result:
        print(i[1])
        
    if cv2.waitKey(1)& 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()
