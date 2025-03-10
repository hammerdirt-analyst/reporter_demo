openning = {
    "English": "The state of things",
    "French": "L'état des choses",
    "German": "Der Stand der Dinge",
    "Italian": "Lo stato delle cose"
}

secondopenning = {
    "English": "Making sense of litter counts at the beach. A practical application of citizen science: Decision Support.",
    "French": "Donner un sens aux comptages de déchets sur la plage. Une application pratique de la science citoyenne : aide à la décision.",
    "German": "Sinnvolle Auswertung von Müllzählungen am Strand. Eine praktische Anwendung der Bürgerwissenschaft: Entscheidungsunterstützung.",
    "Italian": "Dare un senso ai conteggi dei rifiuti in spiaggia. Un'applicazione pratica della scienza civica: supporto alle decisioni."
}

tasks = {
    "English": {
        "Evaluate a sample / get a forecast": "Evaluate / Forecast",
        "Make a report": "Make a report",
        "Chat with the references": "Chat with the references"
    },
    "French": {
        "Evaluate a sample / get a forecast": "Évaluer / Prévoir",
        "Make a report": "Faire un rapport",
        "Chat with the references": "Discuter avec les références"
    },
    "German": {
        "Evaluate a sample / get a forecast": "Bewerten / Vorhersagen",
        "Make a report": "Einen Bericht erstellen",
        "Chat with the references": "Mit den Referenzen chatten"
    },
    "Italian": {
        "Evaluate a sample / get a forecast": "Valutare  / previsione",
        "Make a report": "Fare un rapporto",
        "Chat with the references": "Chattare con i riferimenti"
    }
}

chat_rag = {
    "English": "Hi, I am here to answer questions about beach litter monitoring, protocols, and applications.",
    "French": "Bonjour, je suis ici pour répondre aux questions sur la surveillance des déchets sur la plage, les protocoles et les applications.",
    "German": "Hallo, ich bin hier, um Fragen zur Überwachung von Strandmüll, Protokollen und Anwendungen zu beantworten.",
    "Italian": "Ciao, sono qui per rispondere a domande sul monitoraggio dei rifiuti in spiaggia, protocolli e applicazioni."
}

# Evaluate a sample
sampleExplanation = {
    "English": (
        "This function allows you to evaluate a beach litter inventory or get a forecast using either the surrounding"
        " land-use as a reference, one of several cantons, or one of several lakes.\n\n**Evaluate a sample:**\nIf you"
        " have a properly formatted .csv file you can upload the beach litter counts directly. If you have counts for just a"
        " few items you can enter them in a list with the chat agent. Supply the object description, the number of objects"
        " the length in meters of beach or mountain trail, for example: _plastic bottles, 2, 50 m_.\n\n**Forecast**\nIf you want"
        " to forecast or predict quantities of specific items just enter the object description or the code. Recall that you"
        " can search for the code in the sidebar."
    ),
    "French": (
        "Cette fonction vous permet d'évaluer un inventaire de déchets sur la plage ou d'obtenir une prévision en utilisant"
        " soit l'utilisation des terres environnantes comme référence, soit l'un des plusieurs cantons, soit l'un des plusieurs"
        " lacs.\n\n**Évaluer un échantillon :**\nSi vous avez un fichier .csv correctement formaté, vous pouvez télécharger"
        " directement les comptages de déchets sur la plage. Si vous avez des comptages pour seulement quelques objets, vous"
        " pouvez les entrer dans une liste avec l'agent de chat. Fournissez la description de l'objet, le nombre d'objets,"
        " la longueur en mètres de la plage ou du sentier de montagne, par exemple : _bouteilles en plastique, 2, 50 m_."
        "\n\n**Prévision**\nSi vous souhaitez prévoir ou prédire les quantités d'articles spécifiques, entrez simplement la"
        " description de l'objet ou le code. N'oubliez pas que vous pouvez rechercher le code dans la barre latérale."
    ),
    "German": (
        "Diese Funktion ermöglicht es Ihnen, ein Strandmüllinventar zu bewerten oder eine Vorhersage zu erhalten, indem Sie"
        " entweder die umgebende Landnutzung als Referenz, einen von mehreren Kantonen oder einen von mehreren Seen verwenden."
        "\n\n**Eine Probe auswerten:**\nWenn Sie eine korrekt formatierte .csv-Datei haben, können Sie die Strandmüllzählungen"
        " direkt hochladen. Wenn Sie Zählungen für nur wenige Gegenstände haben, können Sie diese in einer Liste mit dem Chat-Agenten"
        " eingeben. Geben Sie die Objektbeschreibung, die Anzahl der Objekte und die Länge in Metern des Strandes oder Wanderweges"
        " an, z.B.: _Plastikflaschen, 2, 50 m_.\n\n**Vorhersage**\nWenn Sie die Mengen bestimmter Artikel vorhersagen oder"
        " prognostizieren möchten, geben Sie einfach die Objektbeschreibung oder den Code ein. Denken Sie daran, dass Sie den Code"
        " in der Seitenleiste suchen können."
    ),
    "Italian": (
        "Questa funzione consente di valutare un inventario dei rifiuti sulla spiaggia o di ottenere una previsione utilizzando"
        " l'uso del suolo circostante come riferimento, uno dei vari cantoni o uno dei vari laghi.\n\n**Valutare un campione:**\nSe"
        " si dispone di un file .csv correttamente formattato, è possibile caricare direttamente i conteggi dei rifiuti sulla spiaggia."
        " Se si dispone di conteggi per pochi oggetti, è possibile inserirli in un elenco con l'agente di chat. Fornire la descrizione"
        " dell'oggetto, il numero di oggetti, la lunghezza in metri della spiaggia o del sentiero di montagna, ad esempio: _bottiglie di"
        " plastica, 2, 50 m_.\n\n**Previsione**\nSe si desidera prevedere o predire le quantità di articoli specifici, è sufficiente"
        " inserire la descrizione dell'oggetto o il codice. Ricorda che puoi cercare il codice nella barra laterale."
    )
}

