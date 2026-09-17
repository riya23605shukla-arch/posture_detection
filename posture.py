import cv2
import mediapipe as mp
import numpy as np
import winsound
import time
import csv

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle
    return angle

bad_posture_start = 0
alert_given = False

good_time = 0
bad_time = 0
last_update_time = time.time()

while True:
    success, img = cap.read()
    if not success:
        break

    current_time = time.time()
    time_diff = current_time - last_update_time
    last_update_time = current_time

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(img_rgb)

    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark

        # Key points: Shoulder, Ear, Hip
        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        ear = [landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x,
               landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]
        hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
               landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

        angle = calculate_angle(ear, shoulder, hip)

        # UI Window Panel
        cv2.rectangle(img, (0,0), (350,120), (50,50,50), -1)
        cv2.putText(img, f"ANGLE: {int(angle)}", (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        # Posture Detection Logic
        if angle < 150:  # BAD POSTURE
            cv2.putText(img, "BAD POSTURE", (10,90), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 3)

            bad_time += time_diff

            if bad_posture_start == 0:
                bad_posture_start = time.time()

            if time.time() - bad_posture_start > 5 and not alert_given:   # After 5 seconds continuously
                winsound.Beep(1000, 600)
                alert_given = True

        else:   # GOOD POSTURE
            cv2.putText(img, "GOOD POSTURE", (10,90), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)
            good_time += time_diff

            bad_posture_start = 0
            alert_given = False

        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    cv2.imshow("AI Posture Correction System", img)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC Key
        break

# Save session report to CSV
with open("posture_log.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Session Summary", f"Good Time: {round(good_time,2)} sec", f"Bad Time: {round(bad_time,2)} sec"])

cap.release()
cv2.destroyAllWindows()
