import cv2
import numpy as np
import argparse
global lines
lines = []

drawing = False
x2,y2 = -1,-1

def draw_shape(event,x,y,flag,parm):
    global x2,y2,drawing, img, img2
    
    if len(lines) < 2:
        if event == cv2.EVENT_LBUTTONDOWN:
            # print('Clicked: ', (x,y))
            lines.append((x, y))
            drawing = True
            img2 = img.copy()
            x2,y2 = x,y
            cv2.line(img,(x2,y2),(x,y),(0,0,255),1, cv2.LINE_AA)

        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing == True:
                # print('Moving: ',(x,y))
                a, b = x, y
                if a != x & b != y:
                    img = img2.copy()
                    cv2.line(img,(x2,y2),(x,y),(0,255,0),1, cv2.LINE_AA)

        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
            # print('Released: ',(x,y))
            lines.append((x, y))
            img = img2.copy()
            cv2.line(img,(x2,y2),(x,y),(0,0,255),1, cv2.LINE_AA)
    else:
        return

def draw_lines(image_path):
    global img, img2
    img = cv2.imread(image_path)
    img2 = img.copy()
    cv2.namedWindow("Draw")
    cv2.setMouseCallback("Draw",draw_shape)
    
    # press the escape button to exit
    while True:
        cv2.imshow("Draw",img)
        k = cv2.waitKey(10) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    return lines

def define_ROI(image_path):
    """
    Define Region of Interest based on user input.
   """
    
    lines = draw_lines(image_path)
    # print(lines)
    # print([lines[0], lines[1]])
    return [lines[0], lines[1]]
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Draw')
    parser.add_argument('--input_image', type=str, help='Input videos file path name')
    args = parser.parse_args()
    img_ms_path = args.input_image
    line = define_ROI(img_ms_path)
    dist = ((line[0][0]-line[1][0])**2 + (line[0][1]-line[1][1])**2)**0.5
    print(dist)