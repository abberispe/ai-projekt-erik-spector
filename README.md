# Reddit Bot - LifeProTips

I detta projekt har jag tränat en model på inlägg på subredditen LifeProTips, så att den kan skapa egna inlägg. Detta gör jag sedan till en bot som lägger ut sina egen-genererade inlägg på Reddit. Såhär kan ett inlägg se ut:
![Inlägg](images/post.PNG)

## Files
* **data.txt** - Varje rad är ett inlägg. Titeln och texten separeras av "\*\*\*\*\*". Detta så att modellen kan tränas för att både skapa titeln och text.
* **train.py** - Tränar en modell på data i data.txt.
* **model_bot.py** - Innehåller funktioner för att generera text via modellen, och för att se om den genererade texten finns i data.txt
* **bot.py** - Använder funktionerna i **model_bot.py** och lägger upp inlägg på Reddit under godtyckliga intervall.

## Usage
För att kunna använda denna bot på ditt egna reddit konto, måste du skapa en Reddit applikation på sidan [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/). Byt ut mina client-id och client-secret på filen **bot.py** med dina client-id och client-secret som du fick när du skapade applikationen. Byt också ut mina inloggningsuppgifter med dina. Titta gärna på [denna](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/) guide för att förstå mer om hur du får ditt client-id och client-secret. Du kan nu välja vilken subreddit botten ska köras i, alltså var den kommer att göra sina inlägg, med hjälp av variabeln "subreddit" i filen **bot.py**. I mitt fall gör den sina inlägg i subredditen "BotsParadise", som är en egengjord subreddit för testning. När du har lagt till client-id, client-secret samt subreddt, är det bara att köra filen **bot.py**, för att få botten att köras. Ett lyckat post kan se ut såhär i terminalen:
![Inlägg](images/terminal.PNG)
### Dependencies
* praw ``` pip install praw==6.5.1```
* gpt_2_simple ``` pip install gpt_2_simple==0.7.1 ```
* tensorflow 1.14.0 ``` pip install tensorflow==1.14.0```

## How it works

## Problems and solutions
Ett problem jag stötte på när jag skapade denna bot var att den ofta skapade alldeles för långa inlägg. Den kunde fortsätta i flera hundra ord, ofta med många upprepningar. Jag löste detta genom att skapa flera inlägg vid varje cykel, och välja den som var kortast.

## Future developments
Projektet kan till exempel utvecklas genom att få botten att svara på kommentarer den får på sitt inlägg. 