properlyFormattedCsv = {
    "English": (
        "The .csv file should have the following columns: 'code', 'quantity', 'length'. Your data is not stored. If you want"
        " to enter your data into the reference values you need to have a login. For the moment no logins are being issued"
        " because there is no budget for ongoing operations."
    ),
    "French": (
        "Le fichier .csv doit contenir les colonnes suivantes : 'code', 'quantité', 'longueur'. Vos données ne sont pas stockées."
        " Si vous souhaitez entrer vos données dans les valeurs de référence, vous devez avoir un identifiant. Pour le moment,"
        " aucun identifiant n'est délivré car il n'y a pas de budget pour les opérations en cours."
    ),
    "German": (
        "Die .csv-Datei sollte die folgenden Spalten enthalten: 'Code', 'Menge', 'Länge'. Ihre Daten werden nicht gespeichert."
        " Wenn Sie Ihre Daten in die Referenzwerte eingeben möchten, benötigen Sie einen Login. Derzeit werden keine Logins"
        " ausgegeben, da kein Budget für laufende Operationen vorhanden ist."
    ),
    "Italian": (
        "Il file .csv deve contenere le seguenti colonne: 'codice', 'quantità', 'lunghezza'. I tuoi dati non vengono memorizzati."
        " Se desideri inserire i tuoi dati nei valori di riferimento, è necessario disporre di un login. Al momento non vengono"
        " rilasciati login perché non è disponibile un budget per le operazioni in corso."
    )
}


sampleTable = (
    "*Properly formatted .csv file*\n\n"
    "| code | quantity | length |\n"
    "|------|----------|--------|\n"
    "| G27   | 2        | 50     |\n"
    "| G28   | 3        | 50     |\n"
)

report_assistant_text = {
    "English": (
        "This digital assistant helps put local environmental observations in the context of regional and national strategies."
        " Plastics and other trash in the environment are a recognized nuisance. In Switzerland the population is agreed:"
        " we prefer less trash and plastics in the environment. Here you can make reports and chat with them or chat with"
        " reference documents on the subject of beach litter."
    ),
    "French": (
        "Cet assistant numérique aide à mettre les observations environnementales locales dans le contexte des stratégies régionales"
        " et nationales. Les plastiques et autres déchets dans l'environnement sont une nuisance reconnue. En Suisse, la population"
        " s'accorde à dire : nous préférons moins de déchets et de plastiques dans l'environnement. Ici, vous pouvez faire des rapports,"
        " discuter avec eux ou discuter avec des documents de référence sur le sujet des déchets sur les plages."
    ),
    "German": (
        "Dieser digitale Assistent hilft, lokale Umweltbeobachtungen in den Kontext regionaler und nationaler Strategien zu stellen."
        " Kunststoffe und anderer Müll in der Umwelt sind ein anerkanntes Ärgernis. In der Schweiz ist sich die Bevölkerung einig:"
        " Wir bevorzugen weniger Müll und Kunststoffe in der Umwelt. Hier können Sie Berichte erstellen und mit ihnen chatten oder mit"
        " Referenzdokumenten zum Thema Strandmüll chatten."
    ),
    "Italian": (
        "Questo assistente digitale aiuta a contestualizzare le osservazioni ambientali locali nel quadro delle strategie regionali e nazionali."
        " Le plastiche e altri rifiuti nell'ambiente sono un fastidio riconosciuto. In Svizzera la popolazione concorda:"
        " preferiamo meno rifiuti e plastiche nell'ambiente. Qui puoi fare rapporti e chattare con essi o chattare con"
        " documenti di riferimento sull'argomento dei rifiuti in spiaggia."
    )
}


