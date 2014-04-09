import re
import SETTINGS

if __name__ == "__main__":
    sample = "Daren,\n\nI am handling CP&L and am trying to resolve this issue from February production.  CP&L shows 5,000 mmbtu on February 21, but we do not have a deal.  Were you able to find anything out about this?\n\nThanks for your help.\n\nRebecca\n---------------------- Forwarded by Rebecca Griffin/NA/Enron on 03/27/2001 04:04 PM ---------------------------\n\n\nKatherine Herrera\n03/26/2001 09:57 AM\nTo:\tRebecca Griffin/NA/Enron@Enron\ncc:\t \n\nSubject:\tRe: CP&L\n\n\n---------------------- Forwarded by Katherine Herrera/Corp/Enron on 03/26/2001 09:46 AM ---------------------------\n   \n\t  From:  Gary W Lamphier @ ECT                           03/26/2001 09:52 AM\t\n\t\t\n\n\nTo:\tDaren J Farmer/HOU/ECT@ECT\ncc:\tKatherine Herrera/Corp/Enron@ENRON \n\nSubject:\tRe: CP&L   \n\nCan we verified this gas flowed?  If it did it should have been billed on his term deal if there was one in place.  If the gas flowed and we did not invoice for it on term let me know and I will put it in.\n\n\n\nJanet H Wallis\n03/22/2001 04:53 PM\nTo:\tGary W Lamphier/HOU/ECT@ECT\ncc:\tKatherine Herrera/Corp/Enron@ENRON \nSubject:\tCP&L\n\nBob says he was not billed for a purchase he made from you at 5K  $5.16 on Feb 21st.  Will you check this out and get with\nBob A and Katherine Herrera.\n\nJW\n\n\n\n\n\n\n\n\n<Embedded StdOleLink>,You want to handle, or you want me to take a stab at it?\n\n-----Original Message----- \nFrom: Siegel, Misha \nSent: Thu 10/18/2001 12:33 PM \nTo: Dasovich, Jeff; Bourgeois-Galloway, Hilda; Parquet, David \nCc: Schwartz, Laura \nSubject: RE: Community Affairs-related Activity\n\n\n\n\nHi Jeff, \nAmong other things, Community Relations is here to help the business units drive their business!  Please forward any related materials to my attention, either via email or to the Enron building (1400 Smith St, eb1632b, Houston, TX  77002). A list of support categories would be helpful!\n\nThanks, \nMisha \n\n -----Original Message----- \nFrom:   Dasovich, Jeff  \nSent:   Thursday, October 18, 2001 11:00 AM \nTo:     Bourgeois-Galloway, Hilda; Parquet, David \nCc:     Siegel, Misha \nSubject:        RE: Community Affairs-related Activity \n\nThanks very much. \n\n -----Original Message----- \nFrom:   Bourgeois-Galloway, Hilda  \nSent:   Thursday, October 18, 2001 7:37 AM \nTo:     Dasovich, Jeff \nCc:     Siegel, Misha \nSubject:        RE: Community Affairs-related Activity \nImportance:     High \n\nHi Jeff: \n\nGot you message and I'm copying this to Misha Siegel.  Misha is the person who can help you with this. \n\nHilda \n\n -----Original Message----- \nFrom:   Dasovich, Jeff  \nSent:   Wednesday, October 17, 2001 4:36 PM \nTo:     Parquet, David; Bourgeois-Galloway, Hilda \nSubject:        FW: Community Affairs-related Activity \n\nHi Hilda: \nI got an \"out of office\" reply from Elyse that mentions that you're the contact in her absense.  Please see the note below.\n\nBest, \nJeff \n -----Original Message----- \nFrom:   Dasovich, Jeff  \nSent:   Wednesday, October 17, 2001 4:28 PM \nTo:     Kalmans, Elyse; Parquet, David \nSubject:        Community Affairs-related Activity \n\nHi Elyse: \nI work in government affairs in San Francisco.  Dave Parquet (VP, Western Origination) has been approached by a California state legislator to participate in a golf tournament, the proceeds of which will go to a children's charity (Dave, correct me if I got it wrong).  The legislator is someone who has been and will likely continue to be supportive of Dave's on-going commercial activities and Dave would like to participate.  I've been informed that this could fall under the sorts of activities that community affairs has resources for.  Is that right?  Thanks for the help.\n\nBest, \nJeff ++++++++++++++$PIRATEBOUNTY$+++++++++++++++\n\nGet your FREE daily horoscope and Unlimited\nLIVE Psychic Readings for 3 FULL DAYS. Your\nPersonal Reading is done for you and only you!\n\nClick Here:\nhttp://r1.postlite.com/?u=139&l=68&id=159916\n\n<a href=\"http://r1.postlite.com/?u=139&l=68&id=159916\"> AOL Users Click Here </a>\n\nThanks,\nPirateBounty.com\nhttp://www.piratebounty.com\n\n->>-------------------------------------------------------------<<-\nTO UNSUBSCRIBE click here:\n\nhttp://www.postlite.com/u/?l=piratebounty&e=alewis@ect.enron.com\n\n<a href=\"http://www.postlite.com/u/?l=piratebounty&e=alewis@ect.enron.com\">\nAOL users click here to unsubscribe\n</a>\n\nor...\n\nReply to this email with the word \"remove\" as the subject.\n\nThis email was sent to: alewis@ect.enron.com\n\nX-Postlite-Recipient: alewis@ect.enron.com\nX-Postlite-Userid: piratebounty\n->>-------------------------------------------------------------<<-\n"
    # Removing special characters
    sample = re.sub("[\n\t\-\*\+\$\"\\\(\)]+", " ", sample)
    sample = re.sub("<<", " ", sample)
    # Removing tags
    sample = re.sub('(<[^<]+>|<<[^<<]+>>)', "", sample)
    # Removing time
    sample = re.sub('([\d]+:\d\d) (AM|PM)', "", sample)
    # Removing date
    sample = re.sub('([\d]+/[\d]+/[\d]+)', "", sample)
    sample = re.sub('([\d]+\.[\d]+\.[\d]+)', "", sample)
    sample = re.sub('(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday){0,1},? (January|February|March|April|May|June|July|August|September|October|November|December){0,} [\d]*,? ?[\d]*', " ", sample)
    # Removing labels
    sample = re.sub('(From:|To:|Sent:|Cc:|cc:|Bcc:|RE:|Re:|FWD:|Subject:|Original Message)', "", sample)
    # Removing urls
    sample = re.sub('https?:\/\/.*? ', '', sample)
    # Removing punctuations
    sample = re.sub('[;\,\?\.\:\!]', " ", sample)
    # Removing numbers
    sample = re.sub('(0|1|2|3|4|5|6|7|8|9){1,}', "", sample)
    # Removing email address
    
    # Removing rest
    sample = re.sub('[/@]', " ", sample)
    sample = re.sub("'s", "", sample)
    # Removing stop words
    f = open(SETTINGS.stop_words_file)
    stop_words = f.read().splitlines()
    sample = " ".join(word for word in sample.split() if word.lower() not in stop_words)
    
    print sample
       
