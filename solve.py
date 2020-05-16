import numpy as np
import cv2
#
 #x = np.arange(108)
#  x
# x = x.reshape(9,12)
# print(x)
# print(x[0])
# print(np.size(x,0))
# for i in range(0,np.size(x,0)):
#     x[i]=0
# print(x)


#x = np.roll(x, -1, axis=0) # up
#print(x)

def show_webcam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            blurred = cv2.GaussianBlur(gray, (3, 3), 0)
            canny = cv2.Canny(blurred, 20, 60)
            kernel = np.ones((3,3), np.uint8)
            dilated = cv2.dilate(canny, kernel, iterations=2)
            #(contours, hierarchy) = cv2.findContours(dilated.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('my webcam',dilated )
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()