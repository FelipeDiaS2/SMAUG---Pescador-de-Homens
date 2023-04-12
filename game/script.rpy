init python:
    PeixesScore = 0
    


# Imagens para personagens

image PedroManha = ("images/Personagens/Pedro-MANHA.png")
image AveiaManha = ("images/Personagens/Aveia-MANHA.png")
image PedroTarde = ("images/Personagens/Pedro-TARDE.png")
image AveiaTarde = ("images/Personagens/Aveia-TARDE.png")
image PedroNoite = ("images/Personagens/Pedro-NOITE.png")
image AveiaNoite = ("images/Personagens/Aveia-NOITE.png")
# Imagens para cenário

image cena2 = ("images/Cenário/Manhã.jpg")
image manha = Movie(play="images/Cenário/Manhã.webm")
image cena5 = ("images/Cenário/Noite.jpg")
image noite = Movie(play="images/Cenário/Noite.webm")
image cena4 = ("images/Cenário/Tarde.jpg")
image tarde = Movie(play="images/Cenário/Tarde.webm")
image cena6 = Movie(play="images/Cenário/Ena1.webm")
image cena7 = Movie(play="images/Cenário/Ena2.webm")
image cena8 = Movie(play="images/Cenário/Ena3.webm")
image cena9 = Movie(play="images/Cenário/Ena4.webm")
image cena10 = ("images/Cenário/Fim.png")
image PeixeMedio = ("images/Cenário/Pirarara (Peixe Médio).jpg")
image PeixePequeno = ("images/Cenário/Truta Arco-Íris (Peixe Pequeno).jpg")
image PeixeGrande = ("images/Cenário/Jaú (Peixe Grande).jpg")

# Imagens para Efeitos 

image particulasColoridas = Fixed(SnowBlossom("images/HUD/Particulas1.png", 3, xspeed = (-65, -35), yspeed = (0, 0), start = 1)) 

# Músicas 

define audio.agua = "audio/agua.ogg"

# Definição de personagens 

define e = Character("Ena")
define i = Character("?????")
define p = Character("[player_name]")
define a = Character("Aveia")
define P = Character("Pedro")
define n = Character("")

# Imagens SplashScreen

image Logo = ("images/splash/Noodles.png")
image smaug = ("images/splash/Smaug.jpg")

label splashscreen:
    

    scene black with dissolve
    pause (2)
    scene smaug with dissolve
    pause (2)
    scene black with dissolve
    pause (2)
    scene Logo with dissolve
    pause (2)
    scene black with dissolve
    pause (1)
    return


# Capítulo 1 : "Graça"

label start:
    
    # Variables 
    $ player_name = ""

    scene black with fade

    show particulasColoridas 

    play music "audio/vento.ogg" fadein 1

    pause(2)

    i "Boas novas campeão, você acaba de receber a graça divina… Como se sente?" 
    i "O que? Você é uma campeã? Na verdade, me diga, como gostaria de ser chamado… Ou chamada?"
   
    $ player_name = renpy.input("Coloque seu nome aqui")
    $ player_name = player_name.strip()
    if player_name == "":
        $ player_name = "Desconhecido"

    stop music fadeout 1
    i "Olha que nome bonito… [player_name]. Me chamo… Ena"
    
    play music agua volume 0.1 fadein 2 
    show cena6 with fade

    p "Tá, o que que tá acontecendo?"
    e "Bom, como te disse, você recebeu a graça divina… Sabe quando a pessoa morre? Daí uma galera diz que ela vai pro céu, outra galera diz que vai pro inferno e outras dizem que você começa toda aquela ladainha de “vida” tudo de novo."
    e "Eu sei lá porque a galera gosta de inventar tanta moda, mas fazer o que, não sou eu que man… "
    p "Tá, mas me ajuda aqui, o que que tá acontecendo?"
    e "É simples, você já era… Caiu do balanço… Bateu as botas… Sério, você literalmente tava num balanço, se empurrou forte demais, bateu as botas no chão, saiu voando e caiu duro. Pelo menos não deu trabalho, foi rapidinho. "
    p "Então eu morri?"
    e "É."
    p "E não tem como voltar?"
    e "Voltar pra que?"
    p "Sei lá… O que que eu faço agora?"
    e "É simples… Como você foi presenteado com a graça divina, você não tem mais os problemas do lado de lá… E meio que a gente te escolheu pra fazer parte da nossa família! Você é muito importante, sabia?"
    p "Aham… Como?"
    e "Então, como eu tava explicando… Na nossa família, você vai ajudar a gente a fazer o nosso serviço e…"
    p "Segura. Eu morri e eu tenho que trabalhar? VOCÊ TÁ BRINCANDO NÉ!?!?"
    e "Calma aí pô, tô tentando te explicar como funciona! Fica em paz meu…"
    p "…"
    e "Mais uma vez… Você vai ajudar a gente… A criar… Um mundo melhor!"
    p "Ah pronto!? agora eu que te pergunto, COMO!?"
    e "Pois dá pra se acalmar, você já morreu, não tem mais volta! Agora é só graça…"
    p "Não to vendo graça nenhuma…"
    e " Ta na tua frente, você que não quer ver…"
    p " … Beleza, então me ajuda a entender, por favor… O que que eu tenho que fazer?"
    e "Vamo lá…"
    
    # Descompressão de dados


label Cena2:

    #fazer parada das nuvens pt.1

    scene manha with fade 
    show PedroManha with dissolve
    show AveiaManha with dissolve
    pause (0.5)

    e "Vamos lá… Você conhece este homem?"
    
    menu ConhecerHomem:
        "Sim":
            e "Sério? Vou ter que falar com a supervisão… Enfim, presta atenção. Esse é o cara que a gente escolheu pra te ensinar a como ser um deus!"
        "Não":
            e "Sério? Vou ter que falar com a supervisão… Enfim, presta atenção. Esse é o cara que a gente escolheu pra te ensinar a como ser um deus!"
    
    p "UM DEUS?!"
    e "Quase isso, tem chão ainda kkkkk. Você vai ficar responsável por conversar com ele e basicamente entender as necessidades dele para ajudar no dia a dia. Fácil né?"
    p "Parece fácil…"
    e "To te falando! Você vai pegar o jeito rapidinho, falei que você era importante… Agora tu vai aprender um pouquinho sobre ele para interagir, mas pra começar, hoje vou deixar você tranquilo, só pra conhecer ele, conversar um pouquinho e essas coisas. Pode ser?"

    menu PodeSer:
        "Sim":
            e " Show de bola! Então agora é com você, boa sorte e se precisar de alguma coisa, eu venho te socorrer. Até mais [player_name]!"
        "Não":
            e " Show de bola! Então agora é com você, boa sorte e se precisar de alguma coisa, eu venho te socorrer. Até mais [player_name]!"

    p "Que? mas, já?"
    e "É pô, achou que ia ter um tutorial ou coisa assim, que nem nos vídeo games?"
    p "..."
    e "É de boa, você foi escolhido, lembra? Você tem graça, vai se sair bem..."
    
