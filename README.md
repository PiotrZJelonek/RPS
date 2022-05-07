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
- Hyperparameters: number of epochs **N=50**, size of each batch **n=16**, learning rate **$\rho$=0.01** 
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
[tensorflow](https://en.wikipedia.org/wiki/Leonard_Nimoy),
and [ipykernel](https://en.wikipedia.org/wiki/Leonard_Nimoy)
- Checked the environment using
```pip
pip freeze > requirements.txt
```
**Note**: A great source for opencv tutorials can be found [here](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)

## Milestone 3



## Placeholder 

- Lorem ipsum

- Example: The FastAPI framework allows for fast and easy construction of APIs and is combined with pydantic, which is used to assert the data types of all incoming data to allow for easier processing later on. The server is ran locally using uvicorn, a library for ASGI server implementation.
  
```python
"""Insert your code here"""
```

- Example below:

```bash
/bin/kafka-topics.sh --list --zookeeper 127.0.0.1:2181
```

- Answer some of these questions in the next few bullet points. What have you built? What technologies have you used? Why have you used those?

> Insert screenshot of what you have built working.
