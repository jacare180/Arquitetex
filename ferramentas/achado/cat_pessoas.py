# Cada resposta: "Nome exibido" ou "Nome exibido=Título na Wikipedia pt" ou "Nome=@en:Título en".
# Grafias extras depois de "|", separadas por ";".
C = {}
C["ach-001"] = dict(pergunta="Um arquiteto ou arquiteta brasileira modernista", tipo="pessoa",
 verifica=r"(arquitet|architect).*(brasil|brazil)|(brasil|brazil).*(arquitet|architect)", lead=True, respostas="""
Oscar Niemeyer|Niemeyer
Lúcio Costa|Lucio Costa
Lina Bo Bardi|Lina
Affonso Eduardo Reidy|Reidy;Affonso Reidy
Paulo Mendes da Rocha
João Batista Vilanova Artigas|Vilanova Artigas;Artigas
Rino Levi
Gregori Warchavchik|Warchavchik
Roberto Burle Marx|Burle Marx
Lelé=João Filgueiras Lima|João Filgueiras Lima;João da Gama Filgueiras Lima
Sérgio Bernardes
Joaquim Guedes
Carlos Leão
Jorge Machado Moreira|Jorge Moreira
Marcelo Roberto=Irmãos Roberto|Irmãos Roberto;MMM Roberto
Henrique Mindlin
Oswaldo Bratke
Lina Bo Bardi
Ruy Ohtake|Ohtake
Lygia Fernandes
Eduardo Kneese de Mello
Carmen Portinho
Giancarlo Palanti
Franz Heep
David Libeskind (arquiteto brasileiro)=David Libeskind (arquiteto)|David Libeskind
Ícaro de Castro Mello
Paulo Antunes Ribeiro
Acácio Gil Borsoi|Borsoi
Delfim Amorim
Severiano Mário Porto|Severiano Porto
Abelardo de Souza
Fábio Penteado
Sérgio Rodrigues
Zanine Caldas=José Zanine Caldas|José Zanine Caldas
Álvaro Vital Brazil|Vital Brazil
Attilio Corrêa Lima
Ernani Vasconcellos
Flávio de Carvalho
Luiz Nunes
Francisco Bolonha
Milton Roberto
Marcos Konder Netto
Glauco Campello
Carlos Millan
Decio Tozzi
Eduardo de Almeida
""")
C["ach-002"] = dict(pergunta="Uma arquiteta mulher, de qualquer época", tipo="pessoa",
 verifica=r"arquitet|architect", lead=True, respostas="""
Zaha Hadid|Zaha
Lina Bo Bardi|Lina
Kazuyo Sejima|Sejima
Denise Scott Brown
Eileen Gray
Charlotte Perriand|Perriand
Jeanne Gang
Anne Lacaton=@en:Anne Lacaton|Lacaton
Yvonne Farrell=@en:Yvonne Farrell
Shelley McNamara=@en:Shelley McNamara
Carme Pinós=@en:Carme Pinós|Carme Pinos
Elizabeth Diller=@en:Elizabeth Diller|Liz Diller
Odile Decq=@en:Odile Decq
Amanda Levete=@en:Amanda Levete
Benedetta Tagliabue=@en:Benedetta Tagliabue
Gae Aulenti
Lilly Reich
Margarete Schütte-Lihotzky|Schütte-Lihotzky;Grete Lihotzky
Julia Morgan
Marion Mahony Griffin|Marion Mahony
Jane Drew=@en:Jane Drew
Alison Smithson
Ray Eames
Carmen Portinho
Lygia Fernandes
Tatiana Bilbao=@en:Tatiana Bilbao
Frida Escobedo=@en:Frida Escobedo
Mariam Kamara=@en:Mariam Kamara
Marina Tabassum=@en:Marina Tabassum
Lu Wenyu=@en:Lu Wenyu
Itsuko Hasegawa=@en:Itsuko Hasegawa
Sophia Hayden=@en:Sophia Hayden
Norma Merrick Sklarek=@en:Norma Merrick Sklarek|Norma Sklarek
Natalie de Blois=@en:Natalie de Blois
Anne Tyng=@en:Anne Tyng
Lotte Stam-Beese=@en:Lotte Stam-Beese
Ada Louise Huxtable
Carla Juaçaba=@en:Carla Juaçaba
Gabriela Carrillo=@en:Gabriela Carrillo
Neri Oxman
Momoyo Kaijima=@en:Momoyo Kaijima
Sheila O'Donnell=@en:O'Donnell + Tuomey
Patty Hopkins=@en:Patty Hopkins
Eva Jiřičná=@en:Eva Jiřičná|Eva Jiricna
""")
C["ach-002"]["fixar"] = {"Neri Oxman": "Arquivo"}
C["ach-003"] = dict(pergunta="Um vencedor do Prêmio Pritzker", tipo="pessoa",
 verifica=r"pritzker", lead=False, respostas="""
Philip Johnson
Luis Barragán|Barragan;Barragán
James Stirling
Kevin Roche
I. M. Pei|Ieoh Ming Pei;Pei
Richard Meier
Hans Hollein
Gottfried Böhm|Bohm;Böhm
Kenzo Tange|Tange
Gordon Bunshaft|Bunshaft
Oscar Niemeyer|Niemeyer
Frank Gehry|Gehry
Aldo Rossi
Robert Venturi|Venturi
Álvaro Siza|Siza;Alvaro Siza Vieira
Fumihiko Maki|Maki
Tadao Ando|Ando
Christian de Portzamparc|Portzamparc
Renzo Piano|Piano
Norman Foster|Foster
Rem Koolhaas|Koolhaas
Jacques Herzog=Herzog & de Meuron|Herzog;Herzog e de Meuron;Pierre de Meuron;de Meuron
Glenn Murcutt|Murcutt
Jørn Utzon|Jorn Utzon;Utzon
Zaha Hadid|Zaha;Hadid
Thom Mayne|Mayne
Paulo Mendes da Rocha
Richard Rogers|Rogers
Jean Nouvel|Nouvel
Peter Zumthor|Zumthor
Kazuyo Sejima=SANAA|Sejima;Ryue Nishizawa;Nishizawa;SANAA
Eduardo Souto de Moura|Souto de Moura;Souto Moura
Wang Shu
Toyo Ito|Ito
Shigeru Ban
Frei Otto
Alejandro Aravena|Aravena
RCR Arquitectes=@en:RCR Arquitectes|RCR;Rafael Aranda;Carme Pigem;Ramon Vilalta
Balkrishna Doshi|Doshi;B. V. Doshi
Arata Isozaki|Isozaki
Yvonne Farrell=@en:Grafton Architects|Grafton Architects;Shelley McNamara;Grafton
Anne Lacaton=@en:Lacaton & Vassal|Lacaton e Vassal;Jean-Philippe Vassal;Lacaton & Vassal
Francis Kéré|Kere;Kéré;Diébédo Francis Kéré
David Chipperfield|Chipperfield
Riken Yamamoto=@en:Riken Yamamoto|Yamamoto
Liu Jiakun=@en:Liu Jiakun
""")
C["ach-004"] = dict(pergunta="Um arquiteto japonês", tipo="pessoa",
 verifica=r"(arquitet|architect).{0,300}(japon|japan)|(japon|japan).{0,300}(arquitet|architect)", lead=True, respostas="""
Tadao Ando|Ando
Kenzo Tange|Tange
Toyo Ito|Ito
Kengo Kuma|Kuma
Shigeru Ban
Kazuyo Sejima|Sejima
Ryue Nishizawa|Nishizawa
Fumihiko Maki|Maki
Arata Isozaki|Isozaki
Kisho Kurokawa|Kurokawa
Sou Fujimoto|Fujimoto
Junya Ishigami|Ishigami
Kunio Maekawa|Maekawa
Kiyonori Kikutake|Kikutake
Riken Yamamoto=@en:Riken Yamamoto|Yamamoto
Itsuko Hasegawa=@en:Itsuko Hasegawa|Hasegawa
Kazuo Shinohara=@en:Kazuo Shinohara|Shinohara
Yoshio Taniguchi=@en:Yoshio Taniguchi|Taniguchi
Kenzo Tange
Togo Murano=@en:Togo Murano|Murano
Sutemi Horiguchi=@en:Sutemi Horiguchi
Tetsuo Furuichi=@en:Tetsuo Furuichi
Hiroshi Hara=@en:Hiroshi Hara
Atelier Bow-Wow=@en:Atelier Bow-Wow|Bow-Wow
Momoyo Kaijima=@en:Momoyo Kaijima
Akihisa Hirata=@en:Akihisa Hirata
Terunobu Fujimori=@en:Terunobu Fujimori|Fujimori
Tadao Ando
Shin Takamatsu=@en:Shin Takamatsu
Kazuhiro Kojima=@en:Kazuhiro Kojima
Hitoshi Abe=@en:Hitoshi Abe
Jun Aoki=@en:Jun Aoki|Aoki
Takaharu Tezuka=@en:Tezuka Architects|Tezuka
Kiyoshi Sey Takeyama=@en:Kiyoshi Sey Takeyama
Junzo Yoshimura=@en:Junzo Yoshimura|Yoshimura
""")
C["ach-005"] = dict(pergunta="Um arquiteto latino-americano que não seja brasileiro", tipo="pessoa",
 verifica=r"arquitect|arquitet|architect", lead=True, respostas="""
Luis Barragán|Barragan;Barragán
Alejandro Aravena|Aravena
Clorindo Testa|Testa
César Pelli|Pelli;Cesar Pelli
Carlos Raúl Villanueva|Villanueva
Eladio Dieste|Dieste
Rogelio Salmona|Salmona
Félix Candela|Candela
Juan O'Gorman|O'Gorman
Mario Pani|Pani
Ricardo Legorreta|Legorreta
Teodoro González de León=@en:Teodoro González de León|Teodoro Gonzalez de Leon
Pedro Ramírez Vázquez|Ramirez Vazquez
Mathias Goeritz|Goeritz
Augusto H. Álvarez=@en:Augusto H. Álvarez
Tatiana Bilbao=@en:Tatiana Bilbao
Frida Escobedo=@en:Frida Escobedo
Smiljan Radić=@en:Smiljan Radić|Smiljan Radic;Radic
Mathias Klotz=@en:Mathias Klotz|Klotz
Emilio Duhart=@en:Emilio Duhart|Duhart
Amancio Williams|Williams
Mario Roberto Álvarez=@en:Mario Roberto Álvarez
Alejandro Bustillo=@en:Alejandro Bustillo|Bustillo
Antonio Bonet=@en:Antonio Bonet Castellana|Bonet
Mario Palanti|Palanti
Julio Vilamajó=@en:Julio Vilamajó|Vilamajo
Fernando Romero=@en:Fernando Romero
Alberto Kalach=@en:Alberto Kalach|Kalach
Enrique Norten=@en:Enrique Norten|Norten
Agustín Hernández Navarro=@en:Agustín Hernández Navarro
Juan Sordo Madaleno=@en:Juan Sordo Madaleno
Giancarlo Mazzanti=@en:Giancarlo Mazzanti|Mazzanti
Simón Vélez=@en:Simón Vélez|Simon Velez
Fruto Vivas=@en:Fruto Vivas
Rafael Viñoly|Vinoly;Viñoly
Emilio Ambasz=@en:Emilio Ambasz|Ambasz
Solano Benítez=@en:Solano Benítez|Solano Benitez
Gabriela Carrillo=@en:Gabriela Carrillo
Mauricio Rocha=@en:Mauricio Rocha
Ricardo Porro=@en:Ricardo Porro
Abraham Zabludovsky=@en:Abraham Zabludovsky
""")
C["ach-005"]["fixar"] = {"Smiljan Radić": "Arquivo", "Abraham Zabludovsky": "Arquivo"}
C["ach-006"] = dict(pergunta="Um pintor impressionista", tipo="pessoa", verifica=r"impression", lead=True, respostas="""
Claude Monet|Monet
Pierre-Auguste Renoir|Renoir
Edgar Degas|Degas
Camille Pissarro|Pissarro
Alfred Sisley|Sisley
Berthe Morisot|Morisot
Mary Cassatt|Cassatt
Gustave Caillebotte|Caillebotte
Édouard Manet|Manet;Edouard Manet
Frédéric Bazille|Bazille
Armand Guillaumin|Guillaumin
Eva Gonzalès=@en:Eva Gonzalès
Marie Bracquemond=@en:Marie Bracquemond
Paul Cézanne|Cézanne;Cezanne
Childe Hassam=@en:Childe Hassam|Hassam
Joaquín Sorolla|Sorolla
Max Liebermann|Liebermann
Lovis Corinth=@en:Lovis Corinth
John Singer Sargent|Sargent
Giuseppe De Nittis=@en:Giuseppe De Nittis
Federico Zandomeneghi=@en:Federico Zandomeneghi
Gustave Loiseau=@en:Gustave Loiseau
Henri Lebasque=@en:Henri Lebasque
Theodore Robinson=@en:Theodore Robinson
William Merritt Chase=@en:William Merritt Chase
Eliseu Visconti|Visconti
Georgina de Albuquerque
Tom Thomson=@en:Tom Thomson
Philip Wilson Steer=@en:Philip Wilson Steer
Walter Sickert=@en:Walter Sickert
Kitty Kielland=@en:Kitty Kielland
Konstantin Korovin=@en:Konstantin Korovin
Alfred Stevens=@en:Alfred Stevens (painter)
Stanislas Lépine=@en:Stanislas Lépine
Jean-Louis Forain=@en:Jean-Louis Forain
Jean-Baptiste Armand Guillaumin=Armand Guillaumin
Albert Lebourg=@en:Albert Lebourg
Henri Rouart=@en:Henri Rouart
""")
C["ach-007"] = dict(pergunta="Um artista do Renascimento", tipo="pessoa", verifica=r"renasc|renaissance", lead=True, respostas="""
Leonardo da Vinci|Leonardo;Da Vinci
Michelangelo|Michelangelo Buonarroti;Miguel Ângelo
Rafael Sanzio|Rafael;Raffaello;Raphael
Sandro Botticelli|Botticelli
Donatello
Ticiano|Tiziano;Titian;Tiziano Vecellio
Albrecht Dürer|Dürer;Durer
Jan van Eyck|Van Eyck
Giotto di Bondone|Giotto
Filippo Brunelleschi|Brunelleschi
Masaccio
Piero della Francesca
Fra Angelico
Andrea Mantegna|Mantegna
Giovanni Bellini|Bellini
Lorenzo Ghiberti|Ghiberti
Paolo Uccello|Uccello
Andrea del Verrocchio|Verrocchio
Domenico Ghirlandaio|Ghirlandaio
Hieronymus Bosch|Bosch
Pieter Bruegel, o Velho|Bruegel;Brueghel;Pieter Bruegel
Hans Holbein, o Jovem|Holbein;Hans Holbein
Giorgione
Tintoretto
Paolo Veronese|Veronese
Correggio
Andrea del Sarto
Fra Filippo Lippi|Filippo Lippi
Perugino|Pietro Perugino
Benvenuto Cellini|Cellini
Lucas Cranach, o Velho|Cranach;Lucas Cranach
Rogier van der Weyden|Van der Weyden
Hans Memling|Memling
Antonello da Messina
Leon Battista Alberti|Alberti
Donato Bramante|Bramante
Andrea Palladio|Palladio
Giorgio Vasari|Vasari
Parmigianino
Bronzino|Agnolo Bronzino
Sofonisba Anguissola|Anguissola
Pontormo|Jacopo Pontormo
Luca della Robbia|Della Robbia
Jacopo della Quercia
Pinturicchio
Carlo Crivelli|Crivelli
""")
C["ach-008"] = dict(pergunta="Um artista brasileiro do século 20", tipo="pessoa",
 verifica=r"(artista|pintor|pintora|escultor|escultora|gravador|gravadora|fotograf|painter|sculptor|artist).{0,400}(brasil|brazil)|(brasil|brazil).{0,400}(artista|pintor|pintora|escultor|escultora|gravador|painter|sculptor|artist)", lead=True, respostas="""
Tarsila do Amaral|Tarsila
Candido Portinari|Portinari;Cândido Portinari
Di Cavalcanti|Emiliano Di Cavalcanti
Anita Malfatti|Malfatti
Hélio Oiticica|Oiticica;Helio Oiticica
Lygia Clark
Lygia Pape
Alfredo Volpi|Volpi
Tomie Ohtake
Victor Brecheret|Brecheret
Ismael Nery
Vicente do Rego Monteiro|Rego Monteiro
Lasar Segall|Segall
Cícero Dias
Alberto da Veiga Guignard|Guignard
Djanira|Djanira da Motta e Silva
Iberê Camargo|Ibere Camargo
Arthur Bispo do Rosário|Bispo do Rosário
Amilcar de Castro
Franz Weissmann|Weissmann
Mira Schendel
Sergio Camargo
Abraham Palatnik|Palatnik
Waldemar Cordeiro|Cordeiro
Geraldo de Barros
Lothar Charoux
Ivan Serpa|Serpa
Rubens Gerchman|Gerchman
Antonio Dias
Cildo Meireles|Cildo
Anna Maria Maiolino|Maiolino
Wesley Duke Lee
Nelson Leirner|Leirner
Carybé
Rubem Valentim
Mestre Vitalino|Vitalino
Heitor dos Prazeres
José Pancetti|Pancetti
Flávio de Carvalho
Maria Martins
Oswaldo Goeldi|Goeldi
Lívio Abramo
Burle Marx=Roberto Burle Marx|Roberto Burle Marx
Athos Bulcão
Aldemir Martins
Tunga
Leonilson|José Leonilson
Regina Silveira
Beatriz Milhazes|Milhazes
Vik Muniz
Sebastião Salgado
Rosângela Rennó
Adriana Varejão|Varejão
Ernesto Neto
Arthur Barrio
Artur Barrio
Claudio Tozzi|Cláudio Tozzi
Siron Franco
Glauco Rodrigues
Genaro de Carvalho
Manabu Mabe|Mabe
Samson Flexor
Milton Dacosta|Dacosta
Maria Leontina
Hércules Barsotti
Willys de Castro
Judith Lauand
""")
C["ach-009"] = dict(pergunta="Um escultor, de qualquer época", tipo="pessoa", verifica=r"escult|sculpt", lead=True, respostas="""
Michelangelo|Michelangelo Buonarroti
Auguste Rodin|Rodin
Gian Lorenzo Bernini|Bernini
Donatello
Aleijadinho|Antônio Francisco Lisboa
Constantin Brâncuși|Brancusi;Brâncuși
Alberto Giacometti|Giacometti
Henry Moore
Camille Claudel
Louise Bourgeois
Fídias|Phidias
Praxíteles|Praxiteles
Policleto|Polykleitos
Míron|Myron
Antonio Canova|Canova
Bertel Thorvaldsen|Thorvaldsen
Jean-Antoine Houdon|Houdon
Benvenuto Cellini|Cellini
Lorenzo Ghiberti|Ghiberti
Victor Brecheret|Brecheret
Amilcar de Castro
Franz Weissmann|Weissmann
Sergio Camargo
Maria Martins
Alexander Calder|Calder
Barbara Hepworth|Hepworth
Jean Arp|Hans Arp
Naum Gabo|Gabo
Antoine Pevsner|Pevsner
Umberto Boccioni|Boccioni
Richard Serra|Serra
Anish Kapoor|Kapoor
Jeff Koons|Koons
Louise Nevelson|Nevelson
Isamu Noguchi|Noguchi
Eduardo Chillida|Chillida
Jorge Oteiza|Oteiza
Ron Mueck|Mueck
Antony Gormley|Gormley
Niki de Saint Phalle
Jean Tinguely|Tinguely
Claes Oldenburg|Oldenburg
Donald Judd|Judd
Carl Andre
Paul Landowski|Landowski
Frédéric Auguste Bartholdi|Bartholdi
Aristide Maillol|Maillol
Edgar Degas|Degas
Pablo Picasso|Picasso
Ernesto de Fiori
Bruno Giorgi|Giorgi
Alfredo Ceschiatti|Ceschiatti
Rodolfo Bernardelli|Bernardelli
Mestre Valentim|Valentim da Fonseca e Silva
Kiki Smith
Yayoi Kusama|Kusama
""")
C["ach-010"] = dict(pergunta="Um designer de cadeira famosa", tipo="pessoa", verifica=r"cadeira|chair|poltrona|mobili|furniture", lead=False, respostas="""
Charles Eames|Eames;Charles e Ray Eames
Ray Eames
Ludwig Mies van der Rohe|Mies;Mies van der Rohe
Marcel Breuer|Breuer
Le Corbusier|Corbusier
Charlotte Perriand|Perriand
Arne Jacobsen|Jacobsen
Hans Wegner|Wegner;Hans J. Wegner
Eero Saarinen|Saarinen
Harry Bertoia|Bertoia
Verner Panton|Panton
Michael Thonet|Thonet
Alvar Aalto|Aalto
Gerrit Rietveld|Rietveld
Charles Rennie Mackintosh|Mackintosh
Josef Hoffmann|Hoffmann
Frank Lloyd Wright
Eileen Gray
Philippe Starck|Starck
Gio Ponti|Ponti
Joe Colombo=@en:Joe Colombo
Eero Aarnio=@en:Eero Aarnio|Aarnio
Pierre Paulin=@en:Pierre Paulin
Poul Kjærholm=@en:Poul Kjærholm
Finn Juhl=@en:Finn Juhl
Børge Mogensen=@en:Børge Mogensen
George Nelson=@en:George Nelson (designer)
Isamu Noguchi|Noguchi
Jean Prouvé|Prouvé;Prouve
Frank Gehry|Gehry
Ron Arad=@en:Ron Arad
Jasper Morrison=@en:Jasper Morrison
Irmãos Campana|Campana;Fernando Campana;Humberto Campana;Estúdio Campana
Sergio Rodrigues=@en:Sérgio Rodrigues (designer)|Sérgio Rodrigues
Lina Bo Bardi|Lina
Joaquim Tenreiro|Tenreiro
Zanine Caldas=José Zanine Caldas
Oscar Niemeyer|Niemeyer
Jorge Zalszupin=@en:Jorge Zalszupin|Zalszupin
Geraldo de Barros
Paulo Mendes da Rocha
Hella Jongerius=@en:Hella Jongerius
Konstantin Grcic=@en:Konstantin Grcic|Grcic
Patricia Urquiola=@en:Patricia Urquiola|Urquiola
Gaetano Pesce=@en:Gaetano Pesce|Pesce
Ettore Sottsass|Sottsass
Achille Castiglioni|Castiglioni
Vico Magistretti=@en:Vico Magistretti
Warren Platner=@en:Warren Platner
""")
C["ach-011"] = dict(pergunta="Um paisagista", tipo="pessoa", verifica=r"paisag|landscape|jardin|garden", lead=True, respostas="""
Roberto Burle Marx|Burle Marx
Frederick Law Olmsted|Olmsted
André Le Nôtre|Le Nôtre;Le Notre
Capability Brown=Lancelot Brown|Lancelot Brown;Brown
Gertrude Jekyll|Jekyll
Piet Oudolf=@en:Piet Oudolf|Oudolf
Glaziou=Auguste François Marie Glaziou|Auguste Glaziou
Mestre Valentim
Rosa Kliass
Fernando Chacel
Humphry Repton=@en:Humphry Repton|Repton
William Kent
Calvert Vaux=@en:Calvert Vaux
Dan Kiley=@en:Dan Kiley
Lawrence Halprin=@en:Lawrence Halprin
Thomas Church=@en:Thomas Church (landscape architect)
Ian McHarg=@en:Ian McHarg
Kathryn Gustafson=@en:Kathryn Gustafson
Gilles Clément=@en:Gilles Clément
Martha Schwartz=@en:Martha Schwartz
Peter Walker=@en:Peter Walker (landscape architect)
Michel Desvigne=@en:Michel Desvigne
Geoffrey Jellicoe=@en:Geoffrey Jellicoe
Jens Jensen=@en:Jens Jensen (landscape architect)
Beatrix Farrand=@en:Beatrix Farrand
Mirei Shigemori=@en:Mirei Shigemori
Luis Barragán|Barragán
Jean-Claude Nicolas Forestier=@en:Jean-Claude Nicolas Forestier|Forestier
Carlos Thays=@en:Charles Thays|Thays
Paul Villon
Adolphe Alphand=@en:Jean-Charles Alphand|Alphand
Fernando Magalhães Chacel
Burle Marx
Raul Penteado
Waldemar Cordeiro
Sakate Mitsuo
""")
C["ach-012"] = dict(pergunta="Um fotógrafo de arquitetura ou de arte", tipo="pessoa", verifica=r"fotograf|photograph", lead=True, respostas="""
Julius Shulman=@en:Julius Shulman|Shulman
Ezra Stoller=@en:Ezra Stoller|Stoller
Iwan Baan=@en:Iwan Baan
Hélène Binet=@en:Hélène Binet
Marcel Gautherot|Gautherot
Nelson Kon
Thomaz Farkas|Farkas
Geraldo de Barros
German Lorca
Cristiano Mascaro|Mascaro
Bernd e Hilla Becher=Bernd e Hilla Becher|Becher;Bernd Becher;Hilla Becher
Andreas Gursky|Gursky
Candida Höfer=@en:Candida Höfer
Thomas Struth=@en:Thomas Struth|Struth
Hiroshi Sugimoto|Sugimoto
Lucien Hervé=@en:Lucien Hervé
Eugène Atget|Atget
Berenice Abbott|Abbott
Walker Evans
Ansel Adams
Man Ray
Henri Cartier-Bresson|Cartier-Bresson
Robert Mapplethorpe|Mapplethorpe
Cindy Sherman
Sebastião Salgado|Salgado
Claudia Andujar|Andujar
Pierre Verger|Verger
Marc Ferrez|Ferrez
Augusto Malta
Militão Augusto de Azevedo|Militão
Vik Muniz
Rosângela Rennó
Miguel Rio Branco
Bob Wolfenson
Leonardo Finotti
Hedrich Blessing=@en:Hedrich Blessing
Edward Steichen|Steichen
Alfred Stieglitz|Stieglitz
Diane Arbus|Arbus
Annie Leibovitz|Leibovitz
Vivian Maier
Wolfgang Tillmans=@en:Wolfgang Tillmans
Jeff Wall=@en:Jeff Wall
Thomas Ruff=@en:Thomas Ruff
""")
C["ach-010"]["fixar"] = {"Charles Eames": "Cartão-postal", "Ludwig Mies van der Rohe": "Cartão-postal", "Le Corbusier": "Cartão-postal",
  "Marcel Breuer": "Cartão-postal", "Oscar Niemeyer": "Repertório", "Lina Bo Bardi": "Repertório", "Frank Lloyd Wright": "Repertório", "Warren Platner": "Arquivo"}
C["ach-006"]["fixar"] = {"Walter Sickert": "Arquivo", "Childe Hassam": "Repertório"}