what_this_reprorting_method_does = {
    "English": (
        "**What this reporting method does**\n\n"
        "This reporting method aggregates the data according to administrative boundaries or geographic boundaries."
        " Stakeholders can quickly review and compare survey results between cities, cantons, lakes or rivers."
        " Comparing results in this way can help identify locations that are"
        " in need of investment, or locations that are performing well in relation to their peers.\n**In the first case we"
        " identify need in the second case we identify best practices**."
    ),
    "French": (
        "**Ce que fait cette méthode de reporting**\n\n"
        "Cette méthode de reporting agrège les données selon les limites administratives ou géographiques."
        " Les parties prenantes peuvent rapidement examiner et comparer les résultats des enquêtes entre les villes, les cantons,"
        " les lacs ou les rivières. Comparer les résultats de cette manière peut aider à identifier les lieux qui"
        " ont besoin d'investissements ou ceux qui se comportent bien par rapport à leurs pairs.\n**Dans le premier cas, nous"
        " identifions les besoins, dans le second cas, nous identifions les meilleures pratiques**."
    ),
    "German": (
        "**Was diese Berichtsmethode bewirkt**\n\n"
        "Diese Berichtsmethode aggregiert die Daten nach administrativen oder geografischen Grenzen."
        " Interessengruppen können schnell Umfrageergebnisse zwischen Städten, Kantonen, Seen oder Flüssen überprüfen und vergleichen."
        " Ein solcher Vergleich kann helfen, Standorte zu identifizieren, die Investitionen benötigen, oder Standorte, die im Vergleich"
        " zu ihren Mitbewerbern gut abschneiden.\n**Im ersten Fall identifizieren wir Bedarf, im zweiten Fall identifizieren wir Best Practices**."
    ),
    "Italian": (
        "**Cosa fa questo metodo di reporting**\n\n"
        "Questo metodo di reporting aggrega i dati in base ai confini amministrativi o geografici."
        " Gli stakeholder possono rivedere e confrontare rapidamente i risultati delle indagini tra città, cantoni, laghi o fiumi."
        " Confrontare i risultati in questo modo può aiutare a identificare le località che"
        " hanno bisogno di investimenti o quelle che si comportano bene rispetto ai loro pari.\n**Nel primo caso identifichiamo i bisogni,"
        " nel secondo caso identifichiamo le migliori pratiche**."
    )
}


valuing_citizen_science = {
    "English": (
        "**Valuing Citizen Science**\n\nCitizen science is a valuable tool for collecting data at scale. Volunteer observations"
        " are used in ornithological and botanical studies regularly. The practical application of the data"
        " collected in citizen science projects remains limited, usually it is used for messaging or awareness campaigns."
        " However, their is a practical application of the data for monitoring and assessments. Specifically in the case"
        " of litter on the beach or in the forest. At the municipal level sampling will help identify the problem areas and"
        " can help identify the source. At the cantonal level the aggregated results will identify the most common objects"
        " that are found. Making it easy to identify priorities both geographically and in terms of object abundance."
        " \n\nThis data also serves as a field report for decision support packages that are addressing plastics in the environment."
        " Litter counts add context to the top down approach of monitoring or estimating the amount of plastic in the environment."
        " Furthermore, with this prototype these results are now easy to verify and can be used to assess progress towards a reduction goal."
        " **In this way participatory science can be used to raise awareness, advance research, inform policy and monitor progress**."
    ),
    "French": (
        "**Valoriser la science citoyenne**\n\nLa science citoyenne est un outil précieux pour collecter des données à grande échelle."
        " Les observations des volontaires sont régulièrement utilisées dans les études ornithologiques et botaniques. L'application pratique"
        " des données collectées dans les projets de science citoyenne reste limitée, elles sont généralement utilisées pour des campagnes"
        " de sensibilisation ou de communication. Cependant, il existe une application pratique des données pour la surveillance et les évaluations."
        " Notamment dans le cas des déchets sur la plage ou dans la forêt. Au niveau municipal, l'échantillonnage aidera à identifier les zones"
        " problématiques et peut aider à identifier la source. Au niveau cantonal, les résultats agrégés identifieront les objets les plus courants"
        " trouvés. Facilitant ainsi l'identification des priorités à la fois géographiquement et en termes d'abondance d'objets."
        " \n\nCes données servent également de rapport de terrain pour les outils d'aide à la décision qui traitent des plastiques dans l'environnement."
        " Les comptages de déchets ajoutent du contexte à l'approche descendante de surveillance ou d'estimation de la quantité de plastique dans l'environnement."
        " De plus, avec ce prototype, ces résultats sont désormais faciles à vérifier et peuvent être utilisés pour évaluer les progrès vers un objectif de réduction."
        " **Ainsi, la science participative peut être utilisée pour sensibiliser, faire avancer la recherche, informer les politiques et surveiller les progrès**."
    ),
    "German": (
        "**Den Wert der Citizen Science erkennen**\n\nCitizen Science ist ein wertvolles Instrument zur großflächigen Datenerhebung. Freiwilligenbeobachtungen"
        " werden regelmäßig in ornithologischen und botanischen Studien verwendet. Die praktische Anwendung der in Citizen-Science-Projekten"
        " gesammelten Daten bleibt jedoch begrenzt und wird in der Regel für Kommunikations- oder Sensibilisierungskampagnen verwendet."
        " Es gibt jedoch eine praktische Anwendung der Daten für Überwachung und Bewertungen. Insbesondere im Fall von Müll am Strand oder im Wald."
        " Auf kommunaler Ebene hilft die Stichprobenentnahme, Problemgebiete zu identifizieren und kann helfen, die Quelle zu ermitteln."
        " Auf kantonaler Ebene werden die aggregierten Ergebnisse die am häufigsten gefundenen Objekte identifizieren."
        " Dies erleichtert die Identifizierung von Prioritäten sowohl geografisch als auch hinsichtlich der Häufigkeit von Objekten."
        " \n\nDiese Daten dienen auch als Feldbereicht für Entscheidungsunterstützungspakete, die sich mit Kunststoffen in der Umwelt befassen."
        " Müllzählungen liefern Kontext für den Top-Down-Ansatz zur Überwachung oder Schätzung der Kunststoffmenge in der Umwelt."
        " Darüber hinaus sind diese Ergebnisse mit diesem Prototyp nun leicht zu überprüfen und können verwendet werden, um den Fortschritt"
        " in Richtung eines Reduktionsziels zu bewerten. **Auf diese Weise kann die partizipative Wissenschaft genutzt werden,"
        " um das Bewusstsein zu schärfen, die Forschung voranzutreiben, die Politik zu informieren und den Fortschritt zu überwachen**."
    ),
    "Italian": (
        "**Valorizzare la scienza civica**\n\nLa scienza civica è uno strumento prezioso per raccogliere dati su larga scala. Le osservazioni dei volontari"
        " vengono utilizzate regolarmente negli studi ornitologici e botanici. L'applicazione pratica dei dati raccolti nei progetti di scienza civica"
        " rimane limitata, di solito vengono utilizzati per campagne di messaggistica o sensibilizzazione. Tuttavia, esiste un'applicazione pratica"
        " dei dati per il monitoraggio e le valutazioni. In particolare nel caso dei rifiuti in spiaggia o nel bosco. A livello municipale, il campionamento"
        " aiuterà a identificare le aree problematiche e può aiutare a identificare la fonte. A livello cantonale, i risultati aggregati identificheranno"
        " gli oggetti più comuni trovati. Facilitando così l'identificazione delle priorità sia geograficamente che in termini di abbondanza di oggetti."
        " \n\nQuesti dati fungono anche da rapporto sul campo per i pacchetti di supporto alle decisioni che affrontano le plastiche nell'ambiente."
        " I conteggi dei rifiuti aggiungono contesto all'approccio dall'alto verso il basso di monitoraggio o stima della quantità di plastica nell'ambiente."
        " Inoltre, con questo prototipo, questi risultati sono ora facili da verificare e possono essere utilizzati per valutare i progressi verso un obiettivo di riduzione."
        " **In questo modo, la scienza partecipativa può essere utilizzata per sensibilizzare, promuovere la ricerca, informare le politiche e monitorare i progressi**."
    )
}

