import requests
from bs4 import BeautifulSoup

# idPessoa, Nome, DataNascimento, CodigoPostal, Morada
tablePessoa = [
        #Utilizadors -> Dar nomes significativos
        [1, "'Hugo Guimaraes'",     "'17-07-2000'",    "'4490-438'", "'Praca dos Combatentes'"],
        [2, "'Samuel Fernandes'",   "'28-06-2000'",    "'4860-466'", "'Rua Doutor Franscico Botelho'"],
        [3, "'Paulo Ribeiro'",      "'16-10-2000'",    "'4490-421'", "'Praca do Almada'"],
        [4, "'Pedro Nero '",        "'28-01-1969'",    "'4490-438'", "'Praca dos Combatentes'"],
        [5, "'Ana Monteiro'",       "'24-08-1969'",    "'4490-438'", "'Praca dos Combatentes'"],
        [6, "'Marta Lopes'",        "'12-01-2000'",    "'4465-428'", "'Avenida 25 de Abril'"],
        [7, "'Marta Figueiredo'",   "'30-01-2000'",    "'4490-125'", "'Rua 31 de Janeiro'"],
        [8, "'Rodrigo Festas'",     "'17-07-2000'",    "'4490-436'", "'Rua Caetano de Oliveira'"],
        [9, "'Carlos Monteiro'",    "'17-07-2000'",    "'4490-211'", "'Rua Doutor Leonardo Coimbra'"],
        [10, "'Rui Samudio'",       "'04-01-2001'",    "'4490-118'", "'Rua da Junqueira'"],
        [11, "'Matilde Vale'",      "'09-11-2000'",    "'4480-216'", "'Rua Nova'"],
        [12, "'Ana Santos'",        "'10-01-2000'",    "'4480-657'", "'Rua 1'"],
        [13, "'Pedro Castro'",      "'19-03-2000'",    "'4860-510'", "'Chacim'"],
        [14, "'Bernardo Vaz'",      "'25-08-2000'" ,   "'4860-528'", "'Rua de Outeirinho'"],
        [15, "'Marta Vieitas'",     "'12-01-1999'",    "'3020-852'", "'Avenida Sá da Bandeira'"],
        [16, "'Ines Machado'",      "'17-07-2000'",    "'3020-174'", "'Rua das Azeiteiras'"],
        [17, "'Olena Shelvytska'",  "'09-06-1998'",    "'79007-888'","'Lviv Snow Stree'"],
        [18, "'Beatriz Mendes'",    "'01-06-2000'",    "'4850-715'", "'Centro da Maia'"],
        [19, "'Marta Santos'",      "'09-12-2001'",    "'4425-628'", "'Rua 1o de janeiro'"],
        [20, "'Mafalda Silva'",     "'25-06-1987'",    "'4425-834'", "'Rua 1o de maio'"],
        [21, "'Diogo Figueiredo'",  "'31-03-2000'",    "'1900-777'", "'Avenida Valente de Oliveira'"],
        [22, "'Jose Arriscado'",    "'22-2-2000'",     "'1900-255'", "'Avenida Afonso Costa'"],
        [23, "'Inacio Vasconcelos'","'11-06-1998'",    "'1900-680'", "'Avenida Afonso III'"],
        [24, "'Diana Freitas'",     "'24-07-1999'",    "'4000-901'", "'Avenida Cidade do Porto'"],
        [25, "'Afonso Festas'",     "'09-03-2006'",    "'4000-551'", "'Rua Escura'"],
        [26, "'Alice Horta'",       "'03-08-2000'",    "'4000-817'", "'Rua do Rosario'"],
        [27, "'Carlos Lopes'",      "'13-10-1999'",    "'4000-671'", "'Rua de Passos Manuel'"],
        [28, "'Miguel Rodrigues'",  "'01-02-2001'",    "'4000-586'", "'Rua de Sao Bento da Vitoria'"],
        [29, "'Leonor Coelho'",     "'17-03-2000'",    "'4000-249'", "'Rua de Miguel Bombarda'"],
        [30, "'Telma Araujo'",      "'12-09-2000'",    "'4801-686'", "'Rua de Santa Maria'"],        
        
        # Artistas -> Colocar a data de nascimento, codigo postal e rua
        #   NIRVANA
        [31, "'Kurt Cobain'",                       "'20-02-1967'",    "'01800-273'",   "'McGillen Street'"],
        [32, "'Krist Novoselic'",                   "'16-05-1965'",    "'90220-155'",   "'BigTown Avenue'"],
        [33, "'Dave Grohl'",                        "'14-01-1969'",    "'80892-256'",   "'Pretender Avenue'"],
        # FOO FIGHTERS
        [34,"'Nate Mendel'",                        "'02-12-1968'",    "'58235-766'",   "'Flower Sreet'"],
        [35,"'Taylor Hawkins'",                     "'17-02-1972'",    "'76008-355'",   "'5th of June Street'"],
        # RADIOHEAD
        [36, "'Thomas Yorke'",                      "'07-10-1968'",    "'33368-512'",   "'Route 214'"],
        [37, "'Johnny Greenwood'",                  "'05-11-1971'",    "'27813-221'",   "'5th Avenue'"],
        [38, "'Colin Greenwood'",                   "'15-04-1968'",    "'27813-647'",   "'Major Campbell Street'"],
        [39, "'Ed Obrien'",                         "'26-06-1969'",    "'27814-331'",   "'Small path'"],
        [40, "'Philip Selway'",                     "'23-05-1967'",    "'54221-446'",   "'Route 20'"],
        # BILLIE EILISH
        [41, "'Billie Eilish'",                     "'18-12-2001'",    "'66722-666'",   "'Lil Street'"],
        #Paramore
        [42,"'Hayley Williams'",                    "'27-12-1988'",    "'65352-322'",   "'504 Street'"],
        [43,"'Taylor York'",                        "'17-12-1989'",    "'48569-669'",   "'New Street'"],
        [44,"'Zac Farro'",                          "'04-06-1990'",    "'78845-541'",   "'Father Brown Street'"],
        # Lana del Rey
        [45,"'Elizabeth Grant'",                    "'21-06-1985'",    "'23141-587'",   "'Clubs Square'"],
        #Daughter
        [46, "'Elena Tonra'",                       "'15-01-1990'",    "'44751-417'",   "'Math Jones Street'"],
        [47, "'Igor Haefeli'",                      "'07-03-1987'",    "'25874-968'",   "'Tiana Square'"],
        [48, "'Remi Aguilella'",                    "'15-02-1977'",    "'96985-742'",   "'Bellatrix Avenue'"],
        # Lorde
        [49, "'Ella Yelich-OConnor'",               "'07-11-1996'",    "'47742-568'",   "'Epsom Auckland'"],
        # Eminem
        [50, "'Marshall Bruce Mathers'",            "'17-10-1972'",    "'12536-887'",   "'Johns Square'"],
        #Muse
        [51, "'Matt Bellamy'",                      "'09-06-1978'",    "'89451-213'",   "'Route 404'"],
        [52, "'Chris Wolstenholme'",                "'02-12-1978'",    "'36498-235'",   "'Maitland Street'"],
        [53, "'Dominic Howard'",                    "'07-12-1977'",    "'14764-354'",   "'Silva Avenue'"],
        ]

