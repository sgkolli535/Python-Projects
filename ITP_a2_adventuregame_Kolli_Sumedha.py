# Sumedha Kolli
# ITP 115, Fall 2019
# Assignment 2, Part 2
# sgkolli@usc.edu
# 9/15/2019
# Description:
# This is a program that simulates a "Choose your Own Adventure" game.
# The premise of the story is that you are biking home late at night after stopping by at a local convenience store.
# Each line is indented to make the story easier to read for the user.
print("You open the door of the convenience store to let the frigid night air engulf you once again. After hanging the"
      "\nbag of potato chips, candy bars, and chewing gum onto the bike handle, you set off into the night, peddling"
      "\nfaster in an attempt to leave behind the cold. A few minutes of peddling pass by before you feel the beam of a"
      "\ncar's headlight constantly following you. This seems really odd, since you're on a two lane road and the"
      "\ndriver could easily pass you if they wanted. While you try to turn back to get a good look at the driver"
      "\nbehind you, your bag falls off the handle and rolls down a hill to disappear into the woods. You decide to"
      "\npull over and try to find your bag, but the car also pulls over behind you.")
# Each choice is indented even more to make the format easier to read.
# "quest1" is the variable for the first question, and it has two choices.
quest1 = input("\nDo you: "
               "\n   a) Ignore the car and continue looking for your bag "
               "\n   b) Leave the bag and get away as fast as possible"
               "\n> ")

# the following set of code is for if the user chose option A for the first question.
# "quest21" is the second question asked to the user. This question has three options for the user to choose from.
if quest1 == "a" or quest1 == "A":
    print("\nYou scurry off into the woods, well aware that the car door opened and the driver is getting out."
          "\nSuddenly, you spot the white sheen of your bag stuck inside a bush. At the same moment, you hear scraping"
          "\nsounds and you turn around to see the driver dragging your bike and throwing it in the back of their car.")
    quest21 = input("\nDo you: "
                    "\n   a) Run to grab your bag, risking confrontation with the unknown driver."
                    "\n   b) Try to get away as fast as possible, even without your bag."
                    "\n   c) Confront the unknown driver about taking your bike."
                    "\n> ")
    if quest21 == "a" or quest21 == "A":
        print('\nYou run to your bag, but end up hearing footsteps approaching you. "Oh my god," you think, as you '
              '\nbrace yourself for whatever is about to happen. As the figure approaches, you realize they look '
              '\nawfully familiar... The driver is your mom! She tells you to stop going out alone this late at night,'
              '\nand takes you home. What a night!')
    elif quest21 == "b" or quest21 == "B":
        print('\nYou begin your mad dash to get out of the woods and away from the driver, despite leaving behind both'
              '\nyour bag and bike. Randomly, your phone starts buzzing. You glance at the caller id to see that it is'
              '\nyour mom. "Why is she calling me now?" you wonder. "Why are you running away? I am here to take you'
              '\nhome," she tells you. An immense sigh of relief leaves your mouth as you head back to grab your bag '
              '\nand walk to her car. She lectures you about not going out alone at night, but you listen with content,'
              '\nrather than with anger; you would not have it any other way.')
    elif quest21 == "c" or quest21 == "C":
        print("\nAs you get closer and closer to the looming figure, they begin to look oddly familiar. It's your mom!"
              "\nYou breath a huge sigh of relief as you run up to hug her. You've never been more glad to see her."
              "\nAfter grabbing your bag and listen to a huge lecture about going out alone at night, both of you head"
              "\nhome together under the bright moonlight.")
# If the user enters an invalid option for "quest2", they are defaulted to option A, as per the instructions said.
    else:
        print("You have entered an invalid choice. Your option will be defaulted to option A.")
        print('\nYou run to your bag, but end up hearing footsteps approaching you. "Oh my god," you think, as you '
              '\nbrace yourself for whatever is about to happen. As the figure approaches, you realize they look '
              '\nawfully familiar... The driver is your mom! She tells you to stop going out alone this late at night,'
              '\nand takes you home. What a night!')

