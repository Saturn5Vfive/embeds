from flask import *

app = Flask(__name__)

@app.route("/")
def generate_embed():
    try:
        if not "d" in request.args:
            return render_template('large_embed.html', url="https://mole-embeds.herokuapp.com/", image='https://tenor.com/view/yes-monty-mole-belly-drum-gif-13805191.gif', description='it doesnt look like you put any data to be associated with the embed?', color="#fad47a", title="Moles Embed Generator")
        data = request.args.get("d")
    except:
        return Response(status=400)