# idPessoa, anoInicio carreira de cada artista
tableArtista = [
        [31 , "1987"],
        [32 , "1987"],
        [33 , "1987"],
        [34 , "1994"],
        [35 , "1994"],
        [36, "'1985'"],
        [37, "'1985'"],
        [38, "'1985'"],
        [39, "'1985'"],
        [40, "'1985'"],
        [41, "'2015'"],
        [42, "'2003'"],
        [43, "'2001'"],
        [44, "'2004'"],
        [45, "'2005'"],
        [46, "'2010'"],
        [47, "'2010'"],
        [48, "'2010'"],
        [49, "'2009'"],
        [50, "'1988'"],
        [51, "'1991'"],
        [52, "'1991'"],
        [53, "'1994'"],
        ]

#        
#idPessoa, email, username, password -> NOMES SIGNIFICATIVOS!
tableUtilizador = [
        [1,  "'hugomguima@gmail.com'",  "'Huguima'",    "'gagdafgdfgfdsg'"],
        [2,  "'samue@hotmail.com'",     "'Samuh'",      "'asvvaevaf'"],
        [3,  "'pjbom.best@gmail.com'",  "'PJbomXD'",      "'paulinho123'"],
        [4,  "'pedro.nero@hotmail.com'",  "'pnero'",    "'asafs1234'"],
        [5,  "'ana.monteiro@hotmail.com'","'amonteiro'",     "'njkfj1244'"],
        [6,  "'m.lopes798@gmail.com'","'MartaLopes798'",     "'m798asffad'"],
        [7,  "'martafigueredo254@gmail.com'","'martafigueiredo00'",     "'design3434'"],
        [8,  "'rodrugsparties@gmail.com'",    "'Rfestas'",     "'jarreta34'"],
        [9,  "'cmonteiro@gmail.com'",    "'CarlosMonteiro'",  "'mcmonteiro'"],
        [10,  "'laura_freitas@outlook.com'",    "'freitas'",  "'good_password'"],
        [11,  "'matildevale'",    "'Matile V.C.'",  "'catsAndDogs'"],
        [12,  "'Anasantos@gmail.com'",    "'Ana San'",  "'halelujah34'"],
        [13,  "'PedroCastro@gmail.com'",    "'P. Castro'",  "'Ameemmmmsad'"],
        [14,  "'Bernasvaz468@gmail.com'",    "'Bern Vaz'",  "'passssssssss'"],
        [15,  "'msvieitas@hotmail.com'",    "'m_Vieitas'",  "'protegido234'"],
        [16,  "'inesmachado456@gmail.com'",    "'YayQueima'",  "'naoVaoDescobrir'"],
        [17,  "'Ole.Shelv@outlook.com'",    "'oShelvy'",  "'ukraineislit'"],
        [18,  "'ziniii@outlook.com'",    "'ZiniWhini'",  "'egirl1234'"],
        [19,  "'MartaSantos652@outlook.com'",    "'Marta Santos'",  "'santos123'"],
        [20,  "'Mfsilvaa01@outlook.com'",    "'Mafalda s01'",  "'lopes1243'"],
        [21,  "'digofigueiredo@gmail.com'",    "'digofixe'",  "'xxdigofixexx'"],
        [22,  "'zerisk@outlook.com'",    "'jose boy'",  "'zeboy2000'"],
        [23,  "'inacio_celos.com'",    "'Inacio Vasconcelos'",  "'inaskim34'"],
        [24,  "'Dianamfreitas@gmail.com'",    "'DianaFreitas'",  "'adorolcom34'"],
        [25,  "'memeboy254@outlook.com'",    "'Alphonso Parties'",  "'XxX420XxX'"],
        [26,  "'iamalice@outlook.com'",    "'Alice M. Horta'",  "'aMorta34234'"],
        [27,  "'c.lopes@gmail.com'",    "'teste5'",  "'123456789'"],
        [28,  "'mike.rodriguez@gotmail.com'",    "'mike123'",  "'123456789'"],
        [29,  "'bunnygirl@outlook.com'",    "'Leo C'",  "'123456789'"],
        [30,  "'metallover@gmail.com'",    "'MC Araujo'",  "'123456789'"],
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
        [1, "'Nirvana'",        "'https://imgur.com/sQ5G0n7.jpg'", "1987",     "'Grande sucesso com o estilo grunge'"],
        [2, "'Foo Fighters'",   "'https://imgur.com/ZvzxczA.jpg'", "1994",     "'Criada após o fim dos Nirvana'"],
        [3, "'Radiohead'",      "'https://imgur.com/2oHQiO1.jpg'", "1985",     "'Creep foi o 1o e maior single deles'"],
        [4, "'Billie Eilish'",  "'https://imgur.com/Gv4Ijf6.jpg'", "2016",     "'Ficou famosa com apenas 17 anos!!'"],
        [5, "'Paramore'",       "'https://imgur.com/bRlpyPj.jpg'", "2004",     "'WE ARE PARAMORE!'"],
        [6, "'Lana Del Rey'",   "'https://imgur.com/FmZk0ba.jpg'", "2005",     "'Utiliza frequentemente referencias ao pop americano'"],
        [7, "'Daughter'",       "'https://imgur.com/fQkzZ54.jpg'", "2009",     "'Foi responsavel pela banda sonora de Life is Strange'"],
        [8, "'Lorde'",          "'https://imgur.com/fOzO8jd.jpg'", "1988",     "'Nomeada Mulher Do Ano pela MTV, em 2013'"],
        [9, "'Eminem'",         "'https://imgur.com/A3Uav84.jpg'", "1988",     "'Melhor rapper de sempre'"],
        [10, "'Muse'",          "'https://imgur.com/51doL6Y.jpg'", "1994",     "'Excelente banda, musicas geniais!'"],
        
        ]