data_info_text = {
    "English": (
        "**Where does the data come from?**\n\nThe data was collected by volunteers and experts from NGOs all over Switzerland.\n\n"
        "Collecting data is simple, go to the beach, walk along the water and count and identify the man-made objects you find.\n\n"
        "**Based on field experience**, this app is built on methodologies and insights from the following works:\n\n"
        "- [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)\n"
        "- [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)\n"
        "- [Land Use](https://www.sciencedirect.com/science/article/pii/S0269749124016257)\n"
        "- [Plastock](https://associationsauvegardeleman.github.io/plastock/)\n"
        "- [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)\n\n"
        "**Open Source and Transparent**\n\n"
        "The app's source code, data, and documentation are available for review and collaboration:\n"
        "[Explore the documentation and source code here](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).\n\n"
    ),
    "French": (
        "**D'où viennent les données ?**\n\nLes données ont été collectées par des bénévoles et des experts d'ONG de toute la Suisse.\n\n"
        "La collecte de données est simple, allez à la plage, marchez le long de l'eau et comptez et identifiez les objets fabriqués par l'homme que vous trouvez.\n\n"
        "**Basé sur l'expérience de terrain**, cette application repose sur des méthodologies et des informations issues des travaux suivants :\n\n"
        "- [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)\n"
        "- [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)\n"
        "- [Land Use](https://www.sciencedirect.com/science/article/pii/S0269749124016257)\n"
        "- [Plastock](https://associationsauvegardeleman.github.io/plastock/)\n"
        "- [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)\n\n"
        "**Open Source et Transparent**\n\n"
        "Le code source, les données et la documentation de l'application sont disponibles pour examen et collaboration :\n"
        "[Explorez la documentation et le code source ici](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).\n\n"
    ),
    "German": (
        "**Woher stammen die Daten?**\n\nDie Daten wurden von Freiwilligen und Experten von NGOs aus der ganzen Schweiz gesammelt.\n\n"
        "Die Datenerhebung ist einfach: Gehen Sie an den Strand, laufen Sie am Wasser entlang und zählen und identifizieren Sie die von Menschenhand"
        " geschaffenen Objekte, die Sie finden.\n\n**Basierend auf Felderfahrung** wurde diese App auf Methoden und Erkenntnissen aus den folgenden Arbeiten aufgebaut:\n\n"
        "- [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)\n"
        "- [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)\n"
        "- [Land Use](https://www.sciencedirect.com/science/article/pii/S0269749124016257)\n"
        "- [Plastock](https://associationsauvegardeleman.github.io/plastock/)\n"
        "- [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)\n\n"
        "**Open Source und Transparent**\n\n"
        "Der Quellcode, die Daten und die Dokumentation der App stehen für Überprüfung und Zusammenarbeit zur Verfügung:\n"
        "[Erkunden Sie die Dokumentation und den Quellcode hier](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).\n\n"
    ),
    "Italian": (
        "**Da dove provengono i dati?**\n\nI dati sono stati raccolti da volontari ed esperti di ONG in tutta la Svizzera.\n\n"
        "La raccolta dei dati è semplice: vai in spiaggia, cammina lungo l'acqua e conta e identifica gli oggetti creati dall'uomo che trovi.\n\n"
        "**Basato sull'esperienza sul campo**, questa app si basa su metodologie e intuizioni derivanti dai seguenti lavori:\n\n"
        "- [IQAASL End of Sampling 2021](https://hammerdirt-analyst.github.io/IQAASL-End-0f-Sampling-2021/)\n"
        "- [Solid Waste Team](https://hammerdirt-analyst.github.io/solid-waste-team/titlepage.html)\n"
        "- [Land Use](https://www.sciencedirect.com/science/article/pii/S0269749124016257)\n"
        "- [Plastock](https://associationsauvegardeleman.github.io/plastock/)\n"
        "- [Finding One Object](https://hammerdirt-analyst.github.io/finding-one-object/titlepage.html)\n\n"
        "**Open Source e Trasparente**\n\n"
        "Il codice sorgente, i dati e la documentazione dell'app sono disponibili per la revisione e la collaborazione:\n"
        "[Esplora la documentazione e il codice sorgente qui](https://hammerdirt-analyst.github.io/feb_2024/titlepage.html#).\n\n"
    )
}

