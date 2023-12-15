from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)



@app.route('/', methods=['GET'])
def dropdown():
    sizes = ['3x3', '4x4', '5x5']
    return render_template('form.html', sizes=sizes)

@app.route('/card', methods=['POST'])
def card():
    list = ["Flying", "Android spouse", "Alien invasion", "Superbug", "Zombie apocalypse", "Forest walk", "Evil penpal", "Lonely whale", "Cat overlords", "Time travel", "Hot air balloon", "Creation myth", "Reality TV", "Greatest fear", "Soulmates", "Winning the lottery", "Brought to justice", "Dodgeball rivalry", "Spy hunter", "Watergun fight", "Tallest bridge", "Turkey dinner", "Tipsy mermaid", "Secret king", "Creation myth", "Highly improbable", "Snuffed out", "Bird bones", "Going live", "Long journey", "Masks", "Silly hat"]

    card = []
    dropdownval = request.form['size']

    if dropdownval == '3x3':
        numbers = random.sample(range(30), 9)
        for num in numbers:
            card.append(list[num])
        if request.form.get('free_space'):
            card[4] = "Free space"
        else:
            pass

    elif dropdownval == '4x4':
        numbers = random.sample(range(30), 16)
        for num in numbers:
            card.append(list[num])
        if request.form.get('free_space'):
            card[5] = "Free space"
        else:
            pass

    elif dropdownval == '5x5':
        numbers = random.sample(range(30), 25)
        for num in numbers:
            card.append(list[num])
        if request.form.get('free_space'):
            card[12] = "Free space"
        else:
            pass


    return render_template("card.html", card=card, length=len(card))


if __name__ == "__main__":
    app.run()