# id album, nome, capa, ano -> COLOCAR ANO E CAPAhttps://imgur.com/Gv4Ijf6.jpg
tableAlbum = [
        [1, "'Nevermind'",                                  "'https://imgur.com/pEvqHkD.jpg'", "1991"],
        [2, "'In Utero'",                                   "'https://imgur.com/zJgJ1mC.jpg'", "1993"],
        [3, "'Concrete and Gold'",                          "'https://imgur.com/b4TbjVO.jpg'", "2017"],
        [4, "'OK Computer'",                                "'https://imgur.com/7Prc1JI.jpg'", "1997"],
        [5, "'When We All Fall Asleep, Where Do We Go?'",   "'https://imgur.com/181OJ2a.png'", "2019"],
        [6, "'Brand New Eyes'",                             "'https://imgur.com/2zUv7QL.jpg'", "2009"],
        [7, "'All We Know Is Falling'",                     "'https://imgur.com/Gh2Y21E.jpg'", "2005"],
        [8, "'Born to Die'",                                "'https://imgur.com/uBrvfNq.jpg'", "2012"],
        [9, "'If You Leave'",                               "'https://imgur.com/zxyhdom.jpg'", "2013"],
        [10, "'Melodrama'",                                 "'https://imgur.com/RjJRaBE.jpg'", "2017"],
        [11, "'The Eminem Show'",                           "'https://imgur.com/fRAUYWb.jpg'", "2002"],
        [12, "'Origin of Symmetry'",                        "'https://imgur.com/0jNvjCQ.jpg'", "2001"],
        
        ]

