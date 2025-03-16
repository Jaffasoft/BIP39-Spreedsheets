

For the safest way to make a 12 or 24 word seed phrase use this safe method outlined in this next paragraph. DO NOT USE ANY OTHER WAY IN MY OPINION VERY IMPORTANT NOT TO BE ONLINE. DONT EVEN BE ONLINE FOR A TINY SECOND ITS ALL IT TAKES FOR A HACKER TO GET YOUR SEED AND STEAL YOUR BITCOIN. YOU HAVE BEEN WARNED WITH CAPITAL LETTER!!!!!

This is the MOST important part. For the safest way to make a seed phrase use the PRINT OFFLINE DICE & SEED CALCULATOR.pdf do everything offline for your REAL seed phrase (use paper and a pencil). The one you will really use and store Bitcoin or alt coins in a wallet or hardware device or signing device whatever the case may be. I do not recommend any other method. Sit down and get a dice or dices and roll it 128 times and record the results on the printed A4 sheet and do the math to derive the words. Each roll that is Even (2,4 or 6) you record a 0 in the printed page and each Odd roll (1,3 or 5) you record a 1 in the sheet. These are called binary bits and you should have 11 for each word. 

Example: 01101110011 when binary of 11 bits is converted to decimal (a normal number) it will be a number between 1 and 2048 possible words on the BIP39 wordlist. You then plus +1 to the number because the wordlist will normally start with 1 instead of how coputers count starting from 0 unsing binary bits. It is not overly hard once you see how to do it manually and is a good life skill to have to get good entropy and randomness in your seed phrase. The final word for 12 or 24 word phrases is a little bit more difficult to work out and can't be done on paper easily and usually involved sha256 the total 128 or 256 bits in one long string and the first number (the hex) of the sha256 is converted to 4 binary bits and appended to the end of the 128 bit to make a total of 132 bits and also derives the last checksum (word). It is 8 bits for 24 words a little different but the same principle again. 

You can see it is a little complicated and this is the trickiest part to doing this without going online to a sha256 calculator or script to do it. But hardware devices and signing devices usually will have this function built in so you can input your own 11 or 23 words that you plucked out of thin air rolling your dice and calculating on paper the first 11 or 23 words. And the OFFLINE hardware device will work out and or offer you a few possible last words to select from. 

You can still derive a 12th word or 24th word on your dice and paper getting 7 random bits for the 12th word and 3 random bits for the 24th word instead of 11 bits each row for the other words. Whatever word is calculates to using the 7 or 3 bits. You then enter this 12th or 24th word into your hardware device, even though it will be wrong (though it can randomly be right sometimes) but what this word does it indicate the top word of a block of 16 words in the lsit and one of the 16 below it will be the correct checksum. I realise this is tricky to explain and i would never have got it if i didnt make these spreadsheets. So look at the spreasheets to get a better understaning as i have laid them all out to explain this more esily. Just remember to not use them for any REAL seed generation online. Only use them online to learn how it works.  Then it selects the nearest checksum word offered by the device below it. There is one valid checksum for any 11 words in every block of 16 words and there is 128 blocks of 16. For 24 words there is 8 blocks of 256. 

For example if your random dice got 0 after you rolled the dice 7 bits the word would be Abandon because it is the first word on the wordlist and either that word of one of the other 15 below it will be a valid checksum. 

I spent a couple months late into nights researching this and i came to the conclusion that there is no other way i would do this. I will not trust a PC, a human, a script, a device, your kids random dice on a game or a wallet on a phone or anything online wantsoever or any other thing. If you have rolled a dice and did the seed yourself on good old fashioned paper you know that it is done with random entropy and done acceptably and properly. Take some time sit down roll that dice and sleep easy.  


!!!! WARNING ONLY THE PRINT OFFLINE DICE & SEED CALCULATOR.pdf IS SAFE DO NOT USE ANY OF THE ONLINE SPREADSHEETS ABOVE!!!!!

***** THIS IS DEADLY IMPORTANT... DO NOT USE THIS SPREEDSHEETS OR KIVY OR ANY ONLINE 12 OR 24 WORD SEED PHRASE GENERATOR TO MAKE YOUR OWN SEED ONLINE!*****


DONT EVEN USE THIS OFFLINE TO GENERATE A SEED!!
NEVER USE AN ONLINE SCRIPT OF DIGITAL DICE ROLL OR ANYTHING ONLINE AT ALL FOR THAT MATTER.
PEOPLE HAVE BEEN HACKED USING THESE TYPE OF SCRIPTS ONLINE AND IN HARDWARE DEVICES. ONLY USE THESE SCRIPTS TO LEARN 
THE SAME GOES FOR ALL THE SPREADSHEETS IN MY REPOSITORY. I CREATED THEM SO THAT I CAN SEE AND UNDERSTAND HOW BIP39 WORKS AND I JUST SHARED IT WITH YOU HOW
THE MATH WORKS UNDER THE HOOD TO GIVE YOU A BETTER UNDERSTANDING. BUT IT IS HIGHLY POSSIBLE THAT IT IS NOT PERFECT
AS I AM NOT A CRYPTOGRAPHIC EXPERT OR A CODER. THESE SCRIPTS WERE WRITTEN 100% BY GROK3 BETA I DID NOTHING JUST ASKED IT QUESTIONS. 
EVEN IF THE SEEDS ARE GOOD THE PROBEM IS ALSO THAT A HASKER CAN JUST SEE WITH A KEYLOGGER OR OTHER WAYS TO HACK YOUR SEED PHRASE IF DONE ONLINE.
ONLINE IS NO GO ZONE FOR CRYPTO SEED PHRASES. 

