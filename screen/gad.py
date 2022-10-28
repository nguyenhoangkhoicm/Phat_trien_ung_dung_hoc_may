import cv2
import argparse
from csv import writer

# chúng ta sẽ tạo ra hàm highlightFace , hàm này sẽ trả về frame hình và tọa độ khuôn mặt


def highlightFace(net, frame, conf_threshold=0.7):
    #tạo khung hình khi phát hiện gương mặt
    frameOpencvDnn = frame.copy() 
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    #sử dụng toạ độ đã lấy được phát hiện vẽ ra khung hình
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [
                                 104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3]*frameWidth)
            y1 = int(detections[0, 0, i, 4]*frameHeight)
            x2 = int(detections[0, 0, i, 5]*frameWidth)
            y2 = int(detections[0, 0, i, 6]*frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2),
                          (0, 255, 0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, faceBoxes


parser = argparse.ArgumentParser()
parser.add_argument('--image')
args = parser.parse_args()

# xác định đường dẫn của các tập dữ liệu khuôn mặt , phát hiện tuổi và giới tính .
faceProto = r".\models\opencv_face_detector.pbtxt"
faceModel = r".\models\opencv_face_detector_uint8.pb"
ageProto = r".\models\age_deploy.prototxt"
ageModel = r".\models\age_net.caffemodel"
genderProto = r".\models\gender_deploy.prototxt"
genderModel = r".\models\gender_net.caffemodel"
#Xác định danh sách nhóm tuổi và giới tính mà chúng ta sẽ dự đoán.
MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)',
           '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList = ['Nam', 'Nu']
#Tải các mô hình phát hiện khuôn mặt, phát hiện tuổi và giới tính bằng cách sử dụng 
# đường dẫn nơi chúng ta lưu trữ trước đó.
faceNet = cv2.dnn.readNet(faceModel, faceProto)
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto)

# khởi tạo luồng video và cho phép cảm biến máy ảnh bật lên.
video = cv2.VideoCapture(args.image if args.image else 0)
padding = 20
#tạo vòng lặp, lấy các khung hình từ camera và sau đó gọi hàm highlightFace () với faceNet và các tham số khung . 
#giá trị trả về này sẽ được lưu trữ trong các biến resultimg và faceboxes
while cv2.waitKey(1) < 0:
    hasFrame, frame = video.read()
    if not hasFrame:
        cv2.waitKey()
        break

    resultImg, faceBoxes = highlightFace(faceNet, frame)
    if not faceBoxes:
        print("Khong phat hien guong mat")

    for faceBox in faceBoxes:
        face = frame[max(0, faceBox[1]-padding):
                     min(faceBox[3]+padding, frame.shape[0]-1), max(0, faceBox[0]-padding):min(faceBox[2]+padding, frame.shape[1]-1)]
#Sau khi nhận được khung hình khuôn mặt, chúng ta tạo ra một đốm màu 4 chiều từ hình ảnh. 
# Tiếp theo chúng ta chia tỷ lệ,thay đổi kích thước và chuyển các giá trị trung bình vào.
        blob = cv2.dnn.blobFromImage(
            face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
#Gọi các mô hình phát hiện tuổi và giới tính và chuyển đổi đốm màu 4 chiều về dạng dữ liệu nhị phân.
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        print(f'Gioi tinh: {gender}')
# chuyển đốm màu qua mô hình phát hiện giới tính và nhận được sự tương thích của hai lớp (Nam & Nữ). 
# Giá trị nào cao hơn thì đó là giới tính của người trong ảnh.
        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        print(f'Tuoi: {age[1:-1]} tuoi')
#Xác định độ tuổi
        if age[1:-1] == ('60-100'):
            print("Người già")
        elif age[1:-1] == ('4-6'):
            print('Trẻ em')
        elif age[1:-1] == ('0-2'):
            print('Trẻ em')
        elif age[1:-1] == ('8-12'):
            print('Trẻ em')
        elif age[1:-1] == ('15-20'):
            print('Thanh thiếu niên')
        elif age[1:-1] == ('25-32'):
            print('Thanh thiếu niên')
        elif age[1:-1] == ('38-43'):
            print('Trưởng thành')
        elif age[1:-1] == ('48-53'):
            print('Trưởng thành')
        else:
            print('Chưa có dữ liệu')
           
#Xuất dữ liệu vào file csv
        List=[f'{gender}',f'{age}']
        with open(r'.\data\gender_age.csv','a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(List)
            f_object.close()

       
#Sau khi nhận diện được tuổi và giới tính.
#Tạo một khung hình với kích thước và độ rộng của khung hình được chỉ định, và thêm tuổi và giới tính vào khung hình.
        cv2.putText(resultImg, f'{gender},Tuoi:{age}', (
            faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("Nhan dien gioi tinh va tuoi", resultImg)
        
