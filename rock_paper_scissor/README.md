# Rock, Paper and Scissor game

If you’re unfamiliar, rock paper scissors is a hand game for two or more players. 
Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock (a fist), 
a piece of paper (palm facing downward), or a pair of scissors (two fingers extended). The rules are straightforward:

* Rock smashes scissors.
* Paper covers rock.
* Scissors cut paper.
## program Flow
First, we are importing the random module to enable us randomize computer choices:
```python
import random
```
For, the user input, we create a sequence(in this case a list) to store the possible choices that the user
can pick from. Taking an input from the user is straight forward suing the ```input()``` functions as follows

```python
user_choices = ["rock", "paper", "scissor"]
user_input = input("Please select your choices (rock, paper and scissor):")