label Cena3:

    #fazer a parada das nuvens pt.2 
    p "..."
    P "..."
    p "..."

    play sound "audio/1 Latido.ogg" volume 0.7
    a '“Late”'
    P "Qi qi foi aveia?"
    
    play sound "audio/Latido.ogg" volume 0.7
    a '“Late 4 vezes”' 
    
    P "Num sei não… Ocê sabi qui eu num so os mió com as palavra…"

    play sound "audio/Cachorro choramingando.ogg" 
    a '“Choraminga”' 
    P " PSCHIU! Nois é bixo! Esa genti é diferente…"

    play sound "audio/1 Latido.ogg" volume 0.5
    a "“Late”" 
    P "..."
    
    menu JogadorEscolhas1:
        "Mandar uma brisa leve":
            play sound "audio/Brisa leve.ogg" fadein 3 volume 1
            P " AHN? QUEM QUI TÁ AÍ?"
        "Passos atrás de Pedro":
            play sound "audio/folhas seca.ogg" volume 0.5
            P " AHN? QUEM QUI TÁ AÍ?"
        "Jogar alguma coisa na água":
            play sound "audio/splash.ogg" fadein 1
            P " AHN? QUEM QUI TÁ AÍ?"

    a "“Late algumas vezes”" 
    P "CALMA AVEIA, CALMA!!!"
    a "“Late algumas vezes”" 
    P "OCEIS TAVAM ME OVINDO É?!?! É VISAGE É?!?!"
    p " “Todo mundo tava…”"
    P "Escancara égua!!"
    
    play sound "audio/1 Latido.ogg" volume 0.5
    a '“Late”'

    P " … Eu num to abilolado, num to não…"
    a "“Late 2 vezes”"
    P "Ô! Ei! Eu to abilolado, hehehe… Óh! Vo fala com o sinhô, si é que o sinhô eziste né… Fale cumigo!"
    play sound "audio/1 Latido.ogg" volume 0.7
    a "“Late”"
    play sound "audio/Suspiro.ogg"
    P "Boca de siri batoré, to tentano ovi… " 
    play sound "audio/Cachorro choramingando.ogg" volume 0.7
    a "“Choraminga”"

    p "“… O que que eu to fazendo aqui…”"
    P "Eita pêga, qi qi eu faço…"
    p "“Tá perdido igual eu…”"
    P "Deixe di se amarrado, deixe de milonga!"
    p "“Surto de vez…”"
    P "Oh, eu mi chamo Predo. Pedro. É Pedro… I ocê?"
    play sound "audio/1 Latido.ogg" volume 0.7
    a "“Late”"
    P "Num adianta, to ficano leso…"
    p "“Leso to eu…”"
    P "Si acalme bichinho, vamo dinovo…"
    pause (0.2)
    scene black with fade
    pause (0.2)

label Cena4:

    # Mesma cena principal de Pedro de costas para o jogador, mas desta vez o céu está no fim da tarde, com o sol se pondo. Nada muda na cena além do fundo do céu.
    
    scene tarde with fade 
    show PedroTarde with dissolve
    show AveiaTarde with dissolve
    pause (0.5)

    P "Mi chamo Pedro. So pescadô aqi da região. Tenho meus fio andré, tiago e juão. Mia muie lucia ta co eles em casa, dai eu veio pesca aqi pra a genti te oq di cume."
    play sound "audio/1 Latido.ogg" volume 0.7
    a "“Late”"
    P "I tem a aveia, noso bichinho!"
    a "“Late 2 vezes”"
    P "u nei sei se tei augem ai, mai a lucia falo qi era pra eu tentá! Ta ficano cada vez pió… Os pexe num vem mais, nem manjubinha… Ai eu qiria sabê se oce tinha como ajuda a genti, só um poquio sabe?"
    pause (1)
    P "Eu nunca fui de acredita muito no senhor… mas mi contaro que o sinho sabia das coisa, que o sinho pudia ajuda a genti com os pexe, sabe é?"
    P "Então eu vim dize… Cunversa né, com o sinho memo, de cabra, pra omi… Pq o sinho tem a palavra ne? di qi seu eu fo atrás do sinho e fize as coisa do sinho, ce vai faze as coisa pra mim, é?"
    P "Então eu to aqi ó, qero conhece o sinhô…"

    menu JogadorEscolhas2:
        "Não responder nada":
            play sound "audio/vento.ogg" fadein 3 volume 1
            P "Eu num sei como é qi o sinho vai me ajuda né… Mas asim, se o sinho pude manda uns pexinho pra gente, so pra gente te o qi de cume nos proximo dia… Sabe como é aqi, logo a genti num vai te muito…" 
            P "Para o mês fica paia… Ajuda a gente como cunsegi né, eai me fala qq eu tenho q faze pro sinhô…"
        "Lançar uma brisa suave":
            play sound "audio/vento.ogg" fadein 3 volume 1 
            P "Eu num sei como é qi o sinho vai me ajuda né… Mas asim, se o sinho pude manda uns pexinho pra gente, so pra gente te o qi de cume nos proximo dia… Sabe como é aqi, logo a genti num vai te muito… "
            P "Para o mês fica paia… Ajuda a gente como cunsegi né, eai me fala qq eu tenho q faze pro sinhô…"
            stop sound fadeout 3
    
    menu JogadorEscolhas3:
        "Pouca pescaria":
            $PeixesScore += 1
        "Boa pescaria":
            $PeixesScore += 2
        "Muita pescaria":
            $PeixesScore += 3
    
    P "Ó, eu vo fica aqi, dai o sinhô me diz se vai ajuda ou não, pq eu n to abirobado, eai qando o sinhô qizé, é so falá…"
    play sound "audio/1 Latido.ogg" volume 0.7
    a "“Late”"
    P "Boca de siri, temo qe ovi o omi…"
    
    pause(0.5)
    
    P "Será q é omi aveia?"
    play sound "audio/1 Latido.ogg" volume 0.7
    a "“Late”"
    P "E si num fô?"
    p "“E faz diferença?”"
    P "ÓH, SI O SINHÔ, FÔ UMA SINHORA, NUM TEM PROBEMA NAUM, MAS AI OCE ME DIZ TÁ?!?!"
    a "“Late 2 vezes”"
    p "“O que eu faço agora?”"
    
    pause(0.5)

    P "Será qi tem q fala q nem genti da cidade com eli?"
    a "“Late 2 vezes”"
    P "Vô tenta… Óh sinhô, como eu num sei como ti chama ainda, vo te chama de sinhô, mas dai cuando a muié disse comé qi é, eu falo certinho… Se o sinhô quisé, eu vo aprende a fala direito, ai eu venho aprumado, bem direitinho…"
    a "“Late 2 vezes”"
    P "É isso é Aveia? vo prende a fala com eli…"

    pause (0.5)

    p "“E agora? Acabou?”"

    pause (0.5)

    P "Cadê a tripa de galinha pa buta no anzol…"
    play sound "audio/Som de cachorro choramingando (2).ogg" fadein 2 volume 0.5
    a "“Choraminga”" 
    P "… OCE CUMEU?!"
    play sound "audio/chinelada.ogg" fadein 0.5 volume 0.7
    P "EU JÁ FALEI PRA NUM CUME?! O FIO DA PESTE!!"
    play sound "audio/Cachorro choramingando.ogg" fadein 1 
    a "“Choraminga”"
    P "E COMO EU VO PESCA AGORA?!! SI XOTA DAQI!!"
    

    hide AveiaTarde with dissolve
    pause(2)

