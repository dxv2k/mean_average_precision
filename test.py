from mean_average_precision import metric_base
import numpy as np
import mean_average_precision
from mean_average_precision import MetricBuilder

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
        [199, 194, 287, 201, 289, 267, 196, 263],
        [291, 207, 419, 211, 420, 271, 294, 266], 
        [425, 220, 471, 220, 472, 273, 425, 271], 
        [475, 219, 561, 219, 562, 275, 477, 274], 
        [567, 229, 642, 228, 644, 279, 567, 277], 
        [567, 224, 642, 240, 644, 279, 567, 277], 
        [567, 224, 642, 228, 644, 290, 567, 277], 
        [567, 224, 642, 243, 644, 279, 567, 277], 
   ])

    print(MetricBuilder.get_metrics_list())

    # Create metric_fn 
    metric_fn = MetricBuilder.build_evaluation_metric("map_2d",
                                                num_classes=1)

    metric_fn.add(pred,gt)
    # for i in range(10): 
    #     metric_fn.add(pred,gt)
    #     # print(metric_fn.value)
    print(metric_fn.value(iou_thresholds=np.arange(0.5, 1.0, 0.05), recall_thresholds=np.arange(0., 1.01, 0.01), mpolicy='soft')['mAP']) 
