# LOYOLA, REYLENE GRACE A.
# IT3C
# WEEK 5 - LABORATORY EXERCISES WORDSCAPES

print("#" * 25, " pneumonoultramicroscopicsilicovolcanoconiosis ", "#" * 25)

target = "pneumonoultramicroscopicsilicovolcanoconiosis"
guessed = []
score = 0

while score < 10:
    guess = input("Enter a word:")
    prev_count = guessed.count(guess)
    guessed.append(guess)

    if prev_count > 0:
        print("%s already exists" % guess)
    else:
        # 1. volcano
        if guess == target[30:37]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 2. pneumonic
        elif guess == target[0:7] + target[27:29]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 3. microscopic
        elif guess == target[13:24]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 4. ultra
        elif guess == target[8:13]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 5. silicon
        elif guess == target[24:30] + target[35:36]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 6. monocle
        elif guess == target[4:8] + target[23:27:3] + target[2:3:2]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 7. sonic
        elif guess == target[18:21:2] + target[1:3:2] + target[22:24]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 8. concision
        elif guess == target[37:40] + target[19:23:3] + target[42:44] + target[38:40]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 9. neuron
        elif guess == target[1:4] + target[16:18] + target[-6]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        # 10. concave
        elif guess == target[37:40] + target[33:35] + target[-15] + target[2:3:2]:
            print("%s is correct!" % guess)
            score += 1
            print("Score is %d" % score)

        else:
            print("Sorry, your guess is incorrect.")
if score == 10:
    print("Yayy! Congratulations! You reached 10 points!")