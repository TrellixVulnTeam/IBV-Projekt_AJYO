from game import Game
from game import Board
import cv2 as cv
import time
import test

if __name__ == '__main__':

    print('Program started')

    board = Board()

    board.ref_img = test.get_IMAGE('/Users/alex/Workspace/git_repos/IBV-Projekt/darts/bilder/arrow_21.png', 0)
    # board.set_ref_img()

    board.get_ref_img()
    cv.waitKey(1)
    cv.destroyAllWindows()

    board.img = test.get_IMAGE('/Users/alex/Workspace/git_repos/IBV-Projekt/darts/bilder/arrow_22.png', 0)
    # board.get_img()

    board.get_img()
    cv.waitKey(1)
    cv.destroyAllWindows()

    diff, img_contour, img_detected = board.detect_arrow()

    board.view_image(diff, 'Differenz')
    cv.waitKey(1)
    cv.destroyAllWindows()

    board.view_image(img_contour, 'Kontur')
    cv.waitKey(1)
    cv.destroyAllWindows()

    board.view_image(img_detected, 'Pfeil')
    cv.waitKey(1)
    cv.destroyAllWindows()

    # hier Auftreffpunkt setzen (später wird vom arrow_detect()-Funktion gesetzt)
    # board.point = (1150, 1160)

    db = board.draw_board()
    board.view_image(db, 'Digital Board')
    cv.waitKey(1)
    cv.destroyAllWindows()

    board.scorer_ellipse()
