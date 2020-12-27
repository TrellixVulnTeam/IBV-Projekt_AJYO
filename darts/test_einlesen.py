import cv2 as cv

def get_IMAGE(name, param):

    img = cv.imread(name, param)

    # img = img[33:412, 93:599]

    # ret0, thresh0 = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
    #
    # kernel = np.ones((2, 2), np.uint8)
    # erosion = cv.erode(thresh0, kernel, iterations=1)
    # dilation = cv.dilate(thresh0, kernel, iterations=1)
    #
    # erg = cv.dilate(erosion, kernel, iterations=1)

    # print(kernel)

    # cv2.line(img, (0, 0), (150, 150), (0, 255, 0), 10) #Linie
    # cv2.rectangle(img, (15, 25), (200, 150), (0, 250, 0), 5)   #Rechteck
    # cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)    #Kreis
    # pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)  #P_gon
    # cv2.polylines(img, [pts], True, (0, 255, 0), 1)    # True Parameter (start-stop) verbinden
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(img, 'TEST!', (0, 130), font, 1, (0, 255, 0))

    # titel = ['Original', 'Gray', 'Binary', 'Erosion', 'Dilation', 'ERG']
    # bilder = [img, gray, thresh0, erosion, dilation, erg]
    #
    # for k, i in enumerate(bilder):
    #    plt.subplot(2, 3, k+1)
    #    plt.imshow(i, 'gray')
    #    plt.xticks([])
    #    plt.yticks([])
    #    plt.title(titel[k])

    #cv.imshow('Bild', img)
    #cv.imwrite('neu.png', img)
    return img

def get_VIDEO(pfad):

    cap = cv.VideoCapture(pfad)

    while (cap.isOpened()):

        ret, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        #flipped = cv.flip(gray, flipCode=3)
        flipped = cv.rotate(gray, cv.ROTATE_90_CLOCKWISE)

        name = 'frame'
        cv.namedWindow(name, cv.WINDOW_NORMAL)
        cv.moveWindow(name, 20, 20)
        cv.resizeWindow(name, 600, 600)
        cv.imshow('frame', flipped)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':

    get_VIDEO('/Users/alex/Workspace/git_repos/IBV-Projekt/Testvideos/271220/20201227_160730.mp4')