label Cena5:
    
    scene noite with fade
    show PedroNoite with dissolve
    P "I agora, cumé q eu vo pesca… Num sobrô ninhum engodo é… Ô diacho, tá de rosca ogi… Vai é sem memo, vo tapea com mióca… Fico até di noite…"
    stop music fadeout 3
    play music "audio/Batida de coração.ogg" fadein 4
    play sound "audio/Gota.mp3" fadein 3
    pause (1)
    #cena dele em pé pescando
    n "..." 

    if PeixesScore == 1:
        scene PeixePequeno with fade
        play sound "audio/agua e grilo.ogg" fadein 5 volume 0.3 
        P "..."
        P "..."
        stop music fadeout 1 
        play sound "audio/Gota.mp3"
        P "Num vai vi é nada… Aquela fia dum cabrunco deu fim na pescaria toda… Qero ve amaiã, se ela num vai fica chorando mai uma veis…"
        play sound "audio/Balde e tomara q nn de erro.ogg" fadein 2 volume 0.6
        P "Nois num tem o qi di cume, e ela ainda comi o que nois tem de pesca… Cachorro idiota…"
        P "Qi qi eu vo fala pa lucia… Sinhô idiota, num eziste essas coisa não… Eu vo pa casa, vo pedi ajuda po pegado…"
        P "Deu a bobônica, mi feis de leso e num sobrô nada! Dia da bexiga… ACABO! vo mi embora! Aveia se vira pa de amiã, num vo atrais de cachorro da peste…"
        stop sound fadeout 5 
        play music "audio/Mix.ogg" fadein 3.0 volume 0.4

label Cena5a:
    
    if PeixesScore == 2:
        play sound "audio/agua e grilo.ogg" fadein 2.0 volume 0.4
        P "..."
        P "..."
        play sound ("audio/splash médio.ogg")
        scene PeixeMedio with fade
        P "OOOOOOIAA SÓ…"
        stop music fadeout 2.0
        play sound "audio/Pingado.ogg" fadein 2
        P "Mai num é possíve… Pai d'égua, oia só qe pexão bonito pa nois!! Aveia, corre aqi, volta pa cá fi da peste. Da peste não, de lasca o cano!"
        play sound "audio/1 Latido.ogg"
        a "“Late”"
        P "Foi o sinhô que fez isso?!!?! É O SENHOR DE VERDADE?!!!"
        a "“Late 2 vezes”"
        P "Vamo conta pa Lúcia do peixe batoré!!"
        play sound "audio/Latido.ogg"
        a "“Late constantemente”"
        P "Mas eu nunca vi isso, sem tripa e um pexão assim? Vamo cume aveia, vamo cume!! Isso aqi dá pa uns 3 dia!! É oje qi eu si acabo de cume!!!"
        a "“Late 2 vezes”"
        P "Vamo pa casa aveia, cabo por hoje… Eita dia arretado…"
        play music "audio/Mix.ogg" fadein 1.0 volume 0.4
    else:
        if PeixesScore == 3:
            play sound "audio/agua e grilo.ogg" fadein 4.0 volume 0.4
            P "..."
            P "..."
            scene PeixeGrande with fade
            play sound "audio/splash.ogg" fadein 1 volume 0.4
            stop music fadeout 2.0

            p "UUUUUUAAAAAAAAAUUUUUUUUUU!!!"
            p "NUM CREDITO NISO NAUM!!!"
            p "OIA ESA LAPA DE PEXÃO!! AVEIA, CADE TU BATORÉ?!?!!"
            play music "audio/Mix.ogg" fadein 1.0 volume 0.4
            
    

