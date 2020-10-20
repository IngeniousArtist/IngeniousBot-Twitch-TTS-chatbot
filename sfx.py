from gtts import gTTS
import os

class getsfx:
    def sfx(self,data):
        # Does TTS on highlight my text
        if "msg-id=highlighted-message" in data:
            ind = data.index("PRIVMSG #ingeniousartist :")+26
            name_ind = data.index("display-name=")+13
            i = name_ind
            end_ind = 0
            while True:
                if data[i]==";":
                    end_ind = i
                    break
                i+=1
            
            highlight = data[name_ind:end_ind] + " says: " + data[ind:]
            language = 'en'
            myobj = gTTS(text=highlight, lang=language, slow=False)
            myobj.save("highlight.mp3")
            os.system("highlight.mp3")

        # Thanks subscribers for subbing
        elif "msg-id=resub" in data:
            name_ind = data.index("display-name=")+13
            i = name_ind
            end_ind = 0
            while True:
                if data[i]==";":
                    end_ind = i
                    break
                i+=1
            
            sub = data[name_ind:end_ind] + " has just subscribed to the channel! Arigatow Gozai masu."
            language ='en'
            myobj = gTTS(text=sub, lang=language, slow=False)
            myobj.save("subthank.mp3")
            os.system("subthank.mp3")

        # Custom reward for drop your weapons, change the reward id to yours
        elif "custom-reward-id=3c6182d9-2f87-43ad-bc5b-9764317ca104" in data:
            custom = "Drop your weapon. Drop. Drop it! Drop your weapons. Now!"
            language = 'en'
            myobj = gTTS(text=custom, lang=language, slow=False)
            myobj.save("custom_reward.mp3")
            os.system("custom_reward.mp3")

        # Custom reward for end the stream, change the reward id to yours
        elif "custom-reward-id=a3e7db64-a64b-40d6-bcdd-4c59934c17db" in data:
            custom = "Sad. We have to end the stream now. Boo Hoo. Get ready for the raid boys!"
            language = 'en'
            myobj = gTTS(text=custom, lang=language, slow=False)
            myobj.save("custom_reward.mp3")
            os.system("custom_reward.mp3")

        # Custom reward for play this game, change the reward id to yours
        elif "custom-reward-id=159a44a2-2ba5-4e12-bac8-1cd551bc48d1" in data:
            custom = "Stop. Wait a minute. Now you have to play another game after this."
            language = 'en'
            myobj = gTTS(text=custom, lang=language, slow=False)
            myobj.save("custom_reward.mp3")
            os.system("custom_reward.mp3")

        # Custom reward for change your hero, change the reward id to yours
        elif "custom-reward-id=c76d57c2-aa9c-4137-9bbe-46d4219393c5" in data:
            custom = "Wow. You suck at playing this guy, You better change your hero to this one right here!"
            language = 'en'
            myobj = gTTS(text=custom, lang=language, slow=False)
            myobj.save("custom_reward.mp3")
            os.system("custom_reward.mp3")

        # Custom reward for Hydrate, change the reward id to yours
        elif "custom-reward-id=d2240303-53ff-47c2-a741-b7ac31302e94" in data:
            custom = "DRINK! DRINK! DRINK! DRINK! DRINK!"
            language = 'en'
            myobj = gTTS(text=custom, lang=language, slow=False)
            myobj.save("custom_reward.mp3")
            os.system("custom_reward.mp3")

        # Custom reward for Speak in Bangla for 5 minutes, change the reward id to yours
        elif "custom-reward-id=a9e882c7-f01b-45f2-9705-525a83fd95e7" in data:
            custom = "বাংলা তে কথা বল হালারপো। এখন থেকে এভাবে কথা বলতে হবে ৫ মিনিট ধরে।"
            language = 'bn'
            myobj = gTTS(text=custom, lang=language, slow=False)
            myobj.save("custom_reward.mp3")
            os.system("custom_reward.mp3")