#idmusica, idalbum, nomeal -> COLOCAR DURACAO
tableMusica = [
        [1, 1, "'Smells Like Teen Spirit'",302 ],
        [2, 1, "'In Bloom'", 255],
        [3, 1, "'Come As You Are'", 219],
        [4, 1, "'Breed'", 184],
        [5, 1, "'Lithium'", 257],
        [6, 1, "'Polly'", 174],
        [7, 1, "'Territorial Pissings'", 143],
        [8, 1, "'Drain You'", 224],
        [9, 1, "'Lounge Act'", 156],
        [10, 1, "'Stay Away'", 211],
        [11, 1, "'On A Plain'", 194],
        [12, 1, "'Something In The Way'", 232],
        [13, 2, "'Serve The Servants'", 217],
        [14, 2, "'Scentless Apprentice'", 228],
        [15, 2, "'Heart-shaped Box'", 281],
        [16, 2, "'Rape Me'", 170],
        [17, 2, "'Frances Farmer Will Have Her Revenge On Seattle'", 250],
        [18, 2, "'Dumb'", 152],
        [19, 2, "'Very Ape'", 116],
        [20, 2, "'Milk It'", 235],
        [21, 2, "'Pennyroyal Tea'", 219],
        [22, 2, "'Radio Friendly Unit Shifter'", 292],
        [23, 2, "'Tourette`s'", 95],
        [24, 2, "'All Apologies'", 233],
        [25, 2, "'Gallons Of Rubbing Alcohol Flow Through The Strip'", 454],
        [26, 3, "'T-Shirt'", 83],
        [27, 3, "'Run'", 323],
        [28, 3, "'Make It Right'", 279],
        [29, 3, "'The Sky Is a Neighborhood'", 245],
        [30, 3, "'Concrete and Gold'", 332],
        [31, 4, "'Karma Police'", 288],
        [32, 4, "'Fitter, Happier'", 177],
        [33, 4, "'Electioneering'", 231],
        [34, 4, "'Climbing Up The Walls'", 285],
        [35, 4, "'No Surprises'", 229],
        [36, 4, "'Lucky'", 259],
        [37, 4, "'The Tourist'", 327],
        [38, 5, "'Bad Guy'", 194],
        [39, 5, "'Xanny'", 244],
        [40, 5, "'You Should See Me In a Crown'", 181],
        [41, 5, "'All The Good Girls Go To Hell'", 169],
        [42, 5, "'My Strange Addiction'", 180],
        [43, 5, "'Bury a Friend'", 193],
        [44, 5, "'Ilomilo'", 156],
        [45, 5, "'Listen Before I Go'", 243],
        [46, 5, "'I Love You'", 292],
        [47, 5, "'Goodbye'", 119],
        [48, 6, "'Careful'", 230],
        [49, 6, "'Ignorance'", 219],
        [50, 6, "'Playing God'", 183],
        [51, 6, "'Brick By Boring Brick'", 254],
        [52, 6, "'Turn It Off'", 260],
        [53, 6, "'The Only Exception'", 268],
        [54, 6, "'Feeling Sorry'", 185],
        [55, 6, "'Looking Up'", 209],
        [56, 6, "'Where The Lines Overlap'", 199],
        [57, 6, "'Misguided Ghosts'", 182],
        [58, 6, "'All I Wanted'", 226],
        [59, 7, "'All We Know'", 194],
        [60, 7, "'Pressure'", 186],
        [61, 7, "'Emergency'", 240],
        [62, 7, "'Brighter'", 223],
        [63, 7, "'Here We Go Again'", 226],
        [64, 7, "'Never Let This Go'", 221],
        [65, 7, "'Whoa'", 201],
        [66, 7, "'Conspiracy'", 222],
        [67, 7, "'Franklin'", 199],
        [68, 7, "'My Heart'", 239],
        [69, 8, "'Born To Die'", 285],
        [70, 8, "'Off To The Races'", 300],
        [71, 8, "'Blue Jeans'", 209],
        [72, 8, "'Video Games'", 282],
        [73, 8, "'Diet Mountain Dew'",223],
        [74, 8, "'National Anthem'", 231],
        [75, 8, "'Dark Paradise'", 243],
        [76, 8, "'Radio'", 215],
        [77, 8, "'Carmen'", 249],
        [78, 8, "'Million Dollar Man'", 232],
        [79, 8, "'Summertime Sadness'", 265],
        [80, 8, "'This Is What Makes Us Girls'", 238],
        [81, 8, "'Without You'", 229],
        [82, 8, "'Lolita'", 220],
        [83, 8, "'Lucky Ones'", 225],
        [84, 9, "'Winter'", 283],
        [85, 9, "'Smother'", 241],
        [86, 9, "'Youth'", 253],
        [87, 9, "'Still'", 213],
        [88, 9, "'Lifeforms'", 335],
        [89, 9, "'Tomorrow'", 281],
        [90, 9, "'Human'", 212],
        [91, 9, "'Touch'", 266],
        [92, 9, "'Amsterdam'", 243],
        [93, 9, "'Shallows'", 414],
        [94, 10, "'Green Light'", 235],
        [95, 10, "'Sober'", 197],
        [96, 10, "'Homemade Dynamite'", 190],
        [97, 10, "'The Louvre'", 271],
        [98, 10, "'Liability'", 172],
        [99, 10, "'Hard Feelings / Loveless'", 367],
        [100, 10, "'Sober Ii (Melodrama)'", 179],
        [101, 10, "'Writer In The Dark'", 217],
        [102, 10, "'Supercut'", 278 ],
        [103, 10, "'Liability (Reprise)'", 136],
        [104, 10, "'Perfect Places'", 222],
        [105, 11, "'Curtains Up ( Skit)'", 30],
        [106, 11, "'White America'", 325],
        [107, 11, "'Business'", 252],
        [108, 11, "'Cleanin Out My Closet'", 298],
        [109, 11, "'Square Dance'", 324],
        [110, 11, "'The Kiss'", 76],
        [111, 11, "'Soldier'", 226],
        [112, 11, "'Say Goodbye Hollywood'", 273],
        [113, 11, "'Drips'", 286],
        [114, 11, "'Without Me'", 290],
        [115, 11, "'Paul Rosenberg'", 23],
        [116, 11, "'Sing For The Moment'", 340],
        [117, 11, "'Superman'", 350],
        [118, 11, "'Hailies Song'", 321],
        [119, 11, "'Steve Berman'", 33],
        [120, 11, "'When The Music Stops'", 269],
        [121, 11, "'Say What You Say'", 310],
        [122, 11, "'Till I Collapse'", 298],
        [123, 11, "'My Dads Gone Crazy'", 267],
        [124, 11, "'Curtains Close'", 62],
        [125, 12, "'New Born'", 364],
        [126, 12, "'Bliss'", 252],
        [127, 12, "'Space Dementia'", 381],
        [128, 12, "'Hyper Music'", 202],
        [129, 12, "'Plug in Baby'", 218],
        [130, 12, "'Citizen Erased'", 442],
        [131, 12, "'Micro Cuts'", 219],
        [132, 12, "'Screenager'", 260],
        [133, 12, "'Dark Shines'", 287],
        [134, 12, "'Feeling Good'", 199],
        [135, 12, "'Megalomania'", 280],
        [136, 12, "'Futurism'", 267],
        
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
        [10, 12],
        ]

