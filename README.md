# Reddit Bot - LifeProTips

I detta projekt har jag tränat en model på inlägg på subredditen LifeProTips, så att den kan skapa egna inlägg. Detta gör jag sedan till en bot som lägger ut sina egen-genererade inlägg på Reddit.

## Filer
* **data.txt** - Varje rad är ett inlägg. Titeln och texten separeras av "\*\*\*\*\*". Detta så att modellen kan tränas för att både skapa titeln och text.
* **train.py**
* **model_bot.py**
* **bot.py**
