import json
import cv2


def main():
    cap = cv2.VideoCapture("badapple.mp4")
    frames = []

    for frame_number in range(6572):
        ret, frame = cap.read()
        if frame_number % 6:
            continue

        edframe = []
        for line in range(len(frame)):
            eline = ''
            for column in range(len(frame[line])):
                pixel_sum = sum(frame[line][column]) // 3
                if pixel_sum >= 128:
                    eline += "##"
                else:
                    eline += "  "
            edframe.append(eline)

        frames.append(edframe)
        if not frame_number % 600:
            print(frame_number)

    data = {"data": frames}

    data_json = json.dumps(data)

    with open("frames.json", 'w') as f:
        f.write(data_json)


if __name__ == '__main__':
    main()