# idEstiloMusica, idMusica -> FEITO Fazer mais estilos de musica se calhar?
tableMusicaEstilo = [
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
        # Muse
        [1, 125],
        [1, 126],
        [1, 127],
        [1, 128],
        [1, 129],
        [1, 130],
        [1, 131],
        [1, 132],
        [1, 133],
        [1, 134],
        [1, 135],
        [1, 136],
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
        # Muse
        [51, 1],
        [51, 2],
        [51, 3],
        [52, 1],
        [52, 5],
        [53, 4],
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
        # Eminem
        [9, 1],
        # Muse
        [10, 1],
        [10, 2],
        [10, 3],
        [10, 4],
        [10, 5],
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
        # Muse
        [51, 10],
        [52, 10],
        [53, 10],
        ]


# idPlaylsit, idutilizador, nome, imagem, datacriacao, descriçao, privada
tablePlaylist = [
        [1, 1, "'I Love 90'",           "'imagem'", "'2020'",   "'Best songs of 90s'",              0],
        [2, 2, "'Indie'",              "'imagem'", "'2020'",   "'New Indie Trend'",                0],
        [3, 4, "'Me and my Friends'",   "'imagem'", "'2020'",   "'Put your favorite songs here!'",  1],
        [4, 3, "'Best Rock Songs'",     "'imagem'", "'2020'",   "'The Perfect Playlist :D'", 0],
        ]