# the following set of code is for if the user chose option B for the first question.
# "quest22" following option B from "quest1" is the alternative to "quest21" following option A from "quest1".
elif quest1 == "b" or quest1 == "B":
    print("\nThe lost bag of candy and chips haunts your mind as you pedal to the fastest of your abilities, not"
          "\nknowing whether or not the car is still in your pursuit. Out of nowhere, your phone starts buzzing in your"
          "\npocket.")
    quest22 = input("\nDo you: "
                    "\n   a) Take a look at the phone, even if it means having the car catch up to you."
                    "\n   b) Ignore the call, no matter how important it might be."
                    "\n   c) Stop completely. You're tired of this chase and just want to confront the driver."
                    "\n> ")
    if quest22 == "a" or quest22 == "A":
        print('\nYou use your wobbly left hand to take your phone out of your pocket. The caller id shocks you: it is'
              '\nyour mom... You lift the call to hear her say, "Why are you running away from me?" You slowly turn to'
              '\nsee the confused face of your mom in the car. Your breathing finally begins to slow down as you sit'
              '\nnext to her. Compared to the rest of the night, her lecture about not going out alone at night is one'
              '\nof the highlights. She even promises to buy you the candy bars again.')
    elif quest22 == "b" or quest22 == "B":
        print('\nAs you continue to zoom on, the car starts vigorously honking at you. "What else could they possibly'
              '\nwant", you think to yourself. When you finally give in and turn around, you are shocked to see your'
              '\nmom behind the wheel! You come to speedy halt on the bike and climb into the passenger seat of the'
              '\ncar. She starts to lecture you about going out alone at night, but sees the fatigue in your face and'
              '\nstops. She gives you a tender pat on the head to let you know that everything is alright.')
    elif quest22 == "c" or quest22 == "C":
        print("\nAs your bike tires screech to a halt, you jump off to demand a confrontation with the driver. To your"
              "\nincredible shock, you see your mom behind the wheel. You fall into the passenger seat, exhausted after"
              "\nthe night you've had. Your mom, understanding your situation, holds off on her lecture about going out"
              "\nalone at night. She promises to buy you more candy bars later, and the initial anger begins to fade"
              "'n from your mind.")
# if the user enters an invalid option for "quest2", they are defaulted to option A, as per the instructions said.
    else:
        print("You have entered an invalid choice. Your option will be defaulted to option A.")
        print('\nYou use your wobbly left hand to take your phone out of your pocket. The caller id shocks you: it is'
              '\nyour mom... You lift the call to hear her say, "Why are you running away from me?" You slowly turn to'
              '\nsee the confused face of your mom in the car. Your breathing finally begins to slow down as you sit'
              '\nnext to her. Compared to the rest of the night, her lecture about not going out alone at night is one'
              '\nof the highlights. She even promises to buy you the candy bars again.')

# the following set of code is for if the user typed an invalid choice for the first question, as per the instructions.
# the default option B displays all the choices that come with "quest22".
else:
    print("You have entered an invalid choice. Your option will be defaulted to option B.")
    print("\nThe lost bag of candy and chips haunts your mind as you pedal to the fastest of your abilities, not"
          "\nknowing whether or not the car is still in your pursuit. Out of nowhere, your phone starts buzzing in your"
          "\npocket.")
    quest22 = input("\nDo you: "
                    "\n   a) Take a look at the phone, even if it means having the car catch up to you."
                    "\n   b) Ignore the call, no matter how important it might be."
                    "\n   c) Stop completely. You're tired of this chase and just want to confront the driver."
                    "\n> ")
    if quest22 == "a" or quest22 == "A":
        print('\nYou use your wobbly left hand to take your phone out of your pocket. The caller id shocks you: it is'
              '\nyour mom... You lift the call to hear her say, "Why are you running away from me?" You slowly turn to'
              '\nsee the confused face of your mom in the car. Your breathing finally begins to slow down as you sit'
              '\nnext to her. Compared to the rest of the night, her lecture about not going out alone at night is one'
              '\nof the highlights. She even promises to buy you the candy bars again.')
    elif quest22 == "b" or quest22 == "B":
        print('\nAs you continue to zoom on, the car starts vigorously honking at you. "What else could they possibly'
              '\nwant", you think to yourself. When you finally give in and turn around, you are shocked to see your'
              '\nmom behind the wheel! You come to speedy halt on the bike and climb into the passenger seat of the'
              '\ncar. She starts to lecture you about going out alone at night, but sees the fatigue in your face and'
              '\nstops. She gives you a tender pat on the head to let you know that everything is alright.')
    elif quest22 == "c" or quest22 == "C":
        print("\nAs your bike tires screech to a halt, you jump off to demand a confrontation with the driver. To your"
              "\nincredible shock, you see your mom behind the wheel. You fall into the passenger seat, exhausted after"
              "\nthe night you've had. Your mom, understanding your situation, holds off on her lecture about going out"
              "\nalone at night. She promises to buy you more candy bars later, and the initial anger begins to fade"
              "\n from your mind.")
# if the user enters another invalid option for "quest22", they are defaulted to option A, as per the instructions.
    else:
        print("You have entered an invalid choice. Your option will be defaulted to option A.")
        print('\nYou use your wobbly left hand to take your phone out of your pocket. The caller id shocks you: it is'
              '\nyour mom... You lift the call to hear her say, "Why are you running away from me?" You slowly turn to'
              '\nsee the confused face of your mom in the car. Your breathing finally begins to slow down as you sit'
              '\nnext to her. Compared to the rest of the night, her lecture about not going out alone at night is one'
              '\nof the highlights. She even promises to buy you the candy bars again.')

print("\nTHE END")