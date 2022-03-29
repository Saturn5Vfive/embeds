from flask import *
import json
import base64

app = Flask(__name__)

@app.route("/")
def generate_embed():
    try:
        if not "d" in request.args:
            return render_template('large_embed.html', url="https://mole-embeds.herokuapp.com/", image='https://tenor.com/view/yes-monty-mole-belly-drum-gif-13805191.gif', description='it doesnt look like you put any data to be associated with the embed?', color="#fad47a", title="Moles Embed Generator")
        pdata = request.args.get("d")
        rdata = base64.b64decode(pdata.encode('ascii')).decode('ascii')
        data = json.loads(rdata)
        if not 'large' in data:
            return render_template('embed.html', url=data['url'], image=data['image'], description=data['description'], color=data['color'], title=data['title'])
        if data['large'] == True:
            return render_template('large_embed.html', url=data['url'], image=data['image'], description=data['description'], color=data['color'], title=data['title'])
        else:
            return render_template('embed.html', url=data['url'], image=data['image'], description=data['description'], color=data['color'], title=data['title'])
    except Exception as e:
        print(e)
        return Response(status=400)
