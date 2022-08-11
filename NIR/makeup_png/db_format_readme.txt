- 482 labeled eye images with makeup and 336 unlabeled
- LG2200 sensor was used for image capturing
- Each folder corresponds to a subject, and each subject have a json containing VIA marks for segmentation tasks.
- The structure of the json objects is explained below:

"05487d59.png.bmp308278": {                             ######## -> Filename + size as string (VIA format)
    "filename": "05487d59.png",                         ######## -> Filename
    "size": 308278,                                     ######## -> Size of file. See Python os.path.getsize(path)
    "regions": [                                        ######## -> Regions list with each section of the eye
        {
            "shape_attributes": {                       
                "name": "polygon",                      ######## -> VIA shape name
                "all_points_x": [...],                  ######## -> All points (int) in X-axis
                "all_points_y": [...]                   ######## -> All points (int) in Y-axis
            },
            "region_attributes": {                      ######## -> Metadata
                "Eye": "pupil"                          ######## -> Class type
            }
        },
    ],
    "file_attributes": {}                               ######## -> Extra metadata # Non-used
}