label Cena6:

    scene cena6 with fade
    e "… Eai, como foi?"
    
    menu JogadorEscolhas4:
        "Difícil":
            e "Puxa… Geralmente a galera que vem pra cá no primeiro dia não entende nada, mas acho que você se saiu bem…"
        "Tranquilo":
            e "Puxa… Geralmente a galera que vem pra cá no primeiro dia não entende nada, mas acho que você se saiu bem…"
        "Muito bem":
            e "Puxa… Geralmente a galera que vem pra cá no primeiro dia não entende nada, mas acho que você se saiu bem…"
    
    e "Concorda?" #ROTA PRINCIPAL

    menu JogadorEscolhas5:
        "Sim":
            "Ta vendo, eu disse que não tinha com o que se preocupar…"
        "Não" :
            "Ué, acha que poderia ter feito melhor?" #ROTA SECUNDÁRIA
            menu RotaSecundaria:
                "Sim":
                    e "Eita, vou anotar aqui. Diga, o que gostaria de fazer…" #ROTA TERCIÁRIA
                    menu RotaTerciaria:
                        "Poderia ter interagido mais com o Pedro…":
                            e "Ah sim… No começo a gente faz as coisas um pouco mais devagar… Assim você pode se acostumar sem se sentir muito mal. Pode brincar um pouco e acompanhar melhor."
                            e "Já que o foco é um mundo melhor, precisa ter calma… Não é como se o mundo perfeito tivesse sido feito em sete dias…"
                        "Mudaria minha opção na hora da pescaria… Eu não sabia que ele era assim…":
                            e "É… No começo é assim mesmo… Você está conhecendo ele, e ele com certeza não é perfeito, mas você pode se esforçar para entender a realidade dele e tentar ficar em paz com ele e consigo mesmo, não é verdade?"
                            e " Vocês pensam de maneiras diferentes, então pode ser uma boa ideia ajudá-lo a pensar melhor…"
                        "ELE BATEU NO CACHORRO CARA!":
                            e "É, mas o que você pode fazer sobre isso? Você não é nenhum deus… Agora está aprendendo as coisas que nós contemplamos todos os dias, e temos que escolher se vamos agir ou não… "
                            e "Não é simples tomar essas decisões… Se você quiser, pode dar mais uma chance à ele e continuar, ou pode desistir, você faz o que quiser… "                            
                "Não":
                    e "Hm… então creio que seja questão de tempo pra você se acostumar com a rotina… Mas fica em paz que logo logo a gente ajusta para a programação normal…" #ROTA PRINCIPAL
    
    #RETORNO ROTA PRINCIPAL
    e " … Mas enfim, gostou do cara pelo menos?"

    menu JogadorEscolhas6:
        "Ele é um cara bem simples né?":
            "De fato, um senhorzinho, mas de acordo com o seu perfil, a gente achou que ele seria o mais adequado para te ensinar a trabalhar… Olhando pelo lado positivo, ele ficou empolgadão contigo!"
        "Não sei dizer, não entendi metade do que ele falou…":
            "Ce só reclama meu… Acha que todo mundo é igual você? No primeiro dia já quer mandar o cara pra longe… Você ficou responsável por ele justamente pra aprender algumas coisas, uma delas é conviver em paz com os diferentes de ti…"
        "Ele bateu no cachorro cara…":
            "E você nunca fez algo que outras pessoas julgassem monstruoso? Você recebeu a graça divina e não consegue se separar dessa “humanidade”... Está em outro mundo agora, tome a decisão de torná-lo melhor… Ele precisa de ajuda… Mas como já disse, você pode ir embora quando quiser, só tenha certeza de sua escolha…"

    e "Chega de reclamar agora! To cheio de sono…"
    p "Você sente sono?"
    e "É modo de dizer cara, não aprendeu nada com as expressões do Pedro?"
    p "..."
    e "Pois é… Então show de bola, por hoje é só isso, pode ir curtir a vida e daqui um tempo eu te chamo, ou tu volta quando quiser continuar… A gente se vê depois, tchau…"
    p "Calma aí!"
    e "O que? Quer perguntar mais alguma coisa?"
    
    menu JogadorEscolhas7:
        "Só pra esclarecer tudo. Eu vou escolher o rumo da vida dele?":
            e "É!"
        "Como faço pra entender o que ele fala?":
            e "Sei lá… Tem um monte de pessoas por aí, procura alguém que fala a “língua” dele e tenta entender, conhecer… Como eu já disse, se esforça um pouco pra entender o cara, olha o que ele ta fazendo pra tentar conversar contigo, se esforça também pra conversar com ele… "
        "Tem mais alguma coisa que você devia me contar?":
            e "Não! Quer dizer, se tinha, esqueci… Mas você é esperto, você se vira…"
    
    p "Resposta certa que não serve pra nada…"
    e "Que que foi?"
    p "Nada não, tudo certo, pode ir lá dormir ou sei lá o que você tem pra fazer…"    
    e "Sei… Fica a dica então. Pra uma melhor tomada de decisões, sugerimos que você retorne em alguns dias. Vai andar por aí, espairecer, conhecer o lugar… Tu pode simplesmente continuar, mas se esperar uns dias, pode processar melhor tudo que ta acontecendo…"
    p "Pode deixar, eu me viro… Sou inteligente né?"
    e "É!"
    p "Pois bem, até mais!"
    e "Tchau!"
    stop music fadeout 2.0
    pause (0.4)