SO HOW DO I DO A 12 OR 24 WORD SEED "PROPERLY"? 
BE SMART AND TAKE THE TIME, SIT DOWN AT A GOOD OLD FASHIONED TABLE GET A REAL 6 SIDED DICE OR DICES AND ROLL IT
128 TIMES OR 256 TIMES FOR 24 WORDS AND SO THE MATH IS DONE IN YOUR HEAD (NOT ON A COMPUTER). SOME HARDWARE DEVICES ASK FOR 50 DICE ROLLS. 
STUDY THE SPREADSHEETS ON HOW TO DO IT. 
REFER TO THE SPREADSHEETS AND GET A BLANK SHEET PRINT IT AND GO ABOUT FILLING IT WITH YOUR DICE ROLL RESULTS. IF IT IS AN ODD NUMBER 
PUT A 1 IF IT IS A EVEN NUMBER PUT A 0 UNTILL YOU HAVE 11 BITS FOR EACH WORD AND 4 BITS FOR THE LAST WORD. REFER TO THE SPREADSHEETS
TO SEE HOW TO CALCULATE THE WORDS FROM THE 2048 IN THE LIST. 

I KNOW IT IS A PAIN AND WE LIKE TO USE COMPUTERS TO DO THINGS EASY BUT JUST TAKE AN HR OF YOUR TIME FOR THE SACK OF SECURITY AND DO
LEARN THIS LIFE SKILL WHICH WILL SERVE YOU WELL FOR YEARS TO COME. 




Hi, 

These sheets are from a newbies perspective and a consumers perspective of trying to learn how wallets work and how the 12 0r 24 word seed phrase works. 


There are no scripts in any these files though you should do your own checking. I made these in Google Sheets and downloaded them from my drive!


Discover a groovy trick about working out the checksum manually and guessing it yourself completely offline for the 12th word.  

I created these sheets from scratch because I was curious how it all works and wanted to learn how the Bitcoin Improvement Protocol (BIP39) works under the hood on a basic level of generating the words and how the numbers system works to eventually roll my own dice and randomly generate a new 12- or 24-word seed phrase air gapped and completely offline as you should do too to use for real!!!!

You should never use this sheet online to generate your own 12- or 24-word seed. These sheets are just for learning purposes but just go ahead and have a play. Sheets include a number of ways to get a seed phrase with links to SHA256 hashing web sites and others. 


Key take aways:
Learn how a bitcoin private master key all starts from just generating random 0 and 1s out of thin air.
Each time you edit any cell in the sheet it will lose the last phrase and generate a brand new one. So be careful. You will work it out as you go along. 

Learn how the 0 and 1's can be converted to HEX so that it can be SHa256 hashed to find the checksum from the first number of the hash (hexadecimal) converted to the last four binary digits of the 128 bits of entropy to make 132 bits in total.

The interesting bit I learned most for generating the 12th word (which is supposed to be a correct checksum or it doesn’t work) was that the final word is wrong (though it can possibly be right!) but it directs
you to top of the block of 1-16 words from which to try each one until one of them will always be the checksum word. This is the same for the 24th word but it is 1 word out of 256 for the 24th word so much harder 
to just manually guess. It hard to explain but look at what it says the 12th word is and then go down the list and find that word then that word or one of the other 1-16 below it in that block will be the 
correct checksum. 

This way you can manually type in the wallet and try words until you get the correct one. Not needing to be only at all to use the column website etc if you do not want to. I never read this 
way anyway anywhere else the internet so I wanted to share my discovery. Which only could happen once looking at it all outlaid in the spreadsheet. 


The sheet includes:
Separate column list of 0-2047 binary numbers.
Separate column list of actual 1-2048 actual BIP39 words list.
Separate column list of the words with only the four first letters to each would in the 1 - 2048 BIP39 words list. 
Randomly selects 128 bits of binary 0 and 1s.
Concatenates the full entropy of 128 bits into one long string 0110101010111101 etc 
Concatenates the 128 bits into hexadecimal.
Show which words to try out of the block of 1-16 possible final word for the checksum. 


After you have done all this and you are ready to generate you own REAL 12 word seed phrase I suggest to get an old fashioned
pen or pencil and peace of paper and roll dice or flip a coin 128 times and put them all down on paper and calculate the word and 
look at the word list and write down your 12 words on paper and manually enter in one at a time for the 12th word until your hardware 
wallet accepts it as correct. This way you have generated total random entropy and did it all offline where nobody in the world 
other then you know what the 12 word all important seed phrase is. And 12 words is enough you do not need 24 words plus you can add a passphrase.



All The Best,
Jaffasoft 

