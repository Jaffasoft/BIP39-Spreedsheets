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