# idSessao, dia -> CRIAR MAIS SESSÕES E COMPLETAR O TEMPO OUVIDO
tableSessao = [
        [ 1, "'16-02-2020'"],
        [ 2, "'16-02-2020'"],
        [ 3, "'16-02-2020'"],
        [ 4, "'17-02-2020'"],
        [ 5, "'17-02-2020'"],
        [ 6, "'18-02-2020'"],
        [ 7, "'18-02-2020'"],
        [ 8, "'19-02-2020'"],
        [ 9, "'21-02-2020'"],
        [ 10, "'22-02-2020'"],
        [ 11, "'22-02-2020'"],
        [ 12, "'23-02-2020'"],
        [ 13, "'25-02-2020'"],
        [ 14, "'25-02-2020'"],
        [ 15, "'26-02-2020'"],
        [ 16, "'28-02-2020'"],
        [ 17, "'30-02-2020'"],
        [ 18, "'31-02-2020'"],
        [ 19, "'31-02-2020'"],
        [ 20, "'31-02-2020'"],
        [ 21, "'01-03-2020'"],
        [ 22, "'01-03-2020'"],
        [ 23, "'01-03-2020'"],
        [ 24, "'02-03-2020'"],
        [ 25, "'02-03-2020'"],
        [ 26, "'03-03-2020'"],
        [ 27, "'03-03-2020'"],
        [ 28, "'04-03-2020'"],
        [ 29, "'04-03-2020'"],
        [ 30, "'04-03-2020'"],
        [ 31, "'04-03-2020'"],
        [ 32, "'04-03-2020'"],
        [ 33, "'05-03-2020'"],
        [ 34, "'05-03-2020'"],
        [ 35, "'05-03-2020'"],
        [ 36, "'06-03-2020'"],
        [ 37, "'07-03-2020'"],
        [ 38, "'09-03-2020'"],
        [ 39, "'12-03-2020'"],
        [ 40, "'13-03-2020'"],
        [ 41, "'13-03-2020'"],
        [ 42, "'14-03-2020'"],
        [ 43, "'16-03-2020'"],
        [ 44, "'17-03-2020'"],
        [ 45, "'20-03-2020'"],
        [ 46, "'23-03-2020'"],
        [ 47, "'23-03-2020'"],
        [ 48, "'23-03-2020'"],
        [ 49, "'24-03-2020'"],
        [ 50, "'24-03-2020'"],
        [ 51, "'26-03-2020'"],
        [ 52, "'26-03-2020'"],
        [ 53, "'27-03-2020'"],
        [ 54, "'29-03-2020'"],
        [ 55, "'29-03-2020'"],
        [ 56, "'30-03-2020'"],
        [ 57, "'31-03-2020'"],
        [ 58, "'31-03-2020'"],
        [ 59, "'01-04-2020'"],
        [ 60, "'01-04-2020'"],
        
        ]

# idSessao, idMusica, duracao
tableTempoOuvido = [
        [1,  1, 270],
        [1,  2, 340],
        [2,  3, 420],
        [2, 20, 80],
        [2, 21, 120],
        [2, 22, 210],
        [2, 23, 267],
        [2, 24, 546],
        [2, 25, 126],
        [2, 26, 150],
        [2, 27, 220],
        [2, 28, 462],
        [2, 29, 236],
        [2, 30, 90],
        [2, 31, 99],
        [2, 32, 136],
        [2, 33, 16],
        [2, 34, 200],
        [2, 35, 110],
        [2, 36, 125],
        [2, 37, 135],
        [3, 1,  152],
        [3, 2,  223],
        [3, 3,  321],
        [3, 4,  162],
        [3, 5,  126],
        [3, 6,  278],
        [3, 7,  159],
        [3, 8,  124],
        [3, 9,  299],
        [3, 10, 331],
        [3, 11, 526],
        [4, 13, 136],
        [4, 14, 125],
        [4, 15, 158],
        [4, 16, 226],
        [4, 17, 240],
        [4, 18, 125],
        [4, 19, 324],
        [4, 20, 205],
        [5, 13, 186],
        [5, 15, 260],
        [5, 34, 200],
        [6, 33, 150],
        [6, 35, 165],
        [6, 19, 176],
        [6, 13, 173],
        [7, 33, 165],
        [7, 34, 172],
        [8,  1, 220],
        [8,  2, 440],
        [9,  3, 420],
        [9,  4, 420],
        [10, 40, 190],
        [10, 41, 20],
        [10, 42, 50],
        [10, 43, 265],
        [11, 56, 246],
        [11, 57, 238],
        [11, 58, 112],
        [11, 59, 220],
        [12, 70, 462],
        [13, 71, 236],
        [13, 72, 90],
        [14, 80, 99],
        [14, 81, 136],
        [15, 90, 16],
        [16, 91, 200],
        [16, 92, 110],
        [17, 54, 145],
        [18, 54, 139],
        [18, 19,  154],
        [18, 20,  123],
        [19, 20,  321],
        [20, 89,  152],
        [21, 90,  136],
        [22, 91,  178],
        [22, 91,  189],
        [23, 92,  154],
        [23, 93,  199],
        [23, 94, 231],
        [24, 100, 426],
        [25,  18, 270],
        [25,  18, 340],
        [26,  32, 420],
        [26, 24, 80],
        [26, 28, 120],
        [27, 62, 210],
        [27, 63, 267],
        [27, 64, 546],
        [27, 65, 126],
        [27, 76, 150],
        [27, 77, 220],
        [27, 78, 462],
        [28, 79, 236],
        [28, 80, 90],
        [28, 81, 99],
        [29, 82, 136],
        [29, 83, 16],
        [29, 84, 200],
        [29, 85, 110],
        [29, 86, 145],
        [29, 97, 139],
        [30, 94,  154],
        [30, 92,  123],
        [31, 93,  321],
        [31, 94,  152],
        [32, 95,  136],
        [32, 96,  178],
        [32, 97,  189],
        [32, 98,  154],
        [32, 99,  199],
        [32, 100, 231],
        [32, 112, 426],
        [32, 124,  154],
        [32, 125,  123],
        [33, 136,  321],
        [33, 134,  152],
        [33, 135,  136],
        [33, 126,  178],
        [34, 127,  189],
        [35, 128,  154],
        [36, 129,  199],
        [36, 100, 231],
        [36, 116, 426],
        [37, 117,  154],
        [37, 27,  123],
        [37, 37,  321],
        [38, 34,  152],
        [38, 35,  136],
        [38, 66,  178],
        [39, 67,  189],
        [39, 68,  154],
        [39, 99,  199],
        [39, 132, 231],
        [39, 119, 426],
        [40, 132, 126],
        [40, 104, 120],
        [40, 105, 150],
        [40, 106, 126],
        [40, 107, 230],
        [40, 108, 121],
        [40, 109, 323],
        [40, 110, 204],
        [41, 131, 126],
        [41, 132, 120],
        [41, 133, 150],
        [41, 134, 126],
        [41, 135, 230],
        [42, 91, 121],
        [42, 92, 323],
        [42, 93, 204],
        [43, 42, 126],
        [43, 43, 120],
        [44, 44, 150],
        [44, 45, 126],
        [45, 71, 230],
        [45, 72, 121],
        [45, 73, 325],
        [45, 74, 104],
        [46, 75, 226],
        [46, 76, 320],
        [46, 77, 450],
        [46, 91, 226],
        [47, 92, 330],
        [47, 93, 421],
        [47, 94, 363],
        [48, 121, 224],
        [49, 124, 166],
        [49, 136, 123],
        [49, 52, 170],
        [49, 73, 136],
        [49, 84, 330],
        [49, 84, 131],
        [49, 95, 325],
        [49, 16, 205],
        [50, 57, 182],
        [50, 58, 250],
        [50, 28, 120],
        [50, 129, 160],
        [51, 34, 217],
        [51, 35, 102],
        [51, 36, 182],
        [51, 37, 216],
        [51, 38, 108],
        [51, 12, 120],
        [51, 13, 510],
        [52, 1, 150],
        [52, 2, 187],
        [52, 3, 310],
        [52, 4, 160],
        [53, 13, 150],
        [53, 14, 250],
        [53, 16, 120],
        [53, 17, 280],
        [53, 18, 240],
        [53, 20, 105],
        [53, 21, 182],
        [53, 22, 510],
        [53, 23, 120],
        [54, 24, 185],
        [54, 25, 110],
        [54, 31, 140],
        [55, 32, 160],
        [55, 86, 220],
        [55, 87, 500],
        [56, 98, 160],
        [56, 99, 220],
        [56, 100, 150],
        [56, 101, 187],
        [56, 102, 212],
        [57, 31, 115],
        [57, 32, 136],
        [58, 33, 90],
        [58, 34, 123],
        [58, 35, 342],
        [59, 45, 22],
        [59, 46, 46],
        [59, 47, 75],
        [59, 15, 205],
        [59, 34, 101],
        [60, 23, 156],
        [60, 25, 290],
        [60, 24, 102],
        
        ]


