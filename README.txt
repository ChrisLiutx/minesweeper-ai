Minesweeper game and AI created by Chris Liu 2021

Demo: https://youtu.be/BD6RgtYZOZg

Completely coded from scratch by me as a personal project. ALL the code below are mine. I did read up and do some research, which I'll credit below. Actual coding time around 2 days?
For windows users, execute run.bat which automatically checks for presence of Python installation.

#Features:
- It's a minesweeper game
- You step on mine, you die
- I know I'm supposed to do documentation, but I'm lazy. Read the code yourself.
- Automatically open all cells around it if the one you open is a 0.
- First cell that you click will never be a mine
- The AI will attempt to solve what it can, but since it's possible to result in situations where you can't be certain of the location of a mine, it is also luck based.

#Approach
I wanted to make a simple game at first, and then try to solve it using AI. Minesweeper interested me, since the rules are rather simple. After some research, I found out that minesweeper has been proven to be NP-complete by Richard Kaye. Hence, unless P = NP, then there shouldn't be a simple, straightforward way to solve this problem in polunomial time.

While there are attempts to use Q Learning or other forms of AI to solve minesweeper, I decided to start with the most intuitive one: Constraint Satisfaction Problem (CSP). Since minesweeper is essentially a set of rules that constrain the locations of mines and safe cells, this seems like the obvious way to solve it. This is also how humans tend to solve minesweepers.

#Algorithms
Currently, I only implemented the basics, where the AI will open all the obvious cells where it's 100% certain it's safe, or flag if it's a bomb. This is rather effective in reducing most of the human interaction, but it fails when it reaches situations where it cannot be 100% certain. It also cannot look into cases where multiple cells share information, that constrains the problem, although looking at a single individual cell fails. Thus, at the current stage, the AI requires some human interaction when it gets stuck, but can solve the board quite well. I can implement a random guessing algorithm to complement the time when this stops, but I have plans to implement a probability based AI in the future so that seems unnecessary now.


#Credits
Thank you for these amazing websites! Really helped me out during the research. Do check them out! (Sorry no APA citations cause I'm a CS student not trying to write a research paper)
> https://static1.squarespace.com/static/5cdb03d98dfc8c9c6d3b2ba0/t/5ce1caecb6e19700013e3182/1558301421713/Minesweeper.pdf
> https://luckytoilet.wordpress.com/2012/12/23/2125/
> https://www.askpython.com/python/examples/create-minesweeper-using-python
> http://www.cs.toronto.edu/~cvs/minesweeper/minesweeper.pdf
> google.com for being a bro. Also I received the google foobar challenge while researching for this project so yay?
