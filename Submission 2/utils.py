import requests
from bs4 import BeautifulSoup

# idPessoa, Nome, DataNascimento, CodigoPostal, Morada
tablePessoa = [
        #Utilizadors -> Dar nomes significativos
        [1, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [2, "'Samuel'",             "'Junho'",    "'4860'", "'Rua Doutor Franscico Botelho'"],
        [3, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [4, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [5, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [6, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [7, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [8, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [9, "'Hugo'",               "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [10, "'Hugo'",              "'Julho'",   "'4490'", "'Praca dos Combatentes'"],
        [11, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [12, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [13, "'Pedro Castro'",      "'Maio'",     "'4860'", "'Chacim'"],
        [14, "'Bernardo Vaz'",      "'Maio'" ,    "'4860'", "'Rua de Outeirinho'"],
        [15, "'Marta Sofia'",       "'Novembro'", "'3020'", "'Avenida Sá da Bandeira'"],
        [16, "'Ines Machado'",      "'Janeiro'",  "'3020'", "'Rua das Azeiteiras'"],
        [17, "'Olena Shelvytska'",  "'Marco'",    "'79007'","'Lviv Snow Stree'"],
        [18, "'Beatriz Mendes'",    "'Junho'",    "'4850'", "'Centro da Maia'"],
        [19, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [20, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [21, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [22, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [23, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [24, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [25, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [26, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [27, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [28, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [29, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],
        [30, "'Hugo'",              "'Julho'",    "'4490'", "'Praca dos Combatentes'"],        
        
        # Artistas -> Colocar a data de nascimento, codigo postal e rua
        #   NIRVANA
        [31, "'Kurt Cobain'",                       "'Junho'",    "NULL",   "NULL"],
        [32, "'Krist Novoselic'",                   "'Junho'",    "NULL",   "NULL"],
        [33, "'Dace Grohl'",                        "'Junho'",    "NULL",   "NULL"],
        # FOO FIGHTERS
        [34,"'Nate Mendel'",                        "'Junho'",    "NULL",   "NULL"],
        [35,"'Taylor Hawkins'",                     "'Junho'",    "NULL",   "NULL"],
        # RADIOHEAD
        [36, "'Thomas Yorke'",                      "'Junho'",    "NULL",   "NULL"],
        [37, "'Johnny Greenwood'",                  "'Junho'",    "NULL",   "NULL"],
        [38, "'Colin Greenwood'",                   "'Junho'",    "NULL",   "NULL"],
        [39, "'Ed Obrien'",                         "'Junho'",    "NULL",   "NULL"],
        [40, "'Philip Selway'",                     "'Junho'",    "NULL",   "NULL"],
        # BILLIE EILISH
        [41, "'Billie Eilish'",                     "'Junho'",    "NULL",   "NULL"],
        #Paramore
        [42,"'Hayley Williams'",                    "'Junho'",    "NULL",   "NULL"],
        [43,"'Taylor York'",                        "'Junho'",    "NULL",   "NULL"],
        [44,"'Zac Farro'",                          "'Junho'",    "NULL",   "NULL"],
        # Lana del Rey
        [45,"'Elizabeth Grant'",                    "'Junho'",    "NULL",   "NULL"],
        #Daughter
        [46, "'Elena Tonra'",                       "'Junho'",    "NULL",   "NULL"],
        [47, "'Igor Haefeli'",                      "'Junho'",    "NULL",   "NULL"],
        [48, "'Remi Aguilella'",                    "'Junho'",    "NULL",   "NULL"],
        # Lorde
        [49, "'Ella Yelich-OConnor'",               "'Junho'",    "NULL", "'Epsom Auckland'"],
        # Eminem
        [50, "'Marshall Bruce Mathers'",            "'Junho'",    "NULL",   "NULL"],
        ]

# idPessoa, anoInicio carreira de cada artista
tableArtista = [
        [31 , "NULL"],
        [32 , "NULL"],
        [33 , "NULL"],
        [34 , "NULL"],
        [35 , "NULL"],
        [36, "'1985'"],
        [37, "'1985'"],
        [38, "'1985'"],
        [39, "'1985'"],
        [40, "'1985'"],
        [41, "'2015'"],
        [42, "'2003'"],
        [43, "'2001'"],
        [44, "'2004'"],
        [45, "'0000'"],
        [46, "'0000'"],
        [47, "'0000'"],
        [48, "'0000'"],
        [49, "'0000'"],
        [50, "'0000'"],
        ]

#idPessoa, email, username, password -> NOMES SIGNIFICATIVOS!
tableUtilizador = [
        [1,  "'hugomguima@gmail.com'",  "'Huguima'",    "'password1'"],
        [2,  "'samue@hotmail.com'",     "'Samuh'",      "'password2'"],
        [3,  "'pjbom.best@gmail.com'",  "'pjbom'",      "'password3'"],
        [4,  "'hugomguima@gmail.com'",  "'Huguima'",    "'password1'"],
        [5,  "'teste1@hotmail.com'",    "'teste1'",     "'password2'"],
        [6,  "'teste2@hotmail.com'",    "'teste2'",     "'password3'"],
        [7,  "'teste3@hotmail.com'",    "'teste3'",     "'password3'"],
        [8,  "'teste4@hotmail.com'",    "'teste4'",     "'password3'"],
        [9,  "'ziniii@outlook.com'",    "'ZiniWhini'",  "'egirl1234'"],
        [10,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [11,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [12,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [13,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [14,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [15,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [16,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [17,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [18,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [19,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [20,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [21,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [22,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [23,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [24,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [25,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [26,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [27,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [28,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [29,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        [30,  "'teste5@outlook.com'",    "'teste5'",  "'123456789'"],
        ]

#idPapel, Nome
tablePapel = [
        [1, "'Vocal'"],
        [2, "'Guitarra'"],
        [3, "'Piano'"],
        [4, "'Bateria'"],
        [5, "'Baixo'"],
        [6, "'Viola'"]]

# idEntidadeMusical, nome, imagem, ano fundacao, descricao
tableEntidadeMusical = [
        [1, "'Nirvana'",        "'imagem'", "1987",     "'descricao'"],
        [2, "'Foo Fighters'",   "'imagem'", "1994",     "'descricao'"],
        [3, "'Radiohead'",      "'imagem'", "1985",     "'descricao'"],
        [4, "'Billie Eilish'",  "'imagem'", "2016",     "'descricao'"],
        [5, "'Paramore'",       "'imagem'", "2004",     "'WE ARE PARAMORE!'"],
        [6, "'Lana Del Rey'",   "'imagem'", "2005",     "'descricao'"],
        [7, "'Daughter'",          "'imagem'", "2009",  "'descricao'"],
        [8, "'Lorde'",         "'imagem'", "1988",      "'descricao'"],
        [9, "'Eminem'",         "'imagem'", "1988",     "'descricao'"],

        ]

# id album, nome, capa, ano -> COLOCAR ANO E CAPA
tableAlbum = [
        [1, "'Nevermind'", "'capa'", "'YEAR'"],
        [2, "'In Utero'", "'capa'", "'YEAR'"],
        [3, "'Concrete and Gold - '", "'capa'", "'YEAR'"],
        [4, "'OK Computer'",                                "'https://i.imgur.com/7Prc1JI.jpg'", "'1997'"],
        [5, "'When We All Fall Asleep, Where Do We Go?'",   "'https://i.imgur.com/181OJ2a.png'", "'2019'"],
        [6, "'Brand New Eyes'",                             "'https://i.imgur.com/2zUv7QL.jpg'", "'2009'"],
        [7, "'All We Know Is Falling'",                     "'https://i.imgur.com/Gh2Y21E.jpg'", "'2005'"],
        [8, "'Born to Die'", "'capa'", "'YEAR'"],
        [9, "'If You Leav'", "'capa'", "'2013'"],
        [10, "'Melodrama'", "'capa'", "'YEAR'"],
        [11, "'The Eminem Show'", "'capa'", "'YEAR'"]
        
        ]

#idmusica, idalbum, nomeal -> COLOCAR DURACAO
tableMusica = [
        [1, 1, "'Smells Like Teen Spirit'", "'DURACAO'"],
        [2, 1, "'In Bloom'", "'DURACAO'"],
        [3, 1, "'Come As You Are'", "'DURACAO'"],
        [4, 1, "'Breed'", "'DURACAO'"],
        [5, 1, "'Lithium'", "'DURACAO'"],
        [6, 1, "'Polly'", "'DURACAO'"],
        [7, 1, "'Territorial Pissings'", "'DURACAO'"],
        [8, 1, "'Drain You'", "'DURACAO'"],
        [9, 1, "'Lounge Act'", "'DURACAO'"],
        [10, 1, "'Stay Away'", "'DURACAO'"],
        [11, 1, "'On A Plain'", "'DURACAO'"],
        [12, 1, "'Something In The Way'", "'DURACAO'"],
        [13, 2, "'Serve The Servants'", "'DURACAO'"],
        [14, 2, "'Scentless Apprentice'", "'DURACAO'"],
        [15, 2, "'Heart-shaped Box'", "'DURACAO'"],
        [16, 2, "'Rape Me'", "'DURACAO'"],
        [17, 2, "'Frances Farmer Will Have Her Revenge On Seattle'", "'DURACAO'"],
        [18, 2, "'Dumb'", "'DURACAO'"],
        [19, 2, "'Very Ape'", "'DURACAO'"],
        [20, 2, "'Milk It'", "'DURACAO'"],
        [21, 2, "'Pennyroyal Tea'", "'DURACAO'"],
        [22, 2, "'Radio Friendly Unit Shifter'", "'DURACAO'"],
        [23, 2, "'Tourette`s'", "'DURACAO'"],
        [24, 2, "'All Apologies'", "'DURACAO'"],
        [25, 2, "'Gallons Of Rubbing Alcohol Flow Through The Strip'", "'DURACAO'"],
        [26, 3, "'T-Shirt'", "'DURACAO'"],
        [27, 3, "'Run'", "'DURACAO'"],
        [28, 3, "'Make It Right'", "'DURACAO'"],
        [29, 3, "'The Sky Is a Neighborhood'", "'DURACAO'"],
        [30, 3, "'Concrete and Gold'", "'DURACAO'"],
        [31, 4, "'Karma Police'", "'DURACAO'"],
        [32, 4, "'Fitter, Happier'", "'DURACAO'"],
        [33, 4, "'Electioneering'", "'DURACAO'"],
        [34, 4, "'Climbing Up The Walls'", "'DURACAO'"],
        [35, 4, "'No Surprises'", "'DURACAO'"],
        [36, 4, "'Lucky'", "'DURACAO'"],
        [37, 4, "'The Tourist'", "'DURACAO'"],
        [38, 5, "'Bad Guy'", "'DURACAO'"],
        [39, 5, "'Xanny'", "'DURACAO'"],
        [40, 5, "'You Should See Me In a Crown'", "'DURACAO'"],
        [41, 5, "'All The Good Girls Go To Hell'", "'DURACAO'"],
        [42, 5, "'My Strange Addiction'", "'DURACAO'"],
        [43, 5, "'Bury a Friend'", "'DURACAO'"],
        [44, 5, "'Ilomilo'", "'DURACAO'"],
        [45, 5, "'Listen Before I Go'", "'DURACAO'"],
        [46, 5, "'I Love You'", "'DURACAO'"],
        [47, 5, "'Goodbye'", "'DURACAO'"],
        [48, 6, "'Careful'", "'DURACAO'"],
        [49, 6, "'Ignorance'", "'DURACAO'"],
        [50, 6, "'Playing God'", "'DURACAO'"],
        [51, 6, "'Brick By Boring Brick'", "'DURACAO'"],
        [52, 6, "'Turn It Off'", "'DURACAO'"],
        [53, 6, "'The Only Exception'", "'DURACAO'"],
        [54, 6, "'Feeling Sorry'", "'DURACAO'"],
        [55, 6, "'Looking Up'", "'DURACAO'"],
        [56, 6, "'Where The Lines Overlap'", "'DURACAO'"],
        [57, 6, "'Misguided Ghosts'", "'DURACAO'"],
        [58, 6, "'All I Wanted'", "'DURACAO'"],
        [59, 7, "'All We Know'", "'DURACAO'"],
        [60, 7, "'Pressure'", "'DURACAO'"],
        [61, 7, "'Emergency'", "'DURACAO'"],
        [62, 7, "'Brighter'", "'DURACAO'"],
        [63, 7, "'Here We Go Again'", "'DURACAO'"],
        [64, 7, "'Never Let This Go'", "'DURACAO'"],
        [65, 7, "'Whoa'", "'DURACAO'"],
        [66, 7, "'Conspiracy'", "'DURACAO'"],
        [67, 7, "'Franklin'", "'DURACAO'"],
        [68, 7, "'My Heart'", "'DURACAO'"],
        [69, 8, "'Born To Die'", "'DURACAO'"],
        [70, 8, "'Off To The Races'", "'DURACAO'"],
        [71, 8, "'Blue Jeans'", "'DURACAO'"],
        [72, 8, "'Video Games'", "'DURACAO'"],
        [73, 8, "'Diet Mountain Dew'", "'DURACAO'"],
        [74, 8, "'National Anthem'", "'DURACAO'"],
        [75, 8, "'Dark Paradise'", "'DURACAO'"],
        [76, 8, "'Radio'", "'DURACAO'"],
        [77, 8, "'Carmen'", "'DURACAO'"],
        [78, 8, "'Million Dollar Man'", "'DURACAO'"],
        [79, 8, "'Summertime Sadness'", "'DURACAO'"],
        [80, 8, "'This Is What Makes Us Girls'", "'DURACAO'"],
        [81, 8, "'Without You'", "'DURACAO'"],
        [82, 8, "'Lolita'", "'DURACAO'"],
        [83, 8, "'Lucky Ones'", "'DURACAO'"],
        [84, 9, "'Winter'", "'DURACAO'"],
        [85, 9, "'Smother'", "'DURACAO'"],
        [86, 9, "'Youth'", "'DURACAO'"],
        [87, 9, "'Still'", "'DURACAO'"],
        [88, 9, "'Lifeforms'", "'DURACAO'"],
        [89, 9, "'Tomorrow'", "'DURACAO'"],
        [90, 9, "'Human'", "'DURACAO'"],
        [91, 9, "'Touch'", "'DURACAO'"],
        [92, 9, "'Amsterdam'", "'DURACAO'"],
        [93, 9, "'Shallows'", "'DURACAO'"],
        [94, 10, "'Green Light'", "'DURACAO'"],
        [95, 10, "'Sober'", "'DURACAO'"],
        [96, 10, "'Homemade Dynamite'", "'DURACAO'"],
        [97, 10, "'The Louvre'", "'DURACAO'"],
        [98, 10, "'Liability'", "'DURACAO'"],
        [99, 10, "'Hard Feelings / Loveless'", "'DURACAO'"],
        [100, 10, "'Sober Ii (Melodrama)'", "'DURACAO'"],
        [101, 10, "'Writer In The Dark'", "'DURACAO'"],
        [102, 10, "'Supercut'", "'DURACAO'"],
        [103, 10, "'Liability (Reprise)'", "'DURACAO'"],
        [104, 10, "'Perfect Places'", "'DURACAO'"],
        [105, 11, "'Curtains Up ( Skit)'", "'DURACAO'"],
        [106, 11, "'White America'", "'DURACAO'"],
        [107, 11, "'Business'", "'DURACAO'"],
        [108, 11, "'Cleanin Out My Closet'", "'DURACAO'"],
        [109, 11, "'Square Dance'", "'DURACAO'"],
        [110, 11, "'The Kiss'", "'DURACAO'"],
        [111, 11, "'Soldier'", "'DURACAO'"],
        [112, 11, "'Say Goodbye Hollywood'", "'DURACAO'"],
        [113, 11, "'Drips'", "'DURACAO'"],
        [114, 11, "'Without Me'", "'DURACAO'"],
        [115, 11, "'Paul Rosenberg'", "'DURACAO'"],
        [116, 11, "'Sing For The Moment'", "'DURACAO'"],
        [117, 11, "'Superman'", "'DURACAO'"],
        [118, 11, "'Hailies Song'", "'DURACAO'"],
        [119, 11, "'Steve Berman'", "'DURACAO'"],
        [120, 11, "'When The Music Stops'", "'DURACAO'"],
        [121, 11, "'Say What You Say'", "'DURACAO'"],
        [122, 11, "'Till I Collapse'", "'DURACAO'"],
        [123, 11, "'My Dads Gone Crazy'", "'DURACAO'"],
        [124, 11, "'Curtains Close'", "'DURACAO'"],
        ]


# idEntidadeMusical compoe idAlbum -> FEITO
tableCompoe = [
        [1, 1],
        [1, 2],
        [2, 3],
        [3, 4],
        [4, 5],
        [5, 6],
        [5, 7],
        [6, 8],
        [7, 9],
        [8, 10],
        [9, 11], 
        ]

# idEstiloMusica, idMusica -> FEITO Fazer mais estilos de musica se calhar?
tableEstiloMusica = [
        #Nirvana Songs -> Rock and Grunge
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [1, 6],
        [1, 7],
        [1, 8],
        [1, 9],
        [1, 10],
        [1, 11],
        [1, 12],
        [1, 13],
        [1, 14],
        [1, 15],
        [1, 16],
        [1, 17],
        [1, 18],
        [1, 19],
        [1, 20],
        [1, 21],
        [1, 22],
        [1, 23],
        [1, 24],
        [1, 25],
        [2, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [2, 5],
        [2, 6],
        [2, 7],
        [2, 8],
        [2, 9],
        [2, 10],
        [2, 11],
        [2, 12],
        [2, 13],
        [2, 14],
        [2, 15],
        [2, 16],
        [2, 17],
        [2, 18],
        [2, 19],
        [2, 20],
        [2, 21],
        [2, 22],
        [2, 23],
        [2, 24],
        [2, 25],
        # Foo Fighters - Rock and some grunge
        [1, 26],
        [1, 27],
        [1, 28],
        [1, 29],
        [2, 29],
        [1, 30],
        #RadioHead
        [1, 31],
        [1, 32],
        [1, 33],
        [1, 34],
        [1, 35],
        [1, 36],
        # Billie Eilish - Indie
        [2, 38],
        [2, 39],
        [2, 40],
        [2, 41],
        [2, 42],
        [2, 43],
        [2, 44],
        [2, 45],
        [2, 46],
        [2, 47],
        # Paramore
        [2, 48],
        [2, 49],
        [2, 50],
        [2, 51],
        [2, 52],
        [2, 53],
        [2, 54],
        [2, 55],
        [2, 56],
        [2, 57],
        [2, 58],
        [2, 59],
        [2, 60],
        [2, 61],
        [2, 62],
        [2, 63],
        [2, 64],
        [2, 65],
        [2, 66],
        [2, 67],
        [2, 68],
        # Lana
        [3, 69],
        [3, 70],
        [3, 71],
        [3, 72],
        [3, 73],
        [3, 74],
        [3, 75],
        [3, 76],
        [3, 77],
        [3, 78],
        [3, 79],
        [3, 80],
        [3, 81],
        [3, 82],
        [3, 83],
        # Daughter
        [2, 84],
        [3, 84],
        [2, 85],
        [2, 86],
        [2, 87],
        [2, 88],
        [2, 89],
        [2, 90],
        [2, 91],
        [2, 92],
        [2, 93],
        # Lorde
        [3, 94],
        [3, 95],
        [2, 95],
        [3, 96],
        [3, 97],
        [3, 98],
        [3, 99],
        [3, 100],
        [3, 101],
        [3, 102],
        [3, 103],
        [3, 104],
        # Eminem
        [5, 105],
        [5, 106],
        [5, 107],
        [5, 108],
        [5, 109],
        [5, 110],
        [5, 111],
        [5, 112],
        [5, 113],
        [5, 114],
        [5, 115],
        [5, 116],
        [5, 117],
        [5, 118],
        [5, 119],
        [5, 120],
        [5, 121],
        [5, 122],
        [5, 123],
        [5, 124],
        ]

# idEstiloMusical, NomeEstilo -> FEITO
tableEstiloMusical = [
        [1, "'Rock'"],
        [2, "'Indie'"],
        [3, "'Pop'"],
        [4, "'Grunge'"],
        [5, "'Hip Hop'"]
        ]

# Papel que o artista desempenha -> FEITO
# idArtista, idPapel
tableDesempenha = [
        # Nirvana 
        [31, 1],
        [31, 2],
        [32, 5],
        [33, 1],
        [33, 4],
        # Foo Fighters
        [34, 5],
        [35, 4],
        # Radiohead
        [36, 1],
        [37, 1],
        [38, 1],
        [39, 2],
        [40, 2],
        # Billie
        [41, 1],
        [41, 2],
        # Paramore
        [42, 1],
        [42, 3],
        [43, 2],
        [44, 4],
        # Lana del Rey
        [45, 1],
        [45, 6], 
        #Daughter,
        [46, 1],
        [47, 2],
        [48, 4],
        #Lorde
        [49, 1],
        [49, 6],
        # Eminem
        [50, 1],
        ]

# Papeis que a banda possui
# idEntidadeMusical, idPapel -> FEITO
tablePossui = [
        # Nirvana
        [1, 1],
        [1, 2],
        [1, 4],
        [1, 5],
        # Foo Fighters
        [2, 1],
        [2, 4],
        [2, 5],
        # Radiohead
        [3, 1],
        [3, 2],
        # Billie
        [4, 1],
        #  Paramore
        [5, 1],
        [5, 2],
        [5, 3],
        [5, 4],
        # Lana
        [6, 1],
        [6, 6],
        # Daughter
        [7, 1],
        [7, 2],
        [7, 4],
        # Lorde
        [8, 1],
        [8, 6],
        #Eminem
        [9, 1],
        ]

# idArtista, idEntidadeMusical -> FEITO
tableMembro = [
        # Nirvana
        [31, 1], 
        [32, 1],
        [33, 1],
        # Foo
        [34, 2],
        [35, 2],
        # Radiohead
        [36,3],
        [37,3],
        [38,3],
        [39,3],
        [40,3],
        # Billie
        [41, 4],
        # Paramore
        [42, 5],
        [43, 5],
        [44, 5],
        # Lana Del Rey
        [45, 6],
        # Daughter
        [46, 7],
        [47, 7],
        [48, 7],
        # Lorde
        [49, 8],
        # Eminem
        [50, 9],
        ]


# idPlaylsit, idutilizador, nome, imagem, datacriacao, descriçao, privada
tablePlaylist = [
        [1, 1, "'I Love 90'",           "'imagem'", "'2020'",   "'Best songs of 90s'",              0],
        [2, 2, "'Indie'",              "'imagem'", "'2020'",   "'New Indie Trend'",                0],
        [3, 3, "'Me and my Friends'",   "'imagem'", "'2020'",   "'Put your favorite songs here!'",  1],
        ]

# idSessao, dia -> CRIAR MAIS SESSÕES E COMPLETAR O TEMPO OUVIDO
tableSessao = [
        [ 1, "'16/03/2020'"],
        [ 2, "'16/03/2020'"],
        [ 3, "'16/03/2020'"],
        [ 4, "'17/03/2020'"],
        [ 5, "'17/03/2020'"],
        ]

# idSessao, idMusica, duracao
tableTempoOuvido = [
        [1,  1, "'270'"],
        [1,  2, "'340'"],
        [2,  3, "''"],
        [2, 20, "''"],
        [2, 21, "''"],
        [2, 22, "''"],
        [2, 23, "''"],
        [2, 24, "''"],
        [2, 25, "''"],
        [2, 26, "''"],
        [2, 27, "''"],
        [2, 28, "''"],
        [2, 29, "''"],
        [2, 30, "''"],
        [2, 31, "''"],
        [2, 32, "''"],
        [2, 33, "''"],
        [2, 34, "''"],
        [2, 35, "''"],
        [2, 36, "''"],
        [2, 37, "''"],
        [3, 1,  "''"],
        [3, 2,  "''"],
        [3, 3,  "''"],
        [3, 4,  "''"],
        [3, 5,  "''"],
        [3, 6,  "''"],
        [3, 7,  "''"],
        [3, 8,  "''"],
        [3, 9,  "''"],
        [3, 10, "''"],
        [3, 11, "''"],
        [4, 13, "''"],
        [4, 14, "''"],
        [4, 15, "''"],
        [4, 16, "''"],
        [4, 17, "''"],
        [4, 18, "''"],
        [4, 19, "''"],
        [4, 20, "''"],
        [5, 13, "''"],
        ]


# idUtilizador, idMusica
tableFavoritoAlbum = [
        [1, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 1],
        [4, 1],
        [5, 3],
        ]

# idUtilizador, idMusica, data -> AUMENTAR ISTO! SÓ DEPOIS DE FAZZER OS UTILIZADORES TODOS!
tableFavoritoMusica =  [
        [2, 10, "'15/03/2020'"],
        [1, 5, "'17/03/2020'"],
        ]

#idUtilizador, idPlaylist -> AUMENTAR ISTO! SÓ DEPOIS DE FAZER UTILIZADORES E PLAYLISTS TODAS
tableFavoritoPlaylist = [
        [3, 1],
        [2, 3],
        ]

# idUtilizador, idPlaylist -> AUMENTAR ISTO! SÓ DEPOIS DE FAZER UTILIZADORES E PLAYLISTS TODAS
tableColabora = [
        [1, 3],
        [3, 3],
        ]


# idUtilizador, idSessao  -> AUMENTAR ISTO! SÓ DEPOIS DE FAZZER OS UTILIZADORES TODOS!
tableUtilizadorSessao = [
        [1, 1],
        [2, 2],
        [2, 4],
        [3,  3],
        [1, 4],
        [1, 5],
        [1, 3],
        ]

# idPlaylist, idMusica  -> AUMENTAR ISTO! SÓ DEPOIS DE FAZZER AS PLAYLISTS TODAS
tablePertence = [
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [1, 5],
        [1, 6],
        [1, 7],
        [1, 8],
        [1, 9],
        [1, 10],
        [1, 11],
        [1, 12],
        [2, 15],
        [2, 18],
        [2, 22],
        [2, 23],
        [2, 24],
        [2, 25],
        [3, 28],
        [3, 32],
        ]

# idUtilizador, idUtilizadorSeguido
tableSegue = [
        [3, 1],
        [1, 3],
        [2, 1],
        [2, 3],
        [1, 2],
        [1, 1],
        ]


classes = {"Pessoa" : tablePessoa,
           "Artista" : tableArtista,
           "Utilizador" : tableUtilizador,
           "Papel" : tablePapel,
           "EntidadeMusical" : tableEntidadeMusical,
           "Album" : tableAlbum,
           "Musica" : tableMusica,
           "EstiloMusical" : tableEstiloMusical,
           "Playlist" : tablePlaylist,
           "Sessao" : tableSessao,
           "TempoOuvido" : tableTempoOuvido,
           "Desempenha" : tableDesempenha,
           "Possui" : tablePossui,
           "Membro" : tableMembro,
           "Compoe" : tableCompoe,
           "FavoritoAlbum" : tableFavoritoAlbum,
           "FavoritoMusica" : tableFavoritoMusica,
           "FavoritoPlaylist" : tableFavoritoPlaylist,
           "Colabora" : tableColabora,
           "EstiloMusica" : tableEstiloMusica,
           "UtilizadorSessao" : tableUtilizadorSessao,
           "Pertence" : tablePertence,
           "Segue" : tableSegue,
           }
           

def values(listName):
    return ', '.join(str(a) for a in listName)

def addAlbum(idEntidadeMusical, idEstiloMusical, url): 
    idAlbum = len(tableAlbum) + 1
    listaMusica = []
    listaEstiloMusical = []
        
    url_content = requests.get(url)
    url_data = BeautifulSoup(url_content.content, "html.parser")
    
    idMusica = len(tableMusica) + 1   
    album = "'" + url_data.title.string[:-31] + "'"
    
    paragraphs = url_data.find_all('a')
    for para in paragraphs:
        if para.has_key('class'):
            if para['class'][0] == "nameMusic":
                for j in para['class']:
                    title = "'" + para.get_text() + "'"
                    listaMusica.append([idMusica, idAlbum, title, "'DURACAO'"])
                    listaEstiloMusical.append([idEstiloMusical, idMusica])
                    idMusica += 1
    
    print("\n\n\ntableAlbum =")
    print([idAlbum, album, "'capa'", "'YEAR'"],)
    
    print("\n\n\ntableMusica =")
    for i in listaMusica:
        print(i, end = ",\n")
        
    
    print("\n\n\ntableCompoe =")
    print([idEntidadeMusical, idAlbum],)
    
    print("\n\n\ntableEstiloMusica =")
    for i in listaEstiloMusical:
        print(i, end = ",\n")
        
    return 0

def povoar():
    f = open("povoar.sql", "w")
    
    for classeName in classes:
        f.write("-- {} \n".format(classeName))
        for i in range(len(classes[classeName])):
            f.write("INSERT INTO {} VALUES({});\n".format(classeName, values(classes[classeName][i])))
        f.write("\n")
        
    f.close()
    return 0

def main():
    value = input("1. Povoar\n2. Add Artist Album\n Option: ")
    if value == '1':
        povoar()
    elif value == '2':
        idEntidadeMusical = int(input("idEntidadeMusical: "))
        idEstiloMusical = int(input("idEstiloMusical: "))
        url = input("url: ")
        addAlbum(idEntidadeMusical, idEstiloMusical, url)
    return 0

main()