def get_crossing(line1_coordinates, line2_coordinates):
    crossing_point_coordinates = None

    line1_x1 = line1_coordinates[0][0]
    line1_y1 = line1_coordinates[0][1]
    line1_x2 = line1_coordinates[1][0]
    line1_y2 = line1_coordinates[1][1]

    line2_x1 = line2_coordinates[0][0]
    line2_y1 = line2_coordinates[0][1]
    line2_x2 = line2_coordinates[1][0]
    line2_y2 = line2_coordinates[1][1]

    try: 
        crossing_point_coordinates = []


        slope_line1 = (line1_y2 - line1_y1) / (line1_x2 - line1_x1)
        b1 = line1_y1 - (line1_x1 * (line1_y2 - line1_y1) / (line1_x2 - line1_x1))

        slope_line2 = (line2_y2 - line2_y1) / (line2_x2 - line2_x1)
        b2 = line2_y1 - (line2_x1 * (line2_y2 - line2_y1) / (line2_x2 - line2_x1))

        x = (b2 - b1) / (slope_line1 - slope_line2)
        y = slope_line1 * x + b1

        crossing_point_coordinates.append(x)
        crossing_point_coordinates.append(y)
        return crossing_point_coordinates
    except:
        return "Error, null crossing point coordinates"

print(get_crossing(line1_coordinates=[[1, 0], [1, 11]], line2_coordinates=[[0,9], [5, 9]]))