#Capítulo 2: “Futuro”
label Cena7:

    scene black with fade
    play sound "audio/Sino.ogg" fadein 2 volume 0.4
    centered "{color=F9BB00}{i}Capítulo 1{/i}{/color}"
    pause (2)

    play music "audio/Mix.ogg" fadein 3 volume 0.4
    scene cena7 with fade
    e "Boa [player_name], você voltou… Como que foi esse tempo que ficou fora?"

    menu JogadorEscolhas8:
        "Breve":
            e "Ah, show de bola, mas podia ter aproveitado um pouco mais… Ter ido no parque, comido alguma coisa, pensado na vida, essas coisas de gente…"
        "Demorado":
            e "Oxi, mas num te falei que não existe tempo aqui? Aqui é a eternidade, não existe essa de demorar kkkkkk… Enlouqueceu mesmo kkk…"
        "Pra falar a verdade, eu meio que esqueci...":
            e "Ah pronto, agora virei um qualquer? É assim que você trata seus amigos?? Meu Pai… Assim magoa a gente, credo…"

    p "Você é bom de piada né…"
    e "É!"
    p "{size=20}{i}Foi uma pergunta retórica…{/i}{/size}"
    e "Como que é?"
    p "Nada… To de volta! E quero conversar com o Pedro de novo!"
    e "Oooolha, parece que alguém aprendeu alguma coisa desde nossa última conversa…"
    e "Me diz aí, o que quer conversar com ele?"
    
    menu JogadorEscolhas9:
        "Quero testar umas coisas diferentes, me senti perdido da última vez…":
            e "Certo, certo, então hoje vou te ajudar a pensar melhor sobre as coisas, pode ser?"
        "Quero conhecer mais ele, saber da história dele…":
            e "Aí sim, falei que você ia gostar do cara… Gente fina né?"
        "Como assim? Eu quis dizer que só voltei pra continuar de onde parei…":
            e "Beleza, então vou fingir que você sabe o que tá fazendo, ok?"
    
    p "Sim"
    e "Show de bola marreco, bora pra cima!"
    p "Que que cê tá falando?"
    e "Me inspirei no Pedro e comecei a falar com umas gírias de jovens, pra parecer mais descolado, entendeu? Quer dizer, {i}tá ligado?{/i}"
    p "Só tem doido aqui né?"
    e "É!"
    P "Eu vou buscar ajuda…"
    e "Vai nada, vem cá que vou te mostrar como vai ser o dia de hoje…"
    P "Lá vem…"
    e "Então é o seguinte: Percebemos que da última vez você quase não interagiu com o Pedro… A gente achou que você podia tá meio tímido, nervoso, acuado mas vou te dar uma ideia de como melhorar isso…"
    p "Eu meio que não tive muita esco/"
    e "Sei, sei… Escuta, faz silêncio…"
    p "O quê?"
    e "Silêncio meu!"
    p "..."
    e "..."
    p "{size=20}O que era pra gente tá ouvindo?{/size}"
    e "Você não está ouvindo não?"
    p "Não!"
    e "Ué, meu Pai tá falando com a gente!"
    p "Teu pai? Tu tem pai? Achei que t/"
    e "É claro que eu tenho Pai!! Cê também tem!"
    p "Eu sei, é só que imaginei qu/"
    e "Ele é teu pai também!"
    p "Deixa eu terminar uma fra… Quê?"
    e "É!"
    p "Quem é meu pai?"
    e "O meu Pai, é seu Pai também! É pai de todo mundo na verdade… Mas vocês do lado de lá são cheios de coisinha né…"
    p "Como assim, não to entendendo nada…"
    e "Incrível como vocês também não aprendem nada… É simples, como tudo aqui em cima… Meu Pai, é seu Pai também… Lembra que te falei sobre você ter recebido a graça divina?"
    p "Sim..."
    e "Então, foi Ele que deu pra ti!"
    p "Porquê?"
    e "Ai eu não sei, pergunta pra Ele…"
    p "Você disse que sabia!"
    e "Talvez. Mas foi importante pra você entender no começo… Se não, olha só, não teria voltado…"
    p "Eu não voltei por nada disso, voltei porque…"
    e "{i}Por que…{/i}"
    p "Não importa o porquê! Eu voltei! Só estou aqui pra ajudar o Pedro!"
    e "Ótimo, e a gente tá aqui pra te ajudar!"
    p "CHEGA!"
    e " Estressou, vixe…"
    p "..."
    e "Pode falar, eu deixo, vai..."
    p "Certo… Então como eu, que acabei de chegar, falo com esse meu novo pai?"
    e "Ué, que nem o Pedro tá tentando fazer contigo!"
    p "Mas… Quê?!"
    e "Vamos de novo… O seu Pai agora vai estar contigo… Por isso você está aprendendo a cuidar do Pedro, pra poder ajudar ele que nem teu novo Pai vai te ajudar!"
    p "Como ele vai me ajudar?"
    e "Pra começar, você que tem que ir atrás, Ele não vai te forçar a nada…"
    p "{size=20}{i}Legal, mais coisa pra fazer…{/i}{/size}"
    e "Ué, mas é você que tem querer ajuda né? Se não quiser é só continuar tua existência por aí…"
    p "..."
    e "Calma, eu não falo assim porque quero te sacanear, mas você também precisa se ajudar…"
    p "Sei..."
    e "Sabe mesmo? Que legal, então tá liberado! Pode ir lá com Pedro…"
    p "Foi iro/"
    e " Eu que sei agora, abençoado…"
    p "{size=20}{i}Ta ficando cada vez pior…{/i}{/size}"
    e "Show de bola, vou deixar você à vontade agora, a gente se vê depois…"
    p "Até…"
    e "Lembra que se precisar de ajuda, é só pedir!"
    p "Aham, vou pedir sim…"
    e "Legal, tchau…"

label Cena8:

        scene manha with fade
        show PedroManha with dissolve
        show AveiaManha with dissolve

        # som de assovio
        P "Eeeeitcha, cheguemo pra hoji… Vamo que eu num quero bater sete freguesias mais não… "
        play sound "audio/1 Latido.ogg" volume 0.7
        a "“Late uma vez”"
        P "De hoje foi quando qui eu me dei di fala sozinho da otra vez Aveia?"
        p "{size=50}{i}Sinceramente Ena, me ajuda aqui. Nem começou essa conversa de maluco eu já me perdi…{size=50}{i}"
        a "“Murmura”"
        P "Qui eu fiquei matutando distrenado de ovido…"
        a "“Late duas vez”"
        P "Cê num sabe de nada Aveia! Me ajuda com as coisa qui hoji eu vo fala com o omi…"
        play sound "audio/1 Latido.ogg" volume 0.7
        a "“Late uma vez”"
        P "Tinha ficado encafifado, mas a Lúcia dise que era omi… Se fosse muié eu ficava até aprumado pa fala cum ela hehehe…"
        a "“Murmura”"
        p "{i}Não vai dá pra seguir assim não…{i}"
        P "Venha! Se aquiete qui eu vo fala!"
        a "“Choraminga”"
        #[Som de assobio, como se estivesse chamando alguém]
        P "Óh, sinhô do céu, to di volta aqui pa fala com o sinhô! Feiz um bucado de tempo já qui eu num tava de me dize com o sinhô, mai a Lúcia me ajudo!"
        a "“Late duas vez”"
        P "Se aquieta batoré! Eu fui enxerido da ota vez, agora vo fala qui di verdade!"
        a "“Murmura”"
        P "Vem comigo que vou lhe mostra!"
        P "Óh, sinhô do céu! Eu me endireitei com os menino pra ta hoji aqui de fala com o Sinhô!"
        a "“Late uma vez”"
        P "Vô lhe conta como as criança crecero! André, tiago e juão, os treis foi pa iscola! Viu só? Num falei qui eu ia di ficar mió? É qui to aprendendo aos pouco também com os menino né, mas ligero to falando chique!"
        a "“Late duas vez”"
        P "Juão feiz sete ano! Igual a Aveira né?"
        play sound "audio/Latido.ogg" volume 0.7
        a "“Late quatro vez”"
        P "Eeeeeitcha arretado! To falando bem demais né bichinho?!!"
        a "“Late duas vez”"
        P "Sossega o facho qui vo fala sério agora!"
        a "“Choraminga”"

