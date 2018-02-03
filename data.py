CONST_IDEAS = 0
CONST_METHODOLOGY = 1
CONST_MONEY = 2
CONST_ACT = 3
CONST_PROGRESS = 4
CONST_SOLVE_PROBLEM = 5
CONST_MISTAKES = 6
CONST_PRODUCTIVITY = 7
CONST_CUSTOMERS = 9
CONST_MANAGE_BUSINESS = 9

def Topics():
    topics = [
        {
            'id': CONST_IDEAS,
            'name':'Ideas',
            'lessons':
                [
                    {
                        'lesson':'Necessity is the mother of invention (Platon)',
                        'source':'The Cathedral and the Bazaar by Eric S. Raymond'
                    },
                    {
                        'lesson':'Often, the most striking and innovative solutions come from realizing that your concept of the problem was wrong',
                        'source':'The Cathedral and the Bazaar by Eric S. Raymond'
                    }
                ]
        },
        {
            'id': CONST_METHODOLOGY,
            'name':'Methodology',
            'lessons':
                [
                    {
                        'lesson':'Plan to throw one away; you will, anyhow.',
                        'source':'The Mythical Man-Month by Fred Brooks'
                    },
                    {
                        'lesson':'Don\'t hesitate to throw away superannuated features when you can do it. Antoine de Saint-Exupery : Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away.',
                        'source':'The Cathedral and the Bazaar by Eric Raymond'
                    },
                    {
                        'lesson':'Smart data structures and dumb code works a lot better than the other way around',
                        'source':'The Cathedral and the Bazaar by Eric Raymond'
                    }
                ]
        },
        {
            'id': CONST_MONEY,
            'name':'Money',
            'lessons':
                [
                    {
                        'lesson':'Ne fais jamais pour de l\'argent ce que tu ne ferais pas gratuitement',
                        'source':'Jean reviere - YouTube'
                    },
                    {
                        'lesson':'Buy assets that will generate the cash flow',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    },
                    {
                        'lesson':'Quand il s\'agit d\'argent, la plupart des gens veulent eviter les risques et se sentir securises. Ce n\'est donc pas la passion qui les mene, c\'est la peur. les gens ressentent la peur de ne pas avoir d\'argent. Au lieu d\'affronter cette peur, ils reagissent avant meme de reflechir. Ils reagissent de facon emotive',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    },
                    {
                        'lesson':'Il faut surmonter la peur de perdre de l\'argent. Le fait de gagner suit habituellement celui de perdre. Aucun riche (avant de le devenir) n\'a jamais perdu de l\'argent',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    }
                ]
        },
        {
            'id': CONST_ACT,
            'name':'Act',
            'lessons':
                [
                    {
                        'lesson':'Si vous etes du genre a attendre que le  bon  evenement se produise, il se peut que vous ayez a attendre longtemps encore. J\'ai observe des individus jouer au jeu CASHFLOW et se plaindre que les cartes des  bonnes  occasions ne se retrouvent jamais entre leurs mains. Ils se contentent donc de rester assis a la table. D\'un autre cote, j\'ai vu des individus tirer la carte de la bonne  occasion, et ne pas avoir assez d\'argent pour la saisir . Ils se plaignent ensuite qu\'ils auraient pu sortir de la  foire d\'empoigne  s\'ils avaient eu assez d\'argent . Ils restent donc assis la eux aussi. J\'ai meme observe des individus tirer une carte de  formidable  occasion et la lire a haute voix sans meme se rendre compte que c\'est vraiment une fantastique occasion. Ils ont de l\'argent, c\'est le bon moment, ils ont la bonne carte, mais ils sont incapables de voir cette occasion qui leur pend au bout du nez. La majorite des individus ne connaissent qu\'une seule solution : travailler dur, economiser et emprunter. ',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    },
                    {
                        'lesson':'Le moment est toujours mauvais. Les feux rouges de la vie ne passeront jamais au vert en meme temps. Si c\'est important pour vous et que vous voulez le faire  un jour ou l\'autre , faites-le aujourd\'hui et corrigez le tir chemin faisant',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'Demander pardon, pas la permission. Lancez-vous et justifiez-vous apres. Les gens rejettent des choses sur une base emotionnelle qu\'ils peuvent apprendre a accepter une fois le fait accompli. Si les degats potentiels sont limites ou reversibles, ne laissez pas aux autres l\'occasion de dire non. La plupart sont prompts a vous arreter avant que vous ayez commence, mais hesitants a se mettre en travers de votre chemin une fois que vous etes lance. Apprenez a devenir un fauteur de trouble et a vous excuser quand vous vous plantez pour de bon.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'Ce que nous avons le plus peur de faire est ce que nous avons le plus besoin de faire. Ce que nous craignons le plus de faire est generalement ce que nous avons le plus besoin de faire. La reussite d\'une personne dans la vie se mesure en general au nombre de conversations delicates ou desagreables qu\'elle est prete a avoir.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    }
                ]
        },
        {
            'id': CONST_PROGRESS,
            'name':'Progress',
            'lessons':
                [
                    {
                        'lesson':'Beaucoup trop de personnes pensent a ce qu\'ils pourraient repliquer plutot que d\'ecouter afin d\'absorber les nouvelles idees et les possibilites de l\'avenir. Ils argumentent au lieu de poser des questions',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    },
                    {
                        'lesson':'Les incredules critiquent et les gagnants analysent. La critique nous aveugle tandis que l\'analyse nous ouvre les yeux . L\'analyse permet aux gagnants de constater que les critiques sont aveugles et de voir des occasions que tous les autres ratent le plus souvent . Et le fait de decouvrir ce que les gens ratent est la cle de toute reussite',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    },
                    {
                        'lesson':'Si tu apprends les lecons de la vie, tu t\'en sortiras fort bien. Sinon la vie continuera tout simplement de te bousculer. Les gens optent pour 2 solutions : se laisser bousculer par la vie OU se facher et en bousculent d\'autres. Ils ne se rendent pas compte que c\'est la vie qui les pousse et les bouscule.',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    },
                    {
                        'lesson':'Quand vous savez que vous etes ignorant sur un sujet precis, instruisez-vous.J\'ai decouvert que beaucoup de gens utilisent l\'arrogance pour tenter de cacher leur propre ignorance.',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    },
                    {
                        'lesson':'Ne pas se perfectionner sur ses capacites a faire un bon hamburger, mais aussi etendre connaissances pour apprendre a le vendre',
                        'source':'Rich Dad Poor Dad by Robert Kiyosaki and Sharon Lechter'
                    }
                ]
        },
        {
            'id': CONST_SOLVE_PROBLEM,
            'name':'Solve a problem',
            'lessons':
                [
                    {
                        'lesson':'Quand vous vous heurtez a un mur, quand vous avez du mal a reflechir au-dela de la prochaine etape, c\'est souvent le bon moment de vous demandez non pas si vous apportez la bonne reponse mais si vous posez la bonne question',
                        'source':'The Cathedral and the Bazaar by Eric Raymond'
                    }
                ]
        },
        {
            'id': CONST_MISTAKES,
            'name':'Mistakes',
            'lessons':
                [
                    {
                        'lesson':'Il y a deux types d\'erreurs : les erreurs d\'ambition et les erreurs de paresse. Les premieres resultent de la decision d\'agir - de faire quelque chose. Elles sont generalement le fruit d\'une information imparfaite : il est impossible de disposer de toutes les donnees avant de se lancer. Ces erreurs sont a encourager. La chance sourit aux audacieux. Les deuxiemes resultent d\'un acte de paresse - ne pas faire quelque chose : par peur, nous refusons d\'agir pour faire evoluer une situation negative alors que nous disposons de toutes les donnees. C\'est ainsi que les experiences d\'apprentissage deviennent des punitions, des relations amoureuses bancales de mauvais mariages et de mauvais choix professionnels des condamnations a la prison a vie.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    }
                ]
        },
        {
            'id': CONST_PRODUCTIVITY,
            'name':'Productivity',
            'lessons':
                [
                    {
                        'lesson':'**Etre efficace**, c\'est faire des choses qui vous rapprochent de vos objectifs. **Etre performant**, c\'est accomplir une tache donnee (qu\'elle soit importante ou non) de la maniere la plus economique possible. Example : la personne qui verifie ses courriels trente fois par jour et met au point un systeme elabore de regles de dossiers et des techniques sophistiquees pour garantir que chacune de ces broutilles se deplace aussi vite que possible. Voici deux truismes a ne pas oublier : 1) bien faire une chose sans importance ne la rend pas importante ; 2) ce n\'est pas parce qu\'une tache exige beaucoup de temps qu\'elle est importante. => Ce que vous faites est infiniment plus important que comment vous le faites. La performance est inutile si on ne l\'applique pas aux bonnes choses.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'Etre deborde est souvent tout aussi sterile que de ne rien faire, et c\'est beaucoup plus desagreable. Etre selectif - en faire moins - est le chemin du productif. Concentrez-vous sur les quelques elements importants et laissez tomber le reste.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    }
                ]
        },
        {
            'id': CONST_CUSTOMERS,
            'name':'Customers',
            'lessons':
                [
                    {
                        'lesson':'Davantage de clients ne signifie pas necessairement davantage de revenus. Example d\'application de la loi de Pareto avec 2 questions : 1. Quelles sont les 20 % de sources qui sont cause de 80 % de mes problemes et de mon insatisfaction ? 2. Quelles sont les 20 % de sources qui produisent 80 % de mes resultats souhaites et de mon bonheur ? L\'objectif est d\'identifier vos inefficacites en vue de les eliminer et de trouver vos points forts pour pouvoir les multiplier. Sur plus de 120 clients grossistes, cinq generaient 95 % des recettes. Je passais 98 % de mon temps a courir apres les autres, les cinq mentionnes ci-dessus me passant regulierement des commandes sans coups de telephone de relance, entreprises de persuasion ou de seduction. En d\'autres termes, je travaillais parce que j\'avais l\'impression qu\'il fallait que je fasse quelque chose de 9 h a 19 h. Je n\'avais pas pris conscience que travailler de 9 h a 19 h n\'est pas l\'objectif ; c\'est seulement la structure que la plupart des gens utilisent, que ce soit necessaire ou non. Augmenter le nombre de vos clients n\'est pas l\'objectif car cela se traduit souvent par 90 % de frais generaux en plus et une miserable augmentation de revenus de 1 a 3 %. J\'ai travaille mes clients les plus rentables, et me suis attache a augmenter la taille et la frequence de leurs commandes. Resultat final ? Au lieu de courir apres 120 clients et d\'essayer de les calmer, je me suis retrouve a receptionner de grosses commandes de huit clients, sans le moindre coup de telephone implorant ou le moindre courriel de harangue',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'Tous les clients ne sont pas egaux. Je connais des  vendeurs qui n\'acceptent ni les virements Western Union ni les cheques. Ce a quoi certains ne manqueront pas de retorquer le client :  Mais vous perdez 10 a 15 % de vos ventes !  Ce a quoi le vendeur repond :  Oui, c\'est vrai mais j\'evite aussi les 10 a 15 % de clients qui creent 40 % des couts et devorent 40 % de mon temps.  Les prospects les plus exigeants et les plus pingres... font les clients les plus exigeants et les plus pingres. Les exclure du jeu est a la fois une bonne decision d\'art de vivre et une bonne decision financiere. Les clients qui n\'aiment pas payer et qui adorent que l\'on s\'occupe d\'eux sont les champions des coups de telephone interminables',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    }
                ]
        },
        {
            'id': CONST_MANAGE_BUSINESS,
            'name':'Manage a business',
            'lessons':
                [
                    {
                        'lesson':'Redefinir les regles et les processus avant d\'ajouter des personnes. Avoir recours a quelqu\'un pour exploiter un processus precis demultiplie la production; Avoir recours a quelqu\'un comme solution a un mauvais processus demultiplie les problemes.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'Automatiser des processus via la technologie. "La premiere regle de toute technologie utilisee dans une entreprise est que l\'automatisation appliquee a une operation efficace amplifiera l\'efficacite. La deuxieme est que l\'automatisation appliquee a une operation inefficace amplifiera l\'inefficacite" Bill Gates',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'Creer la demande est difficile. Y repondre est beaucoup plus facile. Trouvez un marche - definissez vos clients - et ensuite seulement trouvez ou creez un produit pour eux. Soyez membre de votre marche cible et ne vous lancez pas dans des speculations hasardeuses sur ce dont les autres pourraient avoir besoin ou envie d\'acheter.  Si tout le monde est votre client, personne n\'est votre client , a-t-on coutume de dire. Si vous avez dans l\'idee de creer un produit pour les amoureux de chiens ou de voitures, arretez-vous tout de suite. Faire de la publicite pour un marche aussi important coute cher et vous etes en concurrence avec trop de produits et trop d\'information gratuite. Si vous vous concentrez sur le dressage de bergers allemands ou un produit de restauration pour les vieilles Ford, en revanche, le marche et la concurrence se reduisent, et il est moins couteux de toucher vos clients et plus facile de pratiquer des prix eleves.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'Automatiser, deleguer. Le probleme, c\'est que les memes entrepreneurs ne savent pas quand ni comment quitter la scene pour passer du stade artisanal au stade industriel. Par industriel , je veux dire une architecture capable de traiter 10 000 commandes par semaine aussi facilement qu\'elle peut en traiter dix par semaine. Cela suppose de minimiser vos responsabilites de prise de decision, ce qui vous permet d\'etre plus libre de votre temps tout en mettant en place les conditions necessaires pour multiplier vos revenus par deux ou trois sans augmenter le nombre de vos heures de travail.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    },
                    {
                        'lesson':'L\'objectif financier d\'une start-up devrait etre simple : realiser des benefices le plus rapidement possible avec le minimum d\'efforts. Pas plus de clients, pas plus de chiffre d\'affaires, pas plus de bureaux ou de collaborateurs. Plus de benefices.',
                        'source':'The 4-Hour Workweek by Timothy Ferriss'
                    }
                ]
        }
    ]

    return topics
