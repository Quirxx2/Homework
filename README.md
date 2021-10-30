Python RSS reader
Final task for EPAM Python Training 2021.09

rss-news-reader is a command line utility that makes it easy to view RSS feeds in a readable format.

Python 3.9 required

usage: rss_reader.py [-h] [--version] [--json] [--verbose] [--limit LIMIT]
                     [--date NEWS_DATE] [--to-html FILE] [--to-pdf FILE]
                     [source ...]

Pure Python command-line RSS reader.

positional arguments:
  source            RSS URL

optional arguments:
  -h, --help        show this help message and exit
  --version         Print version info
  --json            Print result as JSON in stdout
  --verbose         Outputs verbose status messages
  --limit LIMIT     Limit news topics if this parameter provided
  --date NEWS_DATE  Save RSS in a local storage
  --to-html FILE    Convert rss feed into html and save as file
  --to-pdf FILE     Convert rss feed into pdf and save as file

Logging

When parameter is indicated, logs always are printed to console


Parsing
XML is parsed by parser, which has an additional feature to get an additional content from links, indicated as a reference to news story 

Cashing

All files are stored inside current directory. Old version with the same name will be overwritten
Cashed files have .json format. 

Following structure as an example:

{
    "title": "Feed: Yahoo News - Latest News & Headlines",
    "description": "The latest news and headlines from Yahoo! News. Get breaking news stories and in-depth coverage with videos and photos.",
    "pubDate": "Thu, 28 Oct 2021 15:36:11",
    "items": [
        {
            "id": 1,
            "title": "Cheap antidepressant shows promise treating early COVID-19",
            "pubDate": "2021-10-27T22:37:35Z",
            "image": "https://s.yimg.com/uu/api/res/1.2/4XvMxiuN0axashY4vvuQLw--~B/aD0xNjA4O3c9MjUxMDthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/ap.org/4168c825dd9423c04fb059c73db62fd8",
            "description": "",
            "link": "https://news.yahoo.com/cheap-antidepressant-shows-promise-treating-223735055.html",
            "content": "A cheap antidepressant reduced the need for hospitalization among high-risk adults with COVID-19 in a study hunting for existing drugs that could be repurposed to treat coronavirus.\nResearchers tested the pill used for depression and obsessive-compulsive disorder because it was known to reduce inflammation and looked promising in smaller studies.\nThey've shared the results with the U.S. National Institutes of Health, which publishes treatment guidelines, and they hope for a World Health Organization recommendation.\n\u201cIf WHO recommends this, you will see it widely taken up,\u201d said study co-author Dr. Edward Mills of McMaster University in Hamilton, Ontario, adding that many poor nations have the drug readily available. \u201cWe hope it will lead to a lot of lives saved.\u201d\nThe pill, called fluvoxamine, would cost $4 for a course of COVID-19 treatment. By comparison, antibody IV treatments cost about $2,000 and Merck's experimental antiviral pill for COVID-19 is about $700 per course. Some experts predict various treatments eventually will be used in combination to fight the coronavirus.\nResearchers tested the antidepressant in nearly 1,500 Brazilians recently infected with coronavirus who were at risk of severe illness because of other health problems, such as diabetes. About half took the antidepressant at home for 10 days, the rest got dummy pills. They were tracked for four weeks to see who landed in the hospital or spent extended time in an emergency room when hospitals were full.\nIn the group that took the drug, 11% needed hospitalization or an extended ER stay, compared to 16% of those on dummy pills.\nThe results, published Wednesday in the journal Lancet Global Health, were so strong that independent experts monitoring the study recommended stopping it early because the results were clear.\nQuestions remain about the best dosing, whether lower risk patients might also benefit and whether the pill should be combined with other treatments.\nThe larger project looked at eight existing drugs to see if they could work against the pandemic virus. The project is still testing a hepatitis drug, but all the others \u2014 including metformin, hydroxychloroquine and ivermectin \u2014 haven't panned out.\u00a0\nThe cheap generic and Merck's COVID-19 pill work in different ways and \u201cmay be complementary,\u201d said Dr. Paul Sax of Brigham and Women\u2019s Hospital and Harvard Medical School, who was not involved in the study. Earlier this month, Merck asked regulators in the U.S. and Europe to authorize its antiviral pill.\u00a0\n___\nThe Associated Press Health and Science Department receives support from the Howard Hughes Medical Institute\u2019s Department of Science Education. The AP is solely responsible for all content.\n",
            "links": []
        },
        {
            "id": 2,
            "title": "Police say Brian Laundrie was likely already dead when they confused him for his mother",
            "pubDate": "2021-10-28T17:04:21Z",
            "image": "https://s.yimg.com/uu/api/res/1.2/5iqR1kRc1iPSVqfmTL95XA--~B/aD0xMDIwO3c9MTUyODthcHBpZD15dGFjaHlvbg--/https://media.zenfs.com/en/nbc_news_122/b28373812ffe262a3064398f2302c32f",
            "description": "",
            "link": "https://news.yahoo.com/police-brian-laundrie-likely-already-170421572.html",
            "content": "Brian Laundrie may have already been dead when police confused his mother for him and assumed he was home during surveillance of the residence, officials said Thursday.\nPolice in North Port, Florida, admitted earlier this week that even though investigators had trained cameras on the Laundrie residence, they weren't as aware of his comings and goings as they thought.\nLaundrie left his family's home in his Mustang on Sept. 13. When the car returned on Sept. 15, police thought Laundrie went inside the residence. But the person driving the mustang was his mother, Roberta, who was wearing a baseball cap and is kind of \"built similarly,\" North Port Police spokesperson Josh Taylor told WINK News in Fort Myers.\nThe report led to questions about how the investigation might have gone differently, and if taxpayers' dollars were subsequently wasted in what became a weekslong search for Laundrie, named a person of interest in his fianc\u00e9e, Gabby Petito's disappearance.\nIn a statement shared with NBC News Thursday, Taylor said that \"this misidentification did not have a big impact on costs and the investigation.\"\n\"Other than confusion, it likely changed nothing. There is a very good possibility that Brian was already deceased,\" he said. \"He still needed to be found.\"\n\"We just wanted people to better understand why we thought we knew Brian was in his home. It was a direct result of a lack of cooperation from the family early on in this investigation,\" Taylor added.\nWhen asked if investigators believe Roberta purposefully disguised herself to look like Brian, Taylor said: \"I don\u2019t have any info on that being the case.\"\nPolice realized their mistake when the family reported on Sept. 17 that Laundrie was missing, according to police.\nAs authorities looked for Laundrie, 23, focusing largely on the vast Carlton Reserve, a nationwide search was also ongoing for Petito, 22.\nHer body was found Sept. 19 at the Spread Creek Dispersed Camping Area in the Bridger-Teton National Forest in Wyoming. Petito had been dead for at least three weeks, and her death was ruled a homicide by \"manual strangulation,\" the coroner said.\nLaundrie was never charged in Petito's death, but he was named a person of interest in her disappearance. Authorities also issued an arrest warrant for him after they said he had used Petito's debit card without permission.\nHuman remains found in Florida's Carlton Reserve last Wednesday were confirmed to be Laundrie's after a review of dental records, officials said Thursday. His parents helped lead the FBI and North Port police to the Myakkahatchee Creek Environmental Park, a part of Carlton Reserve.\nAccording to the FBI, the remains were found alongside personal items belonging to Laundrie, such as a backpack and a notebook. The contents of those items have not been disclosed.\nThe remains have been sent to an anthropologist \"for further evaluation\" after autopsy results came back inconclusive, the family's attorney, Steven Bertolino, said late last week.\n\"No manner or cause of death was determined,\" he said in a statement to NBC News.\nAmid conspiracies on social media that the remains do not actually belong to Laundrie, police released a statement from the medical examiner's office in Sarasota.\n\"The identity of the remains found at the Carlton Reserve on Oct. 20 was confirmed by comparison to known dental records of Brian Laundrie,\" according to the statement.\n\"No DNA analysis has yet been performed on the remains,\" officials said. Samples will be submitted for DNA testing once the medical examiner's office completes its report.\nBertolino on Monday said he was not given a timeline for when the anthropologist will conclude the evaluation of Laundrie's remains.\nPetito and Laundrie left for their cross-country road trip from Blue Point, New York, in early July in a 2012 Ford Transit van. The couple chronicled their trip on their Instagram accounts and YouTube under the moniker Nomadic Statik. Petito stopped communicating with her family in late August.\nThe case continues to generate enormous public interest, but it has also raised questions about the unequal media and law enforcement attention given to missing white women compared to missing people of color.\n",
            "links": []
        }

Testing

Script tested manually