label Cena9:
            
            if PeixesScore == 1:
                P "..."
                play sound "audio/vento.ogg" fadein 3 volume 0.7
                P "..."
                p "{size=35}{i}Vai falar nada não?{size=35}{i}"
                P "{size=35}{i}Fala serio… Vo fala o q? Esse diacho num eziste coisa ninhuma! A Lúcia fica cabrunquenta mas ela num vem aqi pesca pra nois tê o qi di cume…{size=35}{i}"
                a "“Murmura”"
                P "Aveia!"
                play sound "audio/1 Latido.ogg" volume 0.7
                a "“Late uma vez”"
                P "Oce acha que si tivesse um brôco desse, ele ia fala com a genti??"
                a "“Murmura”"
                P "Num tem nada disso naum! De hoje pra aquele dia num veio peixe! Num ajudo em nada! Deu nem de bucha pa gente vive ate hoji…"
                a "“Choraminga”"
                P "I qui di mais?? Eu qui tenho que pesca todo dia aqi, num da paiz de fica um dia com pexe purqe temo que vim dinovo…"
                a "“Late uma vez”"
                P "É isso mesmo! Eu qui faço tudo aqi! Vai vê só si num vô volta com um pexão oji!"
                a "“Late duas vez”"
                P "Vai vendo…"
                
            if PeixesScore == 2:
                P "Óh, sinhô do céu! Obrigado! Si o sinhô num tivesse ajudado eu num ia te o qui di cume sabe?"
                P "Naquele dia nois fomo feliz… Aveia se acabo de rue os oso!!"
                a "“Late duas vezes”"
                P " E asim… Cunversando com a muié, dizeu pra tentar ouvi mió!"
                play sound "audio/1 Latido.ogg" volume 0.7
                a "“Late uma vez”"
                P "Mas si eu num to te ovindo agora…"
                play sound "audio/vento.ogg" fadein 3 volume 0.7
                P "..."
                play music agua volume 0.1 fadein 2
                P "{size=35}{i}Serase memo que eziste augem aveia?{size=35}{i}"
                a "“Murmura”"
                P "Num sei…"
                play sound "audio/1 Latido.ogg" volume 0.7
                a "“Late uma vez”"
                P "Para de latí! Ocê num me dexa em pais com as coisa…"
                a "“Murmura”"
                P "Precisamo de ajuda em…"
                p "{size=25}{i}Quem precisa de ajuda sou eu…{size=35}{i}"
                a "“Late quatro vezes”"
                P " Só um troço doido memo pra muda as coisa…"

            if PeixesScore == 3:
                P "Eita qi num tem oqi dize! Os pexe tava arretado, hein! Sobro até pra Aveia!"
                a "“Late quatro vezes”"
                P "Tava barril dimais! Nois cumemo e se acabamo!! Eeeeeita como foi bom…"
                a "“Late duas vez”"
                P "Lembra Aveia, quando eu pesquei os pexe sem isca?!!?!"
                a "“Late quatro vezes”"
                P "Mi respeite que eu sou o pescadô! Tava nois na berada do riacho, quando é fé, si levaaaaanta aqela carrada dagua!!"
                a "“Late duas vez”"
                P "EU SO BOCA DE SUBADO SEU CORNO!!"
                a "“Late quatro vezes”"
                P "QUERO QUI MI VENHA, UM PESCADÔ, MIÓ DO QI EU!!"
                a "“Late duas vez”"
                P " Eeeeeeita que foi um monte de dia comendo, chega cria um corgo na boca… Eeeeeeita…"
                P "Demo um fim das costa naqeles pexe tudo…"
                P "Pesqemo dimais…"

                             
label Cena10:
    
    scene tarde with fade
    show PedroTarde with dissolve
    show AveiaTarde with dissolve

    P "É Aveia, as coisa naum sao faciu nao…"
    a "“Late duas vezes”"
    P "Nem sei si eu divia continua a cunversa… ocê e a unica qui mi escuta…"
    play sound "audio/1 Latido.ogg" volume 0.7
    a "“Late uma vez”"
    P "Mai tambem vuce num mi entende…"
    a "“Late duas vezes”"
    P "Eita… Eu vo é fala contigo batoré! É você i eu aqi óh"
    a "“Late quatro vezes”"
    P "Repare miuda! Agora, ocê é a sinhora do céu!"
    a "“Late uma vez"
    P "É iso ai, me digue aqi Aveia, onde qi nois vai pesca oji?"
    a "“Murmura”"
    P "Oh bichinho, a genti vai pelejar por essas terra tudo. Si num é nóis, num é mai ninguém…"
    a "“Choraminga”"
    P "É…"
    p "{i}Eu juro Ena, quando eu te ver de novo a gente vai conversar sério… SÉRIO!{i}"
    P "Ainda Tiago altiô. Ta largado de ser chupeta…"
    P "Os menino vão cresce ainda… Tão virando cabra macho agora…"
    P "Si a mãe deses menino deixase eles com as costa quente, aprendia cumo qi era na minha época… Dois langanhento. TRÊS!"
    play sound "audio/1 Latido.ogg" volume 0.7
    a "“Late uma vez”"
    P "Mai inda vo ensina esses malino à pulso como qi a vida é… E você não se apurrie naum! Qi logo ocê si amarra…"
    a "“Choraminga”"
    P "Chega de leseira! Vamo pexca"
    a "“Late duas vezes”"
    p "{i}Sinceramente, esse é o doido mais varrido que eu já conheci…{i}"
    pause (0.5)