# idUtilizador, idAlbum
tableFavoritoAlbum = [
        [1, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 12],
        [4, 1],
        [5, 3],
        [6, 1],
        [7, 2],
        [8, 3],
        [9, 4],
        [10, 5],
        [10, 6],
        [11, 6],
        [12, 6],
        [12, 7],
        [12, 8],
        [13, 2],
        [14, 3],
        [15, 7],
        [16, 8],
        [17, 9],
        [18, 11],
        [19, 8],
        [20, 9],
        [21, 11],
        [22, 10],
        [23, 10],
        [23, 1],
        [24, 2],
        [24, 3],
        [25, 4],
        [26, 2],
        [27, 6],
        [27, 7],
        [27, 9],
        [28, 11],
        [29, 10],
        [29, 3],
        [30, 1],
        [30, 4],
        [30, 11],
        ]

# idUtilizador, idMusica, data -> AUMENTAR ISTO! SÓ DEPOIS DE FAZZER OS UTILIZADORES TODOS!
tableFavoritoMusica =  [
        [2, 10, "'15-03-2020'"],
        [1, 33, "'02-04-2020'"],
        [1, 34, "'02-04-2020'"],
        [1, 35, "'23-03-2020'"],
        [3, 129, "'23-03-2020'"],
        [3, 125, "'25-03-2020'"],
        [3, 126, "'25-03-2020'"],
        [3, 134, "'25-03-2020'"],
        [4, 5, "'26-03-2020'"],
        [4, 6, "'28-03-2020'"],
        [5, 7, "'28-03-2020'"],
        [6, 8, "'29-03-2020'"],
        [6, 12, "'29-03-2020'"],
        [6, 34, "'29-03-2020'"],
        [7, 5, "'31-03-2020'"],
        [8, 33, "'01-04-2020'"],
        [8, 24, "'01-04-2020'"],
        [9, 5, "'01-04-2020'"],
        [11, 10, "'02-04-2020'"],
        [11, 33, "'02-04-2020'"],
        [12, 34, "'02-04-2020'"],
        [13, 35, "'22-04-2020'"],
        [13, 6, "'02-04-2020'"],
        [14, 7, "'02-04-2020'"],
        [15, 7, "'02-04-2020'"],
        [15, 5, "'02-04-2020'"],
        [16, 6, "'02-04-2020'"],
        [17, 7, "'02-04-2020'"],
        [17, 8, "'02-04-2020'"],
        [18, 5, "'03-04-2020'"],
        [18, 36, "'03-04-2020'"],
        [19, 5, "'03-04-2020'"],
        [20, 27, "'03-04-2020'"],
        [21, 22, "'03-04-2020'"],
        [22, 12, "'03-04-2020'"],
        
        [22, 15, "'03-04-2020'"],
        [23, 31, "'03-04-2020'"],
        [24, 33, "'03-04-2020'"],
        [25, 32, "'04-04-2020'"],
        [26, 1, "'04-04-2020'"],
        [26, 6, "'04-04-2020'"],
        [27, 3, "'04-04-2020'"],
        [27, 5, "'04-04-2020'"],
        [28, 21, "'04-04-2020'"],
        [28, 27, "'04-04-2020'"],
        [28, 14, "'04-04-2020'"],
        [29, 14, "'04-04-2020'"],
        [30, 15, "'04-04-2020'"],
        [30, 5, "'04-04-2020'"],
        [30, 33, "'04-04-2020'"],
        [30, 34, "'04-04-2020'"],
        [30, 35, "'04-04-2020'"],
        ]

