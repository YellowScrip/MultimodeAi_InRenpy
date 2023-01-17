default vida = 100
default enemigo = 100
default masculinidad = 100

screen pelea():

    vbox:
        xalign .8
        yalign .05
        text _("Vida")
        text _("[vida]") outlines [(2, "#000000")]

    vbox:
        xalign .85
        yalign .05
        text _("Enemigo")
        text _("[enemigo]") outlines [(2, "#000000")]

    vbox:
        xalign .9
        yalign .05
        text _("Masculinidad")
        text _("[masculinidad]") outlines [(2, "#000000")]

label pelea:

    show screen pelea

    vj "Bienvenido a \"Pelea de toros\"! Demuestrale a tu oponente quien tiene los cuernos mas grandes!"

label ataque:

    $ defensa = renpy.random.choice(['ptbaja', 'ptalta', 'pbajo', 'palto'])

    if vida <= 0:

        jump peleaperdida

    elif enemigo <= 0:

        jump peleaganada

    else:

        if defensa == "ptbaja":

            vj "Tu oponente baja la guardia!"

        elif defensa == "ptalta":

            vj "Tu oponente levanta la guardia y mira a tus pies!"

        elif defensa == "pbajo":

            vj "Tu oponente baja la guardia y mira a tus brazos!"

        else:

            vj "Tu oponente levanta la guardia!"

        menu:

            vj "Ataca a tu oponente!"

            "Patada baja":

                if defensa == "ptbaja":

                    vj "Tu oponente esquiva tu golpe por completo!"

                    jump defensa

                elif defensa == "pbajo":

                    $ enemigo -= 10

                    vj "Tu oponente bloquea tu golpe! Aunque eso debio doler."

                    jump defensa

                else:

                    $ enemigo -= 25

                    vj "Tu oponente casi se cae al piso! Su novia te mira impresionada ;)."

                    jump defensa

            "Patada alta":

                if defensa == "ptalta":

                    vj "Tu oponente esquiva tu golpe por completo!"

                    jump defensa

                elif defensa == "palto":

                    $ enemigo -= 10

                    vj "Tu oponente bloquea tu golpe! Aunque eso debio doler."

                    jump defensa

                else:

                    $ enemigo -= 25

                    vj "Casi le arrancas la cabeza a tu oponente! Tu novia aplaude detras tuyo."

                    jump defensa

            "Puño bajo":

                if defensa == "pbajo":

                    vj "Tu oponente esquiva tu golpe por completo!"

                    jump defensa

                elif defensa == "ptbaja":

                    $ enemigo -= 10

                    vj "Tu oponente bloquea tu golpe! Aunque eso debio doler."

                    jump defensa

                else:

                    $ enemigo -= 25

                    vj "Le hundes el pecho a tu oponente! Su novia agarra el suyo pero te mira a ti ;)."

                    jump defensa

            "Puño alto":

                if defensa == "palto":

                    vj "Tu oponente esquiva tu golpe por completo!"

                    jump defensa

                elif defensa == "ptalta":

                    $ enemigo -= 10

                    vj "Tu oponente bloquea tu golpe! Aunque eso debio doler."

                    jump defensa

                else:

                    $ enemigo -= 25

                    vj "Cuidado con los cuernos! Casi noqueas a tu oponente."

                    jump defensa

label defensa:

    $ ataque = renpy.random.choice(['ptbaja', 'ptalta', 'pbajo', 'palto'])

    if vida <= 0:

        jump peleaperdida

    elif enemigo <= 0:

        jump peleaganada

    else:

        if ataque == "ptbaja":

            vj "Tu oponente retrocede y mira tu abdomen!"

        elif ataque == "ptalta":

            vj "Tu oponente retrocede y mira tu cabeza!"

        elif ataque == "pbajo":

            vj "Tu oponente casi no se mueve!"

        else:

            vj "Tu oponente se inclina un poco hacia atras!"

        menu:

            vj "Defiendete de tu oponente!"

            "Patada baja":

                if ataque == "ptbaja":

                    vj "Esquivas el golpe de tu oponente por completo!"

                    jump ataque

                elif ataque == "pbajo":

                    $ vida -= 10

                    vj "Bloqueas el golpe de tu oponente! Aunque eso debio doler."

                    jump ataque

                else:

                    $ vida -= 25

                    vj "Tu oponente casi te tira al piso! Tu novia suspira enamorada?"

                    jump ataque

            "Patada alta":

                if ataque == "ptalta":

                    vj "Esquivas el golpe de tu oponente por completo!"

                    jump ataque

                elif ataque == "palto":

                    $ vida -= 10

                    vj "Bloqueas el golpe de tu oponente! Aunque eso debio doler."

                    jump ataque

                else:

                    $ vida -= 25

                    vj "Tu oponente casi te arranca la cabeza! Su novia aplaude fuerte."

                    jump ataque

            "Puño bajo":

                if ataque == "pbajo":

                    vj "Esquivas el golpe de tu oponente por completo!"

                    jump ataque

                elif ataque == "ptbaja":

                    $ vida -= 10

                    vj "Bloqueas el golpe de tu oponente! Aunque eso debio doler."

                    jump ataque

                else:

                    $ vida -= 25

                    vj "Tu oponente te hunde el pecho! Sos un pobre tipo!"

                    jump ataque

            "Puño alto":

                if ataque == "palto":

                    vj "Esquivas el golpe de tu oponente por completo!"

                    jump ataque

                elif ataque == "ptalta":

                    $ vida -= 10

                    vj "Bloqueas el golpe de tu oponente! Aunque eso debio doler."

                    jump ataque

                else:

                    $ vida -= 25

                    vj "Tu oponente casi te saca los cuernos! Tu novia aplaude?"

                    jump ataque

label peleaperdida:

    $ masculinidad -= 25

    vj "Ahora sabes quien tiene los cuernos mas grandes! Abre paso al hombre de verdad!"

    hide screen pelea

    jump peleafinal

label peleaganada:

    $ masculinidad += 25

    vj "Esos cuernos no se ponen solos! Abran paso al hombre de verdad!"

    hide screen pelea

    jump peleafinal

label peleafinal:

    pp "Suficiente por hoy."
