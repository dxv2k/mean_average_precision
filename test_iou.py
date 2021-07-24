import numpy as np 
import shapely
from shapely.geometry import Polygon,MultiPoint  #Polygon

def compute_iou(pred, gt):
    _gt = np.array(gt).reshape(4,2)
    _pred = np.array(pred).reshape(4,2)

    _poly_gt = Polygon(_gt).convex_hull
    _poly_pred = Polygon(_pred).convex_hull

    # Calc IOU   
    union_poly = np.concatenate((_poly_gt,_poly_pred))
    if not _poly_pred.intersects(_poly_gt): 
        iou = 0 
    else: 
        try: 
            inter_area = _poly_pred.intersection(_poly_gt)
            print("Inter area",inter_area)
            union_area = MultiPoint(union_poly).convex_hull.area
            print("Union area",union_area)
            if union_area == 0: 
                iou = 0 
            iou = float(inter_area)/union_area

        except shapely.geos.TopologicalError:
            print('shapely.geos.TopologicalError occured, iou set to 0')
            iou = 0
    print(iou)
    return iou

if __name__ == "__main__":
	gt = np.array([
		[196, 194, 287, 201, 289, 267, 196, 263],
		[291, 207, 419, 211, 420, 271, 294, 266],
		[425, 220, 471, 220, 472, 273, 425, 271],
		[475, 219, 561, 219, 562, 275, 477, 274],
		[567, 224, 642, 228, 644, 279, 567, 277],
	])
	pred = np.array([
		[196, 194, 287, 201, 289, 267, 196, 263],
		[291, 207, 419, 211, 420, 271, 294, 266],
		[425, 220, 471, 220, 472, 273, 425, 271],
		[475, 219, 561, 219, 562, 275, 477, 274],
		[567, 224, 642, 228, 644, 279, 567, 277],
	])
	_gt = np.tile(gt, (pred.shape[0], 1))
	_pred = np.repeat(pred, gt.shape[0], axis=0)

	print(_gt)
	print('######################')
	print(_pred)
	# print(type(gt)) 
	# # QUAD format [x1,y1,x2,y2,x3,y3,x4,y4]
	# pred = np.array([
	# [196, 194, 287, 201, 289, 267, 196, 263],
	# [291, 207, 419, 211, 420, 271, 294, 266],
	# [425, 220, 471, 220, 472, 273, 425, 271],gg
	# [475, 219, 561, 219, 562, 275, 477, 274],
	# [567, 224, 642, 228, 644, 279, 567, 277],
	# ])
	# poly = []
	# for line in gt: 
	# 	coord = np.array(line).reshape(4,2) 
	# 	poly.append(Polygon(coord).convex_hull) 

	# # print(len(poly))
	# union_poly = np.concatenate((poly[0],poly[1]))
	# print(union_poly)
	# compute_iou(pred,gt)
