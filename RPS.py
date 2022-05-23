import cv2
from keras.models import load_model
import numpy as np
from random import choice
import time
import os

######################################################################
#                              FUNCTIONS                             #
######################################################################

def get_computer_choice(actions: list) -> str:
    """
    Choose (at random) computer action.

    Args:
        actions: a list, containing actions

    Returns:
        a string, denoting a selected action
    """

    action = choice(actions)
    print(f"Computer action: {action}")

    return action

def get_prediction(model: object, actions: list, number_of_counts: int = 3, count_duration: float = 1.0, camera_duration: float = 3.0) -> str:
    """
    Get image. Use keras-tensorflow model to classify the image. Infer player's action. 

    Args:
        model:            an object, keras-tensorflow model
        actions:          a list, containing labels of player's actions
        number_of_counts: an integer, a highest number during countdown
        count_duration:   a float, time given number is displayed in the camera
        camera_duration:  a float, time delay before caountdown and an image being taken

    Returns:
        a string an inferred players' action
    """

    # GET PREDICTION

    # setup
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # initialize time count
    total_time = number_of_counts*count_duration + camera_duration
    countdown = number_of_counts
    time_elapsed_reset = 0 
    time_elapsed = 0  
    start = time.time()
    delayed_start= start

    # define color
    color=(255*0.87,255*0.63,255*0.87)

    # capture image for 'camera_duration' seconds
    while time_elapsed  < total_time:

        # capture framy-by-frame
        ret, frame = cap.read()

        # initiate the countdown        
        if countdown > 0:

            # print countdown
            cv2.putText(frame, str(countdown),(300, 250), cv2.FONT_HERSHEY_COMPLEX,2,color,cv2.LINE_4,1,)

            # update countdown
            if time_elapsed_reset > count_duration:

                delayed_start += count_duration
                countdown -=1

        # # save the pic
        # if countdown == 2:

        #     cv2.imwrite('/home/piotr/Documents/projects/RPS/mypic.png',frame)
        

        # show a frame titled 'Action'
        cv2.imshow("Action", frame)

        # Press q to close the window
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

        # update time
        current_time = time.time() 
        time_elapsed_reset = current_time - delayed_start
        time_elapsed  = current_time - start      

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
    """
    Determine who won.

    Args:
        player_action: a string, denoting inferred player action
        computer_action: a string, denoting action selected by a computer
        lost_against: a dict, determining a winner

    Returns:
        An int, +1 if a player won, -1 if a computer won
    """

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


def play(actions: list, lost_against: dict, number_of_counts: int=3, count_duration: float=2.0, camera_duration: float = 3.0):
    """
    Play the game.

    Args: 
        actions:          a list, containing labels of player's actions
        lost_against:     a dict, determining a winner
        number_of_counts: an integer, a highest number during countdown
        count_duration:   a float, time given number is displayed in the camera
        camera_duration:  a float, time delay before caountdown and an image being taken
    """

    # setup
    model = load_model("keras_model.h5")

    # clear bazzilion warinings
    os.system("cls" if os.name == "nt" else "clear")

    # acknowledgements
    print("\nAll hail Sam Kass! Hail!\n")
    print("Press 'Q' any time to Quit.\n")

    # initialisation
    player_win_count = 0
    computer_win_count = 0
    game_continues = True

    while game_continues:

        # read player action
        player_action = get_prediction(model=model, actions=actions, number_of_counts=number_of_counts, count_duration=count_duration, camera_duration=camera_duration)

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
play(actions=actions, lost_against=lost_against, number_of_counts=3, count_duration=2.5, camera_duration=3.0)
