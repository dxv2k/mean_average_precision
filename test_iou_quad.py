from posixpath import ismount
import numpy as np
import shapely
from shapely.geometry import Polygon, MultiPoint  # Polygon


def calculate_iou(pred, gt):
    _pred = np.array(pred).reshape(4, 2)
    pred_poly = Polygon(_pred).convex_hull
    # print(Polygon(_pred).convex_hull)  # you can print to see if this is the case

    _gt = np.array(gt).reshape(4, 2)
    gt_poly = Polygon(_gt).convex_hull
    # print(Polygon(_gt).convex_hull)

    # Merge two box coordinates to become 8*2
    union_poly = np.concatenate((_pred, _gt))
    # print(MultiPoint(union_poly).convex_hull)
    # If the two quadrilaterals do not intersect
    if not pred_poly.intersects(gt_poly):
        iou = 0
    else:
        try:
            inter_area = pred_poly.intersection(
                gt_poly).area  # intersection area
        #     print(inter_area)
            union_area = MultiPoint(union_poly).convex_hull.area
        #     print(union_area)
            if union_area == 0:
                iou = 0
            iou = float(inter_area)/union_area
        except shapely.geos.TopologicalError:
            print('shapely.geos.TopologicalError occured, iou set to 0')
            iou = 0
    return iou


# line1 = [196, 194, 287, 201, 289, 267, 196, 263]
# line2 = [199, 194, 287, 201, 289, 267, 196, 263]
# line1=[2,0,2,2,0,0,0,0] #One-dimensional array representation of the coordinates of the four points of the quadrilateral, [x,y,x,y....]
# line2=[1,1,4,1,4,4,1,4]

# print(calculate_iou(line1, line2))


gt = np.array([
    [196, 194, 287, 201, 289, 267, 196, 263],
    [291, 207, 419, 211, 420, 271, 294, 266],
    [425, 220, 471, 220, 472, 273, 425, 271],
    [475, 219, 561, 219, 562, 275, 477, 274],
    [567, 224, 642, 228, 644, 279, 567, 277],
])
# print(gt.shape[0])

# QUAD format [x1,y1,x2,y2,x3,y3,x4,y4]
pred = np.array([
    [199, 194, 287, 201, 289, 267, 196, 263],
    [200, 194, 287, 201, 289, 267, 199, 263],
    [291, 207, 419, 211, 420, 271, 294, 266],
    [425, 220, 471, 220, 472, 273, 425, 271],
    [475, 219, 561, 219, 562, 275, 477, 274],
    [567, 224, 642, 228, 644, 279, 567, 277],
    [765, 305, 785, 305, 788, 336, 764, 337],
    [786, 307, 800, 309, 799, 332, 789, 331],
    [763, 376, 799, 375, 799, 408, 766, 407],
    [779, 414, 799, 413, 799, 438, 783, 43],
])

print(pred.shape[0])

def compute_iou(preds,gt): 
	# iou = np.array([]) 
	iou = []
	for idx_gt in range(gt.shape[0]): 
		for idx_pred in range(preds.shape[0]): 
			temp_iou = np.array([calculate_iou(gt[idx_gt],preds[idx_pred])]) 
			iou.append(temp_iou)
			# print(temp_iou)
			# np.concatenate(iou,temp_iou)
	iou = np.array(iou).reshape(preds.shape[0],gt.shape[0])
	return iou 
# gt = np.array([199, 194, 287, 201, 289, 267, 196, 263]) 

print(compute_iou(pred,gt))

# print(np.arange(pred.shape[0]*gt.shape[0]).reshape(pred.shape[0],gt.shape[0]) )