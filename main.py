import os
from api import api_bp
from config import *
from handlers import *


app = Flask(__name__)


@app.route('/dashboard')
def dashboard():
    return render_template('index.html')
    

@app.route("/" + TOKEN, methods=["POST", "GET"])
def checkWebhook():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "Your bot application is still active!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://bitscrow.onrender.com" + "/" + TOKEN)
    return "Bitscrow Bot running!", 200


def run_web():
    if __name__ == "__main__":
        # app.register_blueprint(api_bp)
        app.run(
            host="0.0.0.0",
            threaded=True,
            port=int(os.environ.get('PORT', 5004)),
        )


def run_poll():
    webhook_info = bot.get_webhook_info()
    if webhook_info.url:
        bot.delete_webhook()
    bot.infinity_polling()
    print("Bot polling!")


if WEBHOOK_MODE == "False":
    run_poll()
else:
    run_web()
