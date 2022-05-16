import cv2
from keras.models import load_model
import numpy as np
from random import choice
import time
import os

######################################################################
#                              FUNCTIONS                             #
######################################################################


def countdown(number_of_counts: int = 3, count_duration: float = 1.0):

    # total countdown time
    total_delay = number_of_counts * count_duration
    countdown = number_of_counts

    # output
    print("Countdown!")
    print("")

    # initialize time count
    start = time.time()
    end = start
    time_elapsed = 0

    # wait 'count_duration' seconds for every count
    while time_elapsed < total_delay:

        # wait 'count_duration' seconds
        while (end - start) - time_elapsed < count_duration:
            end = time.time()

        # output
        print(countdown)

        # update
        time_elapsed += count_duration
        countdown -= 1

    print("")


def get_computer_choice(actions: list) -> str:

    action = choice(actions)
    print(f"Computer action: {action}")

    return action


def test_camera(camera_duration: float = 5.0):

    # setup
    cap = cv2.VideoCapture(0)

    # initialize time count
    start = time.time()
    end = start

    # turn on camera
    # capture image for 'camera_duration' seconds
    while end - start < camera_duration:

        # capture framy-by-frame
        ret, frame = cap.read()

        cv2.putText(frame, "3", (200, 200), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), cv2.LINE_4, 1)


        # show a frame titled 'Action'
        cv2.imshow("Action", frame)

    
        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # update time
        end = time.time()


def get_prediction(model: object, actions: list, camera_duration: float = 3.0):

    # setup
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # initialize time count
    start = time.time()
    end = start

    # capture image for 'camera_duration' seconds
    while end - start < camera_duration:

        # capture framy-by-frame
        ret, frame = cap.read()

        # show a frame titled 'Action'
        cv2.imshow("Action", frame)

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # update time
        end = time.time()

    # CLEANUP

    # after the loop release the cap object
    cap.release()

    # destroy all the windows
    cv2.destroyAllWindows()

    # interpolation = resampling using pixel area relation (gives moire-free results)
    resized_frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    # convert image to a numpy array
    image_np = np.array(resized_frame)

    # TODO: check if this is 127.5

    # convert values in [0,255] interval into [-1,1]
    normalized_image = (image_np.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image

    # predict action
    prediction = model.predict(data)
    ind = np.argmax(prediction[0])
    action = actions[ind]

    # output
    print(f"Inferred player action: {action}")

    return action


def get_winner(player_action: str, computer_action: str, lost_against: dict) -> int:

    if computer_action in lost_against[player_action]:

        print("\nThis time you won")
        won = 1

    elif player_action in lost_against[computer_action]:

        print("\nThis time computer won")
        won = -1

    else:

        print("\nIt is a draw!")
        won = 0

    print("")

    return won


def play(actions: list, lost_against: dict, camera_duration: float = 5.0):

    # setup
    model = load_model("keras_model.h5")

    # clear bazzilion warinings
    os.system("cls" if os.name == "nt" else "clear")

    # acknowledgements
    print("\nAll hail Sam Kass! Hail!\n")
    print("Press 'Q' any time to Quit.\n")

    # test camera
    print("Calibrating camera...", end="")
    test_camera(camera_duration=7.0)
    print("\n")

    # initialisation
    player_win_count = 0
    computer_win_count = 0
    game_continues = True

    while game_continues:

        # initiate the countdown
        countdown(number_of_counts=3, count_duration=1.5)

        # read player action
        player_action = get_prediction(
            model=model, actions=actions, camera_duration=camera_duration
        )

        if player_action != "Nothing":

            computer_action = get_computer_choice(actions=actions[:-1])
            won = get_winner(
                player_action=player_action,
                computer_action=computer_action,
                lost_against=lost_against,
            )

            if won == 1:
                player_win_count += 1
            elif won == -1:
                computer_win_count += 1

            game_continues = player_win_count < 3 and computer_win_count < 3

        else:
            print("Hey! Make your move.\n")

    if player_win_count == 3:

        print("Congrats. You won the entire game!")

    elif computer_win_count == 3:

        print("Computer won the game. So sorry!")

    print("")


######################################################################
#                            THE RPS GAME                            #
######################################################################

# action labels (matching 'labels.txt')
actions = ["Rock", "Paper", "Scissors", "Lizard", "Spock", "Nothing"]

# dict with winning actions: 'Rock' > 'Lizard', 'Scissors'
lost_against = {
    "Rock": ["Lizard", "Scissors"],
    "Paper": ["Rock", "Spock"],
    "Scissors": ["Paper", "Lizard"],
    "Spock": ["Scissors", "Rock"],
    "Lizard": ["Spock", "Paper"],
}

# play the game
play(actions=actions, lost_against=lost_against, camera_duration=6.0)
