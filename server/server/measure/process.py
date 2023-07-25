from scipy.spatial.distance import euclidean
from imutils import perspective, contours, grab_contours
import numpy as np
import cv2


def detect_edge(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)

    # Performing edge detection
    edged = cv2.Canny(blur, 100, 200)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    return edged

def find_contours(edged, area_threshold=1000):
    # Find contours
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = grab_contours(cnts)

    # Sort contours from left to right as leftmost contour is reference object
    (cnts, _) = contours.sort_contours(cnts)

    # Remove contours which are not large enough
    cnts = [x for x in cnts if cv2.contourArea(x) > area_threshold]

    return cnts

def get_pixel_per_mm(cnts, dist_in_mm):
    # Reference object dimensions
    ref_object = cnts[0]
    box = cv2.minAreaRect(ref_object)
    box = cv2.boxPoints(box)
    box = np.array(box, dtype="float32")
    box = perspective.order_points(box)
    (tl, tr, br, bl) = box
    dist_in_pixel = euclidean(tl, bl)
    pixel_per_mm = dist_in_pixel/dist_in_mm

    return pixel_per_mm

def draw_remaining_contours(cnts, image, pixel_per_mm):
    # Draw remaining contours
    for cnt in cnts:
        box = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(box)
        box = np.array(box, dtype="float32")
        box = perspective.order_points(box)
        (tl, tr, br, bl) = box
        cv2.drawContours(image, [box.astype("int")], -1, (0, 0, 255), 2)
        mid_pt_horizontal = (tl[0] + int(abs(tr[0] - tl[0])/2), 
                             tl[1] + int(abs(tr[1] - tl[1])/2))
        mid_pt_verticle = (tr[0] + int(abs(tr[0] - br[0])/2),
                           tr[1] + int(abs(tr[1] - br[1])/2))
        wid = euclidean(tl, tr)/pixel_per_mm
        ht = euclidean(tr, br)/pixel_per_mm
        cv2.putText(
            image, 
            "{:.3f}mm".format(wid), (int(mid_pt_horizontal[0] - 15), 
            int(mid_pt_horizontal[1] - 10)), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        cv2.putText(
            image, 
            "{:.3f}mm".format(ht), 
            (int(mid_pt_verticle[0] + 10), int(mid_pt_verticle[1])), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    
    return image

def process_image(img_path: str, vertical: int, area_threshold):
    image = cv2.imread(img_path)
    edged = detect_edge(image)

    # Find contours
    cnts = find_contours(edged, area_threshold)

    # Get pixel per mm
    pixel_per_mm = get_pixel_per_mm(cnts, vertical)
    print(pixel_per_mm)

    # Draw remaining contours
    image = draw_remaining_contours(cnts, image, pixel_per_mm)

    # save image
    cv2.imwrite("images/result.jpg", image)

def process_image_with_pixel_per_mm(img_path: str, pixel_per_mm: float, area_threshold):
    image = cv2.imread(img_path)
    edged = detect_edge(image)

    # Find contours
    cnts = find_contours(edged, area_threshold)

    # Draw remaining contours
    image = draw_remaining_contours(cnts, image, pixel_per_mm)

    # save image
    cv2.imwrite("images/result_with_pixel.jpg", image)