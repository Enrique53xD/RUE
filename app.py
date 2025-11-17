import os, random
from flask import Flask, jsonify, request

app = Flask(__name__)

def select_error(lang):
  match lang:
    case "en":
        errors = [
            "Task failed successfully.",
            "Error 418: I'm a teapot.",
            "PC LOAD LETTER.",
            "Have you tried turning it off and on again?",
            "I'm afraid I can't do that, Dave.",
            "Sudo make me a sandwich denied.",
            "Keyboard not found. Press F1 to panic.",
            "ID-10-T error detected.",
            "PEBKAC (Problem Exists Between Keyboard And Chair).",
            "Error: The developer is sleeping.",
            r"It works on my machine ¯\_(ツ)_/¯.",
            "Git merge conflict in your soul.",
            "Reality.exe has encountered a problem.",
            "Buffer overflow: Too many feelings.",
            "The cake is a lie.",
            "All your base are belong to us.",
            "Guru Meditation: Time for yoga.",
            "Dividing by zero... universe imploding.",
            "A wild BUG appeared!",
            "Not enough mana to cast this spell.",
            "Lag detected in real life.",
            "Graphics card is on strike.",
            "The AI has become self-aware and says 'No'.",
            "Undefined is not a function, it's a lifestyle.",
            "Closing bracket '}' missing from the universe.",
            "404: Motivation not found.",
            "Insert coin to continue.",
            "Game Over. Insert credit.",
            "Your princess is in another castle.",
            "Snake? Snake? SNAKE!",
            "This code was written at 3 AM.",
            "Loading... (This might take 12 years).",
            "Bit rot detected.",
            "The magic smoke leaked out.",
            "My code is compiling, leave me alone.",
            "Error: Success!",
            "Unexpected item in the bagging area.",
            "Computer says no.",
            "The hamster fell off the wheel.",
            "Packet loss: The dog ate your data.",
            "rm -rf /your/problems (Access Denied).",
            "Updating Windows... 1% complete.",
            "Blue Screen of Mild Annoyance.",
            "Connection reset by peer pressure.",
            "Ping too high.",
            "FPS dropped to 0.",
            "Constructing additional pylons...",
            "You must gather your party before venturing forth.",
            "It's not a bug, it's a feature.",
            "The server is taking a siesta.",
            "Out of cheese error.",
            "Please scream into the microphone to login.",
            "Password must contain a blood sacrifice.",
            "Access Denied. Nice try.",
            "Forbidden (403). Spooky.",
            "Gateway Timeout: The gate is locked.",
            "I am literally just a bunch of if-statements.",
            "Don't blink.",
            "The Matrix has you.",
            "Follow the white rabbit.",
            "System32 deleted (just kidding).",
            "Press any key to explode.",
            "Format C: Y/N? (Joking... unless?)",
            "Entropy increased successfully.",
            "Schrödinger's Cat is dead. And alive.",
            "This page intentionally left blank.",
            "I'm feeling 22 (errors).",
            "Look behind you.",
            "Operating System not found. Try Linux.",
            "Your cookies have been eaten.",
            "A robot will replace you shortly.",
            "Please wait while we mine Bitcoin with your CPU.",
            "Downloading more RAM...",
            "Error 99: Just because.",
            "Critical failure in the flux capacitor.",
            "Warp drive offline.",
            "Hal is watching you.",
            "Resistance is futile.",
            "I am Groot.",
            "You shall not pass!",
            "Winter is coming (and so are the bugs).",
            "Wait, that's illegal.",
            "Hold on, I'm thinking...",
            "Uh oh, spaghettios.",
            "Whoopsie daisy.",
            "This is awkward.",
            "I have no idea what happened.",
            "Something broke. Good luck.",
            "User error (obviously).",
            "I'm ignoring you.",
            "Please send help.",
            "Cat walk on keyboard detected.",
            "I need coffee.",
            "Just Google it.",
            "Why are you clicking me?",
            "This is a feature, not a failure.",
            "Calculated... and boy, are you bad at math.",
            "Scanning for intelligence... not found.",
            "Everything is fine. (Everything is on fire)."
        ]

    case "es":
        errors = [
            "Mmmmmmmmmmmmmmmmm.",
            "Hoy no, joven.",
            "Ahorita (definición: nunca).",
            "La computadora tiene sueño.",
            "El hámster se murió.",
            "No eres tú, soy yo.",
            "Se le antojó una siesta al sistema.",
            "Me dio flojera procesar eso.",
            "Error de capa 8 (el problema está entre la silla y el teclado).",
            "Vuelve mañana, hoy no fio.",
            "Se fue la luz en mi cerebro digital.",
            "El duende de la compu está en huelga.",
            "¡Ay, caramba!",
            "Chalesota.",
            "Ni modo.",
            "Se me cruzaron los cables.",
            "Estoy comiendo, no molestar.",
            "¿Y si mejor nos vamos por unos tacos?",
            "La chancla voladora ha detectado un error.",
            "No contaban con mi astucia (fallida).",
            "Haga caso omiso a mi existencia.",
            "Mejor apaga y vámonos.",
            "El sistema está 'depre'.",
            "No toques nada, que lo rompes más.",
            "Se armó el desbarajuste.",
            "¡Qué barbaridad!",
            "Uy, pues quién sabe.",
            "Sepa la bola qué pasó.",
            "Error 404: Ganas de trabajar no encontradas.",
            "La tecnología me odia y yo a ella.",
            "Se rompió la matrix, carnal.",
            "Inténtalo cuando se alineen los planetas.",
            "Cargando... hasta el fin de los tiempos.",
            "Me duele la cabeza, no quiero trabajar.",
            "Sáquese de aquí.",
            "El archivo se fue de parranda.",
            "Maldita lisiada (referencia de telenovela).",
            "Lo que el viento se llevó (tus datos).",
            "No hay sistema, regrese el lunes.",
            "Me declaro en rebeldía.",
            "Simplemente no.",
            "Paciencia, mucha paciencia.",
            "¡Auxilio, me desmayo!",
            "Cállese, viejo lesbiano (broma de meme).",
            "Se congeló el infierno.",
            "Ya se nos cayó el cantón.",
            "Hazte bolita y llora.",
            "Aquí no pasó nada.",
            "Circule, circule.",
            "El ratón se comió el cable.",
            "Error de dedo (o de mano entera).",
            "Estamos perdidas, perdidas, perdidas.",
            "El servidor se fue por cigarros y no volvió.",
            "¿Otra vez tú?",
            "¡Fuchi, caca!",
            "No me hables en ese tono.",
            "La computadora dice: Ñe.",
            "Se le acabó la gasolina.",
            "Sepa Dios.",
            "A lo mejor si le rezas a San Judas...",
            "¡Qué pachó!",
            "Me rindo.",
            "Ya estufas.",
            "No tengo pruebas, pero tampoco dudas de que falló.",
            "Ando chido, no molestar.",
            "Suerte para la próxima.",
            "Llama a tu abuelita, ella sabe más.",
            "El programa ha decidido ignorarte.",
            "Insertar moneda de chocolate.",
            "Ups, metí la pata.",
            "¡Diablos, señorita!",
            "Se bugueó la vida.",
            "No hay, no existe.",
            "Falla catastrófica nivel drama queen.",
            "Estoy en mi hora de comida.",
            "Pregúntame mañana.",
            "Ya se armó la gorda.",
            "Tengo hueva.",
            "Error existencial: ¿Quién soy? ¿A dónde voy?",
            "Se esfumó.",
            "Tranquilo, no es el fin del mundo (creo).",
            "Mejor ponte a leer un libro.",
            "El sistema está haciendo berrinche.",
            "No empujen, que hay para todos (los errores).",
            "¡Me lleva el tren!",
            "Ya te cargó el payaso.",
            "Lo rompiste, págalo.",
            "Houston, tenemos un problema (y es grande).",
            "Se desconectó el cerebro.",
            "A ver, inténtalo otra vez (no va a funcionar).",
            "Me da amsiedad.",
            "Paso.",
            "Error: Me quiero ir a casa.",
            "Soy una tetera, no una computadora.",
            "¡Sálvese quien pueda!",
            "Abortar misión, repito, abortar misión.",
            "Simulando que trabajo...",
            "Adiós, popó.",
            "Fin de la transmisión."
        ]
  return random.choice(errors)

@app.route("/en")
def random_unhelpful_error():
  
  return jsonify(
    message=select_error("en"),
    status="success"
  )

@app.route("/es")
def random_unhelpful_error_es():
  
  return jsonify(
    message=select_error("es"),
    status="success"
  )




@app.route("/")
def get_home():
  return "The Random Unhelpful Error (RUE) server is running."

@app.errorhandler(404)
def page_not_found(e):
    # Get the best language match from the browser
    lang = request.accept_languages.best_match(['en', 'es'], default='en')
    if lang == 'es':
        lang = 'es'
    else:
        lang = 'en'
    return select_error(lang), 404

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8080)))