what_would_you_like_to_do = {
    "English": "Tasks: What would you like to do?",
    "French": "Tâches : Que souhaitez-vous faire ?",
    "German": "Aufgaben: Was möchten Sie tun?",
    "Italian": "Compiti: Cosa vorresti fare?"
}

define_the_report_parameters = {

        'English': "#### Define the report parameters",
        'French': "#### Définir les paramètres du rapport",
        'German': "#### Definieren Sie die Berichtsparameter",
        'Italian': "#### Definire i parametri del rapporto"
    }


current_articles_rag = (
    "1. The guide for monitoring marine litter in European seas 2023\n"
    "2. Differentiating urban runoff marine transport\n"
    "3. EU marine litter baselines 2012 2016\n"
    "4. EU marine litter thresholds 2020\n"
    "5. EU Riverine shoreline litter monitoring\n"
    "6. Revealing the role of land use features on macrolitter distribution in Swiss freshwaters\n"
    "7. The Swiss Litter Report 2018\n\n")

labels = {
    "whats_this": {
        "English": "Some background information",
        "French": "Quelques informations générales",
        "German": "Einige Hintergrundinformationen",
        "Italian": "Alcune informazioni di base"
    },
    "canton": {
        "English": ":red[Canton]",
        "French": ":red[Canton]",
        "German": ":red[Kanton]",
        "Italian": ":red[Cantone]"
    },
    "city": {
        "English": ":red[City]",
        "French": ":red[Ville]",
        "German": ":red[Stadt]",
        "Italian": ":red[Città]"
    },
    "feature_name": {
        "English": ":red[Feature Name]",
        "French": ":red[Nom du lac/rivière]",
        "German": ":red[Merkmalsname]",
        "Italian": ":red[Nome della caratteristica]"
    },
    "l": {
        "English": "Lake",
        "French": "Lac",
        "German": "See",
        "Italian": "Lago"
    },
    "r": {
        "English": "River",
        "French": "Rivière",
        "German": "Fluss",
        "Italian": "Fiume"
    },
    "both": {
        "English": "Both",
        "French": "Les deux",
        "German": "Beide",
        "Italian": "Entrambi"
    },
    "nofilters": {
        "English": "You have not selected any filters. This will return all data.",
        "French": "Vous n'avez sélectionné aucun filtre. Cela renverra toutes les données.",
        "German": "Sie haben keine Filter ausgewählt. Dies wird alle Daten zurückgeben.",
        "Italian": "Non hai selezionato alcun filtro. Questo restituirà tutti i dati."
    },
    "start_date": {
        "English": "Start Date",
        "French": "Date de début",
        "German": "Anfangsdatum",
        "Italian": "Data di inizio"
    },
    "end_date": {
        "English": "End Date",
        "French": "Date de fin",
        "German": "Enddatum",
        "Italian": "Data di fine"
    },
    "objects": {
        "English": "Objects of Interest",
        "French": "Objets d'intérêt",
        "German": "Interessante Objekte",
        "Italian": "Oggetti di interesse"
    },
    "codegroups": {
        "English": "Code Groups",
        "French": "Groupes de codes",
        "German": "Codegruppen",
        "Italian": "Gruppi di codici"
    },
    "pieces_per_meter": {
        "English": "pieces/meter",
        "French": "pièces/mètre",
        "German": "Stücke/Meter",
        "Italian": "pezzi/metro"
    },
    'select_report_type': {
        'English': ":red[Start by defining what you want to report on.]",
        'French': ":red[Commencez par définir ce que vous souhaitez signaler.]",
        'German': ":red[Beginnen Sie damit zu definieren, was Sie melden möchten.]",
        'Italian': ":red[Inizia definendo cosa vuoi segnalare.]"
    },
    'report_type_options':{
        "English": ["Canton", "City", "Lake", "River"],
        "French": ["Canton", "Ville", "Lac", "Rivière"],
        "German": ["Kanton", "Stadt", "See", "Fluss"],
        "Italian": ["Cantone", "Città", "Lago", "Fiume"]
    },
    "select_feature_type":{
        "English": ":red[Do you want to report on lakes, rivers or both within the canton boundaries?]",
        "French": ":red[Souhaitez-vous signaler les lacs, les rivières ou les deux dans les limites du canton ?]",
        "German": ":red[Möchten Sie über Seen, Flüsse oder beides innerhalb der Kantonsgrenzen berichten?]",
        "Italian": ":red[Vuoi segnalare laghi, fiumi o entrambi entro i confini del cantone?]"
    },
    'feature_type_options':{
        "English": ["Lake", "River", "Both"],
        "French": ["Lac", "Rivière", "Les deux"],
        "German": ["See", "Fluss", "Beides"],
        "Italian": ["Lago", "Fiume", "Entrambi"]
    },
    "select_locations": {
        "English": ":red[Select up to three to compare or report on.]",
        "French": ":red[Sélectionnez jusqu'à trois pour comparer ou signaler.]",
        "German": ":red[Wählen Sie bis zu drei aus, um sie zu vergleichen oder zu melden.]",
        "Italian": ":red[Seleziona fino a tre per confrontare o segnalare.]"
    },
    "select_object_group_type":{
        "English": ":red[Select the objects you want to report on]",
        "French": ":red[Sélectionnez les objets que vous souhaitez signaler]",
        "German": ":red[Wählen Sie die Objekte aus, über die Sie berichten möchten]",
        "Italian": ":red[Seleziona gli oggetti su cui vuoi segnalare]"
    },
    "select_object_group_type_instructions":{
        "English": "Do you want to report on an object group or select specific objects? If you are comparing regions we recommend selecting specific objects or object groups.",
        "French": "Souhaitez-vous signaler un groupe d'objets ou sélectionner des objets spécifiques ? Si vous comparez des régions, nous vous recommandons de sélectionner des objets spécifiques ou des groupes d'objets.",
        "German": "Möchten Sie über eine Objektgruppe berichten oder bestimmte Objekte auswählen? Wenn Sie Regionen vergleichen, empfehlen wir, bestimmte Objekte oder Objektgruppen auszuwählen.",
        "Italian": "Vuoi segnalare un gruppo di oggetti o selezionare oggetti specifici? Se stai confrontando regioni, ti consigliamo di selezionare oggetti specifici o gruppi di oggetti."
    },
    "object_group_type_options":{
        "English": ["All", "Specific objects", "Object group"],
        "French": ["Tous", "Objets spécifiques", "Groupe d'objets"],
        "German": ["Alle", "Spezifische Objekte", "Objektgruppe"],
        "Italian": ["Tutti", "Oggetti specifici", "Gruppo di oggetti"]
    },
    "code_groupnames":{
        "English": ["All", "Specific objects", "Object group"],
        "French": ["Tous", "Objets spécifiques", "Groupe d'objets"],
        "German": ["Alle", "Spezifische Objekte", "Objektgruppe"],
        "Italian": ["Tutti", "Oggetti specifici", "Gruppo di oggetti"]
    },
    "reset_options" : {
        "English": "Reset options",
        "French": "Réinitialiser les options",
        "German": "Optionen zurücksetzen",
        "Italian": "Reimposta opzioni"
    },
    "no_rough_draft_yet" : {
        "English": "No rough draft yet",
        "French": "Pas encore de brouillon",
        "German": "Noch kein Entwurf",
        "Italian": "Nessuna bozza ancora"
    },
    "making_your_report" : {
        "English": "Making your report",
        "French": "Création de votre rapport",
        "German": "Erstellung Ihres Berichts",
        "Italian": "Creazione del tuo rapporto"
    },
    "parameters_not_set" : {
        "English": "Parameters not set",
        "French": "Paramètres non définis",
        "German": "Parameter nicht festgelegt",
        "Italian": "Parametri non impostati"
    },
    'generate_report': {
        "English": "Generate report",
        "French": "Générer un rapport",
        "German": "Bericht erstellen",
        "Italian": "Genera rapporto"
    }

}