label Cena11:

    play sound "audio/1 Latido.ogg" volume 0.7 fadein 2
    P "Boita os miúdo na linha, e dale água…"
    a "“Late uma vez”"
    play sound "audio/Gota.mp3" fadein 3
    P "..."
    play sound "audio/Brisa leve.ogg" fadein 3 volume 1
    P "..."
    a "“Late quatro vezes”"
    play sound agua volume 0.1 fadein 2 
    P "É bichinho… Cumé que nois vai faze pa ajunta os pexe… Purqe eu num vo fica falando cum o vento, to ficando abirobado…"
    a "“Murmura”"
    P "..."
    a "“Choraminga”"
    P "Num sei comu qi vo faze, mas vo te q faze né?"
    a "“Late uma vez”"
    P "Inda mais que os pexe vão fica fininho logo logo… Quando as estacão pasá e as chuva chega, aí é qi num vamo pesca nada memo…"
    a "“Choraminga”"
    P "É Aveia, as coisa num tao facio naum…"
    play sound "audio/1 Latido.ogg" volume 0.7 fadein 2
    a "“Late uma vez”"    
    P "..."
    play sound "audio/grilo.ogg" volume 0.7 fadein 2
    P "Eu vo tenta falá dinovo com o omi lá, ocê num ta ajudando em nada…"
    a "“Murmura”"
    P "Mai si eu chama ele agora vai me esbregueia tudo… Comu qi vo fala se to todo errado…"
    a "“Late uma vez”"
    P "Tu ta certa né fia da muléstia, sabe nem fala a linga dos omi e ta debochado aí…"
    a "“Late duas vezes”"
    P "..."
    a "“Late quatro vezes”"
    P "{size=35}{i}Si dé di chabu, eu num falo é com mai nada...{size=35}{i}"
    #SOM DE ASSOBIO
    P "Sinhô do céu, traiz uns pexinho pra genti… To sabendo q num sô o dos melhoris omem q tem, mas cabra macho eu sô qi só! Sem tira nem farta, to de aguça tudo qi vié pra cima! Pode vim sinhô!"
    a "“Late duas vezes”"
    P "... Foi mal, fiqei ispritado… Mai sinhô, manda uns pexinho pra gente tê oq di cume nos prosimo dias... Eu vo aprende a fala qi nem a lingua dos omi... To quase bicho aqi, maiz os menino vai ensina eu pra di como dize as coisa… Os menino e a muié haha..."
    a "“Late uma vez”"
    P "E a Aveia tambem vai dize as coisa qi eu num sei como qi fala!"
    a "“Late quatro vezes”"
    P "Se aprochegue batoré, temo qi leva um pexe pra cume…"
    a "“Late duas vezes”"
    P "Xiu!"
    $ PeixesScore = 0

    menu JogadorEscolhas10:
        "Pouca pescaria":
            $PeixesScore += 1
        "Boa pescaria":
            $PeixesScore += 2
        "Muita pescaria":
            $PeixesScore += 3
    
    P "..."
    P "Ta sentino auguma coisa Aveia?"
    a "“Murmura”"
    pause (1)

label cena12:

    scene noite with fade
    show PedroNoite with dissolve
    show AveiaNoite with dissolve

    P "... A Lúcia é abirobada das ideia… Fico aporrinhando pra vim falar sozinho qi nem si tivesse auguem pra falá, e oia só..."
    play sound "audio/1 Latido.ogg" volume 0.7 
    a "“Late uma vez”"
    P "Ce lembra Aveia, cuando nois encontramo ocê? Ce era miuda dimais…"
    a "“Murmura”"
    P "Naqueles tempo tava cum a Lúcia ja… Mas o muié fia da peste…"
    a "“Murmura”"
    P " Era eu dize q ia fazer, a ela amola minha oreia qi eu num ia… Há, muié nunca mando em mim!"
    play sound "audio/1 Latido.ogg" volume 0.7 
    a "“Late uma vez”"
    P "Num é de hoge q eu so gato de hoteu, mai naqueles tempo… Eeeeeita…"
    a "“Murmura”"
    P "Era a Lúcia imcasa e eu n forrobodó hahaha..."
    a "“Late duas vezes”"
    P "Ficava tudo entrouxado com as muié do forró, indai pra cuando chega en caza ta ela isperando com as taboca pa se atraca ni mim!"
    play sound "audio/1 Latido.ogg" volume 0.7 
    a "“Late uma vez”"
    P "To te falano Aveia, ela era tabaroa, num prestava em nada… Inda tentava faze eu se lenhar…"
    a "“Late duas vezes”"
    P "Inda tinha cada zuruó qi dexava as muié comigo… Eeeeeeita que vida massa..."
    a "“Murmura”"
    P " E eu era escroto ein? Num sobrava pra ninhum cabra qi vinha tira as quenga di mim…"
    a "“Late quatro vezes”"
    P "É..."
    p "É inacreditável um negócio desses…"
    P "Mai como tudo qi é bom, os oto tora, mi veio um cabueta conta foi tudo pra Lúcia..."
    a "“Murmura”"
    P "Ai vim de deforete… Naquele memo dia nois te encontremo…"
    a "“Late quatro vezes”"
    p " Sem comentários…"
    P "Ai trousemo oce pa faze da Lúcia sossega o facho e de hoje, tamo ai…"
    a "“Late duas vezes”"

label Cena13:
    P " É... Mas vo me aquieta q os pexe preciza vim pa nois inda hoge..."
    a "“Late duas vezes”"

    if PeixesScore == 1:

        play sound "audio/grilo.ogg" volume 0.7 fadein 2
        P "..."
        play sound agua volume 0.1 fadein 2 
        P "..."
        scene PeixePequeno with fade
        play sound "audio/Gota.mp3" 
        P " MISÉRIA!"
        a "“Late quatro vezes”"
        P "Num posso acreditá numa fuleragem desa…"
        play sound "audio/1 Latido.ogg" volume 0.7
        a "“Late uma vez”"
        #som de pessoa chorando
        P "Eu precizo leva pelo meno um pexinho pra caza… Comu qi as criança vao cume… A Lúcia também…"
        a "“Murmura”"
        P "Vamo Aveia… Eu num qero mais ta aqi…"
        a "“Choraminga”"
        P "É dificiu demais… So queria pude come com mia família e o bichinho…"
        a "“Choraminga”"
        P "A gente precisa da um jeito nizo Aveia… Comu qi eu vo faze?"
        a "“Choraminga”"
        P "Si aqeta fi dum cabrunco!! Ja dize q vo da um jeito..."
        a "“Murmura”"
        P "...Pra quei q eu vo pedi ajuda..."
        play sound "audio/1 Latido.ogg" volume 0.7
        a "“Late uma vez”"
        P "Aveia!"
        a "“Late duas vezes”"
        P "Vamo pa cidade! la nois vai te pexe!"
        play sound "audio/1 Latido.ogg" volume 0.7
        a "“Late uma vez”"
        P "Mai eu num dinhero bichinho, ai oce vai te q pega pra genti"
        a "“Choraminga”"
        P "Num é errado naum, eu to com fome! Tamo todo mundo cum fome! Você vai pega sim, e num late alto naum pq a genti vai se fugi pelos mato… Se corre, ja ta di noite..."
        pause (0.5)

    elif PeixesScore == 2:
            
        play sound "audio/agua e grilo.ogg" fadein 2.0 volume 0.4
        P "..."
        P "..."
        stop sound fadeout 2.0
        scene PeixeMedio with fade
        P "RECEEEEBA..."
        play sound "audio/Pingado.ogg" fadein 1
        P "Oia que pexe lindo!! Aveia oia!"
        a "“Late quatro vezes”"
        P "Nois vamo te o qi di cume por uns dia ainda!"
        a "“Late duas vezes”"
        P "Será que foi o sinhô do céu?? ELE QUE MANDO EZE PEXIO PRA GENTI?"
        a "“Late quatro vezes”"
        P "IIIIIIIHÁ!! É OOOOGE Q NOIS SE ACABA DE CUME!"
        a "“Late duas vezes”"
        P "Simbora Batoré, as criança taum esperando cum fome!"
        a "“Late uma vez”"
        P " Oia, si num fose noiz…"
        pause (0.5)

    elif PeixesScore == 3:
    

        play sound "audio/agua e grilo.ogg" fadein 2.0 volume 0.4
        P "..."
        P "..."
        scene PeixeGrande with fade
        play sound "audio/splash.ogg" fadein 2
        P "OOOOOIA ESSE PEXE BICHINHO!!!"
        a "“Late quatro vezes”"
        P "É PEXE PRA DE HOJE ATÉ OITO!! VAMO CUME QI NEI AS RAINHA"
        a "“Late duas vezes”"
        P "ME AJUDA AQI QI TA PESAAAADO!!"
        a "“Rosna”"
        P "MAS ESE TAU DE SINHÔ DO CÉU É BOM DIMAAAAIS!!"
        a "Rosna”"
        P "PESQUEMO TUDO DU BOM E DO MIÓ!!!"
        a "“Late duas vezes”"
        P "CORRE AVEIA, VAMO PA CASA ASBAIGAÇA O PEXE!!"
        a "“Late quatro vezes”"
        P "IIIIIIIHÁ!!! OH GROIA!"
        a "“Late duas vezes”"
        pause (0.5)

