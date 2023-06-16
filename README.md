# Serving Model

Sample Response:
```json
{
  "predictions": [
    {
      "detection_classes": [3.0, 1.0, 4.0, ...],
      "raw_detection_scores": [...],
      "detection_anchor_indices": [...],
      "num_detections": 100.0,
      "detection_multiclass_scores": [...],
      "raw_detection_boxes": [...],
      "detection_boxes": [
        [
          0.130028903, 
          0.342044801, 
          0.937894762, 
          0.624998093
        ],
        [
          0.130028903, 
          0.342044801, 
          0.937894762, 
          0.624998093
        ],
        [
          0.107640505, 
          0.343304783, 
          0.935199499, 
          0.636344671
        ],
        ...
      ],
      "detection_scores": [
        0.307633072, 0.294662386, 0.26344031, ...
      ]
    }
  ]
}
```