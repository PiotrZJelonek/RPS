# Rock-Paper-Scissors-Lizard-Spock

This is an implementation of the iconic Rock-Paper-Scissors-Lizard-[Spock](https://intl.startrek.com/database_article/spock) game, featuring in **Season 5**, **Episode 17** - *The Rothman Disintegration* - of **The Big Bang Theory** show. This episode was originally aired on the 16<sup>th</sup> of February 2012. While Sheldon's intuitive explainaition of the rules is available [here](https://www.youtube.com/watch?v=x5Q6-wMx-K8), the game should be immediately recognizable to any true geek.

## Rules of the game

"Oh, it is very simple. Scissors cuts paper. Paper covers rock. Rock crushes lizard. Lizard poisons [Spock](https://www.amazon.com/I-Am-Spock-Leonard-Nimoy-audiobook/dp/B001H071EU/ref=sr_1_2?crid=2KRM58IYEZ3QX&keywords=I+am+spock&qid=1651781329&sprefix=i+am+spock%2Caps%2C383&sr=8-2). [Spock](https://en.wikipedia.org/wiki/Leonard_Nimoy) smashes scissors. Scissors decapitate lizard. Lizard eats paper. Paper disproves [Spock](https://intl.startrek.com/database_article/spock). [Spock](https://www.amazon.com/Am-Not-Spock-Leonard-Nimoy/dp/0890871175/ref=sr_1_1?crid=3355SCP81PX3W&keywords=I+am+not+spock&qid=1651781425&s=audible&sprefix=i+am+not+spock%2Caudible%2C148&sr=1-1-catcorr) vaporises rock and as it always has rock crushes scissors."

<p align="center" width="100%">
    <img width="66%" src="https://github.com/PiotrZJelonek/RPS/blob/develop/rpsls.webp?raw=true">
</p> 

<p align = "center">
Fig. 1 - Outcomes of RPSLS on a diagram.
</p>

**Fun fact**: A single [mixed strategy Nash equilibrium](https://www.youtube.com/watch?v=IjgYLM4KgFg) of the game is playing every strategy with probability of 20%

## Image Recognition

- Used [TeachableMachine](https://teachablemachine.withgoogle.com/) to generate the sample images and a [Keras-Tensorflow](https://keras.io/about/) deep learning model that can be taught to classify them.
- My model features 6 basic image classes: *Rock*, *Paper*, *Scissors*, *Lizard*, *Spock* and *Nothing*. The training sample consists of 500 images of each class.
- Hyperparameters: number of epochs **N=50**, size of each batch **n=16**, learning rate **<img src="https://render.githubusercontent.com/render/math?math=\rho=0.01">**

- Trained the model in a cloud on the provided sample. Then downloaded it to be used locally by the application (game).

<p align="center" width="100%">
    <img width="33%" src="https://github.com/PiotrZJelonek/RPS/blob/develop/nothing.png?raw=true">
    <img width="33%" src="https://github.com/PiotrZJelonek/RPS/blob/develop/spock.png?raw=true">
</p>

<p align = "center">
Fig. 2 - Computer Vision classification - <em>Nothing</em> and <em>Spock</em>.
</p>

## Environment

- Created new virtual environment <em>rps</em> with
```conda
conda create -n rps python=3.8
```
- Installed [opencv-python](https://pypi.org/project/opencv-python/), 
[tensorflow](https://www.tensorflow.org/learn),
and [ipykernel](https://pypi.org/project/ipykernel/)
- Added [black](https://pypi.org/project/black/) to the mix to *blacken* the code later via
```black
black RPS.py
```
- Checked the environment using
```pip
pip freeze > requirements.txt
```
**Note**: A great source for OpenCV tutorials can be found [here](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

## Determining the winner

- It is practical to map loosing actions to winnig actions using a dictionary
```python
"""
lost_against = {
    'Rock': ['Lizard', 'Scissors'], 
    'Paper': ['Rock','Spock'], 
    'Scissors': ['Paper','Lizard'], 
    'Spock': ['Scissors','Rock'], 
    'Lizard': ['Spock', 'Paper'] 
    }
"""
```
- To determine the winner, it is enough then to check
```python
"""
if computer_action in lost_against[player_action]:
    print("Player won")
    
elif player_action in lost_against[computer_action]:
    print("Computer won")

else: 
    print("It is a draw")

"""
```
- Basic functionality
<p align="center" width="100%">
    <img width="66%" src="https://github.com/PiotrZJelonek/RPS/blob/develop/cant_loose_with_spock.png?raw=true">
</p> 
<p align = "center">
Fig. 3 - You can't loose with <em>Spock</em>! 
</p>

## Countdown

- My <em>countdown</em> function - an early (but functional!) version

```python
"""
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
"""
```
- At the end I integrated <em>countdown</em>  with a function, identifying an image from the camera.

## Final game being played

- Playing the game

<p align="center" width="100%">
    <img width="33%" src="https://github.com/PiotrZJelonek/RPS/blob/develop/spock_1.png?raw=true">
    <img width="33%" src="https://github.com/PiotrZJelonek/RPS/blob/develop/lizard_2.png?raw=true">
</p>

<p align = "center">
Fig. 4 - Now <em>countdown</em>  is displayed in the camera.  
</p>

- Now the game counts down from 3 down to 1. Next the image is captured after another 3 seconds.
- Snapshot from the terminal
<p align="center" width="100%">
    <img width="66%" src="https://github.com/PiotrZJelonek/RPS/blob/develop/full_game.png?raw=true">
</p> 
<p align = "center">
Fig. 5 - Log of the full game
</p>