label cena14:

    scene cena8 with fade
    

    p "Ena…"
    p "Ena, pode vir aqui? Eu não sei mais se quero continuar isso…"
    e "Porque? Você parecia tão empolgado antes... O que te fez mudar de ideia?"

    menu JogadorEscolhas11:
        "Ele traiu a esposa dele!?!? Não parece um motivo bem razoável?!!?":
            e "Veja bem... Estes dilemas morais, que vocês humanos enfrentam no dia a dia, diz respeito à somente o que vocês tem como cultura..."
        "Porque ele é assim? Quero dizer... Porque eu to ajudando ESSE cara?":
            e "Veja bem... Estes dilemas morais, que vocês humanos enfrentam no dia a dia, diz respeito à somente o que vocês tem como cultura..."
        "Esse cara é um completo canalha... Eu não sei mais como prosseguir...":
            e "Veja bem... Estes dilemas morais, que vocês humanos enfrentam no dia a dia, diz respeito à somente o que vocês tem como cultura..."
    
    p "Ena! Já não basta eu não entender uma palavra do que aquele monstro diz, e vem você agora me fazer esse joguinho?"
    e "Não era pra isso que você tinha voltado, pra jogar um pouco mais?"
    p "Não cara! Na verdade não importa mais o porquê eu voltei… Só importa que esse cara é maluco de pedra, canalha, sujo, baixo, filh…"
    e "Calma ai bicho! Você realmente não ta olhando pro Pedro em nada né?"
    p "Do que que você tá falando?!!!"
    e "To te falando que, olha o lugar em que o Pedro está, onde ele cresceu, como é sua vida, suas ideias, pensamentos, comportamentos e tudo mais… Você tá ignorando tudo isso…"
    p "Óbvio! Esse cara não merece nada!"
    e "Ooooopa, aí você machuca a gente..."
    p "Até parece..."
    e "Olha, você recebeu a graça divina justamente para experimentar e entender como as pessoas vivem, e assim poder ajudá-las a melhorar..."
    e "Não quer dizer que você precise concordar com todas as ações de cada pessoa, mas com certeza considerar o porquê de ela ter tomado tais decisões..."
    p "Eu sei que a sua intenção é a das melhores Ena… Mas esse cara é tudo de ruim!"
    e " Deixa disso... Olha com mais cuidado pra ele… Ele ainda vai te surpreender!"
    p "Eu espero que não, porque todas as surpresas que eu tive foram péssimas!"
    e "..."
    p "Não vai falar nada!?"
    e "Já acabou?"
    p "Você também é um palhaço, fica todo todo aí como se não tivesse nada pra fazer..."
    p "Eu pedi tua ajuda lá no meio e você apareceu? Fez alguma coisa?? Ajudou em algo???"
    p "NÃO! VOCÊ NÃO FEZ NADA!"
    e "...Eu queria que você tentasse trabalhar por si só, aprendesse com o Pedro e como as coisas funcionam pra ele... Mas parece que você só liga pra si mesmo..."
    p "EU QUE VIREI O VILÃO DA HISTÓRIA AGORA??!"
    e "Não! É só que, tudo isso é sobre como você pode ajudar os outros, e eu não vejo como toda essa discussão vai ajudar alguém..."
    p "AH PARA NÉ! Eu vo embora!"
    e "Bye bye bebê, quando sentir saudades me liga..."
    p "..."
    e "Vai sair não?"
    p "Como que eu saio daqui?"
    e "Ué, quer ajuda agora?"
    p "..."
    e "As vezes, a gente não pede ajuda, justamente porque a gente nem sabe onde a gente tá!"
    e "Nós pedimos ajuda quando conseguimos identificar o problema... Se não tem problema, não tem porque pedir ajuda..."
    p "Como que eu faço pra ir embora?"
    e "O Pedro ta no mesmo lugar que você, fazendo tudo errado e nem sabendo o porquê..."
    p "..."
    e "Por isso nós somos necessários na vida dele e de quem mais precisar de ajuda, mas claro, isso somente acontece se você quiser..."
    e "Como eu sempre te disse, você tem o livre arbítrio pra decidir fazer o que quiser, então eu recomendo que, por hora, descanse..."
    p "Eu faço o que eu quero!"
    e "Verdade, mas se agir assim, não pode reclamar daquilo que Pedro faz quando quer... Os dois são iguais, só que cada um de jeito..."
    p "...Sinceramente, eu devo ter me perdido no personagem..."
    e "Consigo crer nessa possibilidade, você ficou envolvido demais com essa situação toda, acho que seria melhor você descansar um pouco, espairecer, quem sabe voltar depois?"
    p "Tanto faz cara... Eu não vou voltar mais aqui"
    e "Seja feita vossa vontade… Saiba que assim que retornar, estaremos aqui para acolhê-lo"
    p "É.. To sabendo..."

    scene cena9 with fade 
    pause (0.5)

    e "Até..."
    
    pause (2)
    scene black with dissolve
    pause (2)
    scene cena10 with dissolve
    pause (2)
    scene black with dissolve
    pause (2)
  














    


















    
    
    
    
    
    
    


    
    

    
