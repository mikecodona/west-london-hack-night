# -*- coding: utf-8 -*-
from collections import defaultdict
from operator import itemgetter

import random
import re

lyrics = """Say your prayers little one
Don't forget my son
To include everyone
I tuck you in
Warm within
Keep you free from sin
'Til the sandman he comes
Sleep with one eye open
Gripping your pillow tight
Exit light
Enter night
Take my hand
We're off to never never-land
Something's wrong, shut the light
Heavy thoughts tonight
And they aren't of snow white
Dreams of war
Dreams of lies
Dreams of dragons fire
And of things that will bite, yeah
Sleep with one eye open
Grippin' your pillow tight
Exit light
Enter night
Take my hand
We're off to never never-land
Now I lay me down to sleep
Now I lay me down to sleep
Pray the lord my soul to keep
And if I die before I wake
Pray the lord my soul to take
Hush little baby don't say a word
And never mind that noise you heard
It's just the beast under your bed
In your closet in your head
Exit light
Enter night
Grain of sand
Exit light
Enter night
Take my hand
We're off to never never-land
We're off to never never-land
Take my hand
We're off to never never-land
Take my hand
We're off to never never-land
We're off to never never-land



You know you love me, I know you care
Just shout whenever, and I'll be there
You are my love, you are my heart
And we will never ever ever be apart

Are we an item? Girl, quit playing
We're just friends, what are you saying?
Say there's another and look right in my eyes
My first love broke my heart for the first time
And I was like...

Baby, baby, baby oooh
Like baby, baby, baby nooo
Like baby, baby, baby oooh
I thought you'd always be mine (mine)

Baby, baby, baby oooh
Like baby, baby, baby nooo
Like baby, baby, baby oooh
I thought you'd always be mine (mine)

Oh, for you I would have done whatever
And I just can't believe we ain't together
And I wanna play it cool, but I'm losin' you
I'll buy you anything, I'll buy you any ring
And I'm in pieces, baby fix me
And just shake me 'til you wake me from this bad dream
I'm going down, down, down, down
And I just can't believe my first love won't be around

And I'm like
Baby, baby, baby oooh
Like baby, baby, baby nooo
Like baby, baby, baby oooh
I thought you'd always be mine (mine)

Baby, baby, baby oooh
Like baby, baby, baby nooo
Like baby, baby, baby oooh
I thought you'd always be mine (mine)


Luda! When I was 13, I had my first love,
There was nobody that compared to my baby
And nobody came between us or could ever come above
She had me going crazy, oh, I was star-struck,
She woke me up daily, don't need no Starbucks.
She made my heart pound, it skipped a beat when I see her in the street and
At school on the playground but I really wanna see her on the weekend.
She knows she got me dazing cause she was so amazing
And now my heart is breaking but I just keep on saying

Baby, baby, baby oooh
Like baby, baby, baby nooo
Like baby, baby, baby oooh
I thought you'd always be mine (mine)

Baby, baby, baby oooh
Like baby, baby, baby nooo
Like baby, baby, baby oooh
I thought you'd always be mine (mine)

I'm gone (Yeah Yeah Yeah, Yeah Yeah Yeah)
Now I'm all gone (Yeah Yeah Yeah, Yeah Yeah Yeah)
Now I'm all gone (Yeah Yeah Yeah, Yeah Yeah Yeah)
Now I'm all gone (gone, gone, gone...)
I'm gone"""


def get_words(text):
    return re.findall("[a-z']+", text.lower())


def get_word_counts(lyrics):
    words = get_words(lyrics)
    word_counts = {}
    for w in words:
        following_words = defaultdict(lambda: 0)
        for i, w2 in enumerate(words[:-1]):
            if w == w2:
                following_words[words[i + 1]] += 1

        word_counts[w] = following_words

    return word_counts


def make_chains(word_counts):
    markov_chains = {'.': []}
    for word, following_words in word_counts.iteritems():
        total = sum(i for following_word, i in following_words.items())
        markov_chains[word] = []
        for following_word, count in following_words.items():
            markov_chains[word].append((following_word, count / float(total)))

        markov_chains[word].sort(key=itemgetter(1), reverse=True)

    return markov_chains


def get_next_word(all_words, word):
    possible_words = all_words[word]

    if len(possible_words) == 0:
        return None

    number = random.random()

    for possible_word, probabilty in possible_words:
        if number <= probabilty:
            return possible_word
        else:
            number -= probabilty

    return returnWord


def generate_song(word, num_words, all_words):
    song = [word]

    for i in xrange(0, num_words):
        word = get_next_word(all_words, word)

        if word:
            song.append(word)
        else:
            break

    return song


def pretty_print(song):
    step = 5
    for i in xrange(0, len(song), step):
        print ' '.join(song[i:i + step])


def main():
    word_counts = get_word_counts(lyrics)
    all_words = make_chains(word_counts)
    print pretty_print(generate_song('the', 100, all_words))

if __name__ == "__main__":
    main()

