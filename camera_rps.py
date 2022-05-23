import cv2
from keras.models import load_model
import numpy as np
import time

def countdown(number_of_counts = 3, count_duration = 1.5):

    # total countdown time
    total_delay = number_of_counts * count_duration
    countdown = number_of_counts

    # output
    print("")
    print('Countdown!')
    print("")
    print(countdown)

    # initialize time count
    start = time.time()
    end = start
    time_elapsed = 0
     
    # wait 'count_duration' seconds for every count
    while time_elapsed < total_delay:

        # wait 'count_duration' seconds
        while (end-start) - time_elapsed < count_duration:
            end = time.time()

        # update
        time_elapsed += count_duration
        countdown -= 1 

        # output
        print(countdown)
    
    print('...')

def get_prediction(model, actions_list: list):

    # setup
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # repeat once
    count = 0

    while count < 1: 

        # capture framy-by-frame
        ret, frame = cap.read()

        # interpolation = resampling using pixel area relation (gives moire-free results)
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)

        # convert image to a numpy array
        image_np = np.array(resized_frame)
    
        # convert values in [0,255] interval into [-1,1]
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 
        data[0] = normalized_image

        # predict action
        prediction = model.predict(data)
        ind = np.argmax(prediction[0])
        action = actions_list[ind]
    
        # show a frame titled 'Action'
        cv2.imshow('Action', frame)

        # Press q to close the window
        if cv2.waitKey(3000) & 0xFF == ord('q'):
            break
            
        count +=1
    
    # CLEANUP

    # after the loop release the cap object
    cap.release()

    #  destroy all the windows
    cv2.destroyAllWindows()

    return action

def run_rps():

    # action labels (matching 'labels.txt') 
    actions_list = ['Rock','Paper','Scissors','Lizard','Spock','Nothing']

    # setup
    model = load_model('keras_model.h5')
    
    # acknowledgements
    print("\nAll hail Sam Kass! Hail!")
    print("")
    print("Press 'Q' any time to Quit. ")
    print("")

    # run the game
    game_continues= True

    count = 1
    while game_continues:

        # countdown
        countdown()

        # get action
        action = get_prediction(model, actions_list)

        print(f"Count {count}, predicted action: {action}")

        game_continues = (count  < 3)

        count += 1

######

run_rps()