#idUtilizador, idPlaylist -> AUMENTAR ISTO! SÓ DEPOIS DE FAZER UTILIZADORES E PLAYLISTS TODAS
tableFavoritoPlaylist = [
        [3, 4],
        [2, 3],
        [1, 2],
        [4, 1],
        [4, 3],
        [5, 3],
        [6, 2],
        [7, 1],
        [7, 2],
        [8, 3],
        [9, 1],
        [10, 1],
        [10, 2],
        [11, 2],
        [12, 1],
        [12, 3],
        [13, 3],
        [14, 2],
        [15, 1],
        [16, 3],
        [17, 2],
        [18, 1],
        [18, 2],
        [19, 3],
        [20, 1],
        [22, 1],
        [23, 2],
        [24, 2],
        [25, 2],
        [26, 3],
        [27, 1],
        [28, 1],
        [30, 1],
        [30, 2],
        [30, 3],
        ]

# idUtilizador, idPlaylist -> AUMENTAR ISTO! SÓ DEPOIS DE FAZER UTILIZADORES E PLAYLISTS TODAS
tableColabora = [
        [1, 3],
        [3, 3],
        ]


# idUtilizador, idSessao  -> AUMENTAR ISTO! SÓ DEPOIS DE FAZER OS UTILIZADORES TODOS!
tableUtilizadorSessao = [
        [1, 1],
        [2, 2],
        [2, 4],
        [3, 3],
        [3, 31],
        [1, 4],
        [1, 5],
        [1, 3],       
        [4, 6],
        [4, 2],
        [5, 4],
        [6, 3],
        [6, 4],
        [7, 5],       
        [8, 6],
        [8, 7],
        [9, 6],
        [10, 2],
        [11, 7],
        [11, 10],
        [12, 21],
        [13, 13],
        [14, 28],
        [15, 13],
        [16, 14],
        [16, 23],
        [16, 24],
        [16, 25],
        [17, 26],
        [17, 27],
        [18, 28],
        [19, 29],
        [20, 11],
        [21, 14],
        [21, 13],
        [22, 14],
        [23, 15],
        [24, 23],
        [30, 1],
        [30, 2],
        [30, 4],
        ]

# idPlaylist, idMusica  -> AUMENTAR ISTO! SÓ DEPOIS DE FAZZER AS PLAYLISTS TODAS
#Para já so tmeos 3 playlists
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
        [4, 129],
        [4, 125],
        [4, 126],
        [4, 134],
        ]

# idUtilizador, idUtilizadorSeguido
tableSegue = [
        [3, 1],
        [1, 3],
        [2, 1],
        [2, 3],
        [1, 2],
        [4, 1],
        [5, 1],
        [6, 1],
        [7, 2],
        [8, 2],
        [9, 2],       
        [10, 1],
        [10, 4],
        [11, 6],
        [12, 8],
        [13, 10],
        [14, 12],     
        [15, 14],
        [16, 16],
        [17, 18],
        [18, 20],
        [19, 22],
        [20, 24],    
        [21, 26],
        [22, 30],
        [23, 30],
        [25, 1],
        [26, 2],  
        [27, 26],
        [27, 30],
        [28, 30],
        [30, 2],
        [30, 1],
        [30, 3],
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
           "MusicaEstilo" : tableMusicaEstilo,
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