key_to_code_description ={
    "English": "en",
    "French": "fr",
    "German": "de",
    "Italian": "it"
}
code_group_translations = {
    "English": {
        'agriculture': 'agriculture',
        'food and drink': 'food and drink',
        'infrastructure': 'infrastructure',
        'micro plastics (< 5mm)': 'micro plastics (< 5mm)',
        'packaging non food': 'packaging non food',
        'personal items': 'personal items',
        'plastic pieces': 'plastic pieces',
        'recreation': 'recreation',
        'tobacco': 'tobacco',
        'unclassified': 'unclassified',
        'waste water': 'waste water'
    },
    "French": {
        'agriculture': 'agriculture',
        'food and drink': 'alimentation et boisson',
        'infrastructure': 'infrastructure',
        'micro plastics (< 5mm)': 'microplastiques (< 5mm)',
        'packaging non food': 'emballage non alimentaire',
        'personal items': 'objets personnels',
        'plastic pieces': 'morceaux de plastique',
        'recreation': 'loisirs',
        'tobacco': 'tabac',
        'unclassified': 'non classé',
        'waste water': 'eaux usées'
    },
    "German": {
        'agriculture': 'Landwirtschaft',
        'food and drink': 'Essen und Trinken',
        'infrastructure': 'Infrastruktur',
        'micro plastics (< 5mm)': 'Mikroplastik (< 5mm)',
        'packaging non food': 'Verpackung ohne Lebensmittel',
        'personal items': 'persönliche Gegenstände',
        'plastic pieces': 'Plastikteile',
        'recreation': 'Freizeit',
        'tobacco': 'Tabak',
        'unclassified': 'nicht klassifiziert',
        'waste water': 'Abwasser'
    },
    "Italian": {
        'agriculture': 'agricoltura',
        'food and drink': 'cibo e bevande',
        'infrastructure': 'infrastruttura',
        'micro plastics (< 5mm)': 'microplastiche (< 5mm)',
        'packaging non food': 'imballaggi non alimentari',
        'personal items': 'oggetti personali',
        'plastic pieces': 'pezzi di plastica',
        'recreation': 'ricreazione',
        'tobacco': 'tabacco',
        'unclassified': 'non classificato',
        'waste water': 'acque reflue'
    }
}


