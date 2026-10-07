RABBIT SENTENCE BUILDER - HOW TO ADD YOUR SOUNDS
=================================================
Open index.html in a browser to play. Just drop your recordings
into the folders below using EXACTLY these file names (.mp3).
Any file you don't add stays silent - nothing breaks.

1) audio/                  (game sounds)
   background.mp3   looping background music
   pick.mp3         short sound when a word starts to drag
   dragLoop.mp3     loops while dragging (stops on release)
   drop.mp3         word placed in a slot
   remove.mp3       word sent back to the bank
   correct.mp3      sentence correct
   wrong.mp3        sentence wrong
   hint.mp3         Hint button
   clear.mp3        Clear button
   next.mp3         Next Sentence button
   classChange.mp3  switching class (PP, I, II ...)
   complete.mp3     class finished
   star3.mp3 / star2.mp3 / star1.mp3   cheer for 3 / 2 / 1 stars

2) audio/sentences/        (your recorded sentences, 213 files)
   Named CLASS-NN.mp3, e.g. PP-01.mp3, PP-02.mp3 ... VI-15.mp3
   NN = the sentence number shown on screen.
   See sentence-checklist.csv for the full list (open in Excel).

3) audio/actions/          (optional, one per rabbit action)
   walk.mp3 run.mp3 jump.mp3 climb.mp3 swim.mp3 fly.mp3 fall.mp3
   sit.mp3 stand.mp3 wake.mp3 dance.mp3 eat.mp3 drink.mp3 cook.mp3
   sleep.mp3 read.mp3 write.mp3 draw.mp3 think.mp3 work.mp3
   speak.mp3 sing.mp3 teach.mp3 listen.mp3 look.mp3 cry.mp3
   wash.mp3 open.mp3 water.mp3 wave.mp3 give.mp3 catch.mp3
   push.mp3 bloom.mp3 rain.mp3

TIPS
- Keep files short and small (mp3, mono, 64-128 kbps) so the portal loads fast.
- Browsers only allow sound after the first tap, so the first sentence
  may start playing on the student's first tap.
- To change a file name or turn the voice off, edit the settings near
  the top of the <script> in index.html (AUDIO_FILES, ACTION_SOUNDS,
  SENTENCE_AUDIO).
- Upload the whole folder (index.html + audio/) together to your portal.

CUSTOM FONT (shows on every phone, tablet and computer)
-------------------------------------------------------
Phones do not have your font installed, so it must travel with the game.
1. Convert your font to WOFF2 (free: transfonter.org or cloudconvert.com).
2. Name it CustomFont.woff2 and put it in the fonts/ folder.
   (Optional extras for very old browsers: CustomFont.woff, CustomFont.ttf)
3. Upload the whole folder (index.html + fonts/ + audio/) to your portal.
If a student's browser can't load it, the game falls back to
Noto Sans Tibetan automatically, so Dzongkha is always readable.

Guaranteed option: python3 embed-font.py fonts/CustomFont.woff2
creates index-single-file.html with the font built inside the file.
Make sure your font's licence allows use on websites.
