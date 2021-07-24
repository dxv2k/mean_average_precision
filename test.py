import numpy as np
import mean_average_precision
# from mean_average_precision import metric_builder

if __name__ == "__main__":
    # QUAD format [x1,y1,x2,y2,x3,y3,x4,y4] 
    gt = np.array([
        [196, 194, 287, 201, 289, 267, 196, 263],
        [291, 207, 419, 211, 420, 271, 294, 266], 
        [425, 220, 471, 220, 472, 273, 425, 271], 
        [475, 219, 561, 219, 562, 275, 477, 274], 
        [567, 224, 642, 228, 644, 279, 567, 277], 
   ])

    # QUAD format [x1,y1,x2,y2,x3,y3,x4,y4] 
    pred = np.array([
        [196, 194, 287, 201, 289, 267, 196, 263],
        [291, 207, 419, 211, 420, 271, 294, 266], 
        [425, 220, 471, 220, 472, 273, 425, 271], 
        [475, 219, 561, 219, 562, 275, 477, 274], 
        [567, 224, 642, 228, 644, 279, 567, 277], 
   ])

    print(MetricBuilder.get_metrics_list())