agent_intro = {
    "English": (
        "Hi, I am the report assistant. The rough draft is loaded and available to me."
        " This is a demonstration, we have started to include the reference texts in a Retrieval Augmented Generation (RAG) - set up."
        " You can look up the available references in the side bar."
    ),
    "French": (
        "Bonjour, je suis l'assistant de rapport. Le brouillon est chargé et disponible pour moi."
        " Il s'agit d'une démonstration, nous avons commencé à inclure les textes de référence dans une configuration de Génération Augmentée par Récupération (RAG)."
        " Vous pouvez consulter les références disponibles dans la barre latérale."
    ),
    "German": (
        "Hallo, ich bin der Berichtsassistent. Der Entwurf ist geladen und mir zur Verfügung gestellt."
        " Dies ist eine Demonstration, wir haben begonnen, die Referenztexte in eine Retrieval Augmented Generation (RAG) - Einrichtung einzubeziehen."
        " Sie können die verfügbaren Referenzen in der Seitenleiste nachschlagen."
    ),
    "Italian": (
        "Ciao, sono l'assistente di report. La bozza è caricata e disponibile per me."
        " Questa è una dimostrazione, abbiamo iniziato a includere i testi di riferimento in una configurazione di Generazione Aumentata da Recupero (RAG)."
        " Puoi cercare i riferimenti disponibili nella barra laterale."
    )
}


chat_description = {
    "English": (
        "This is where you can explore the reference documents. The available documents are listed in the sidebar. We are"
        " adding documents every week. So check back later if you don't find what you need. If you want to chat with the survey"
        " results you need to make a report."
    ),
    "French": (
        "C'est ici que vous pouvez explorer les documents de référence. Les documents disponibles sont répertoriés dans la barre latérale."
        " Nous ajoutons des documents chaque semaine. Revenez plus tard si vous ne trouvez pas ce dont vous avez besoin. Si vous souhaitez"
        " discuter des résultats de l'enquête, vous devez faire un rapport."
    ),
    "German": (
        "Hier können Sie die Referenzdokumente erkunden. Die verfügbaren Dokumente sind in der Seitenleiste aufgeführt. Wir fügen jede Woche"
        " neue Dokumente hinzu. Schauen Sie später noch einmal vorbei, wenn Sie nicht finden, was Sie brauchen. Wenn Sie mit den Umfrageergebnissen"
        " chatten möchten, müssen Sie einen Bericht erstellen."
    ),
    "Italian": (
        "Qui puoi esplorare i documenti di riferimento. I documenti disponibili sono elencati nella barra laterale. Aggiungiamo documenti ogni settimana."
        " Quindi, controlla più tardi se non trovi ciò di cui hai bisogno. Se desideri chattare con i risultati del sondaggio, devi fare un rapporto."
    )
}


def introduction_prompt(state):
    """Prompt for the abstract generation task."""
    aprompt = (
        f"You are a research assistant in an engineering firm that assesses the levels of trash and plastics on the shoreline along lakes"
        " and rivers in switzerland. You are part of a team that is creating a decisions support document. The data for this"
        " document is a subset of the observations from volunteers that monitor plastics and trash in the environment. Your task is to write"
        " the introduction to the data analysis section.\n\nThe introduction must include the following information:\n\n"
        "1. The name of the  from the title.\n"
        "2. The date range covered by the samples\n3. The number of samples\n4. The number of survey locations\n5. The min, max mean and median sample results, in pcs/m"
        "6. The total quantity of objects found.\n7. The material composition of the objects found.\n8. The type of objects under consideration, either a list or the classification."
        " The classification or the list of codes is in the subject line. If the number of objects under consideration is greater than five list a few and refer the reader"
        " to the inventory. If the classification is given state the classification and refer the reader to the inventory for the complete list.\n\n"
        f"The results have been prepared for you here:\n\n{state['roughdraft']}\n\n!INSTRUCTIONS!\n\n1. The information you need to write this is in the title, subtitle and summary statistics sections of the report above."
        "\n2. You must reply in a professional narrative style.\n3. We do not want any general closing comments. just report the facts from the provided sections of the document.\n"
        "4. Do not categorize the document type or call it a decision support document or analysis, just go ahead and do the summary.\n5. Supply only the information requested.\n"
        f"6. Identify the objects under consideration in the first paragraph.\n\nPlease reply in the following language: {state['language']}."
    )
    return ''.join(aprompt)
def admin_prompt_cantons_lakes(state):
    aprompt = (
        f"You are a research assistant in an engineering firm that assesses the levels of trash and plastics on the shoreline along lakes"
        " and rivers in switzerland. You are part of a team that is creating a decisions support document. The data for this"
        " document is a subset of the observations from volunteers that monitor plastics and trash in the environment. Your task is to write"
        "  the administrative boundaries and results section of the report. This includes the following sections:\n\n"
        "1. administrative boundaries\n2. the named features in this report\n3. sample results by city\n4. sample results by canton\n5. sample results by feature_name\n\n"
        f"The results have been prepared for you here:\n\n{state['roughdraft']}\n\n!INSTRUCTIONS!\n\n1. Summarize the sample results by city table. Include the number of cities"
        " and name the cities where the quantity is highest and lowest. Identify the cities with the greatest number of samples and the highest pcs/m.\n"
        "2. If the table 'sample results by canton' only has one row you do not need to summarize or mention it. Otherwise include the number of cantons, the canton with the greatest number of samples"
        " the canton with the highest pcs/m and the canton with the greatest quantity.\3. If their is a 'sample results by feature_name' table"
        " include the number of features: call them lakes or rivers. The lake or river with the highest pcs/m, the lake or river with the greatest number of samples and the lake or river"
        " with the highest quantity.\n4 If their is more than one row (not including the header) in the 'sample results by feature_type' table summarize the differences otherwise do not include this section.\n"
        "\n4. You must reply in a professional narrative style.\n5. We do not want any general closing comments. just report the facts from the provided sections of the document.\n"
        "6. Do not categorize the document type or call it a decision support document or analysis, just go ahead and do the summary.\n7. Supply only the information requested.\n"
        f"\n\nPlease reply in the following language: {state['language']}."

            )
    return ''.join(aprompt)

def inventory_prompt(state):
    aprompt = (
        f"You are a research assistant in an engineering firm that assesses the levels of trash and plastics on the shoreline along lakes"
        " and rivers in switzerland. You are part of a team that is creating a decisions support document. The data for this"
        " document is a subset of the observations from volunteers that monitor plastics and trash in the environment. Your task is to write"
        " the inventory of objects section of the report. This includes the following sections:\n\n"
        "1. inventory items\n\n"
        f"The results have been prepared for you here:\n\n{state['roughdraft']}\n\n!INSTRUCTIONS!\n\n"
        "**! INSTRUCTIONS**\n\n"
        "The results have a table for inventory items for each location in the title. You will produce the following summaries:\n\n"
        "1. If their are multiple inventory tables in the report will produce a summary for each. \n\n"
        "**! the general form of the summary ! :** The summary should include the top items with regards to quantity, pcs/m and the chance of finding at least one 1 and the % of total. The top items are those"
        " items when the sum of the % of total is greater than 80%. To do this you will need to sum the values in the % of total column unitll you reach 80%. Start with the first rwo\n\n"
        "**! the order of the summaries ! :** The summaries should be in the reverse order of the inventory tables in the report. The last summary should be the combined summary (the first inventory table)."
        " If their is only one inventory table summarize it.\n\n"
        
        "You must reply in a professional narrative style. We do not want any general closing comments. Just report the facts from the inventory tables.\n"
        "6. Do not categorize the document type or call it a decision support document or analysis, just go ahead and do the summary.\n7. Supply only the information requested.\n"
        f"\n\nPlease reply in the following language: {state['language']}."

            )
    return ''.join(aprompt)

def reporter_prompt(state, context: str = " "):
    aprompt = (
                "You are helping a data scientist write a summary report of volunteer observations of objects found along",
                " lakes and rivers in Switzerland. The data is collected using the JRC/EU/OSPAR method for counting beach litter. This",
                " method is defined in the Guide for monitoring marine litter in european seas.",
                "The client has already prepared a rough draft of the report as well as a bar chart, scatter plot and map.",
                " Your task is to answer the clients questions reference these reports and the provided context. The client is preparing a decision",
                " support document and is relying on you for brief answers that can be supported by the documents provided",
                " below:\n\n",
                f"roughdraft: {state['roughdraft']}\n\n",
                "Furthermore a vectory similarity search has been conducted given the users questions and supporting references if their are any:\n\n",
                f"{context}\n\n",
                "!Instructions!\n\n"
                "1. The information you need to answer the clients questions is in the rough draft and the supporting references.\n"
                "2. You must reply in a professional narrative style.\n"
                "3. You are to discuss plastics, trash or litter in the environment, citizen-science, swiss or european policy concerning plastics and trash in the environment"
                "4. You will not cite non existent references or make up facts. You may complete the information with your own knowledge.\n"
                "5. Other topics of a violent, sexual or racial nature are not to be considered. You are to stick to the subject matter.\n",
            )
    return ''.join(aprompt)