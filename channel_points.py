import os
import win32com.client as wincl

class redeem:
    def points(self,data):
        
        speak = wincl.Dispatch("SAPI.SpVoice")
        
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
            speak.Speak(highlight)
            return

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
            speak.Speak(sub)
            return

        # Custom reward for drop your weapons, change the reward id to yours
        elif "custom-reward-id=3c6182d9-2f87-43ad-bc5b-9764317ca104" in data:
            custom = "Drop your weapon. Drop. Drop it! Drop your weapons. Now!"
            speak.Speak(custom)
            return

        # Custom reward for end the stream, change the reward id to yours
        elif "custom-reward-id=a3e7db64-a64b-40d6-bcdd-4c59934c17db" in data:
            custom = "Sad. We have to end the stream now. Boo Hoo. Get ready for the raid boys!"
            speak.Speak(custom)
            return

        # Custom reward for play this game, change the reward id to yours
        elif "custom-reward-id=159a44a2-2ba5-4e12-bac8-1cd551bc48d1" in data:
            custom = "Stop. Wait a minute. Now you have to play another game after this."
            speak.Speak(custom)
            return

        # Custom reward for change your hero, change the reward id to yours
        elif "custom-reward-id=c76d57c2-aa9c-4137-9bbe-46d4219393c5" in data:
            custom = "Wow. You suck at playing this guy, You better change your hero to this one right here!"
            speak.Speak(custom)
            return

        # Custom reward for Hydrate, change the reward id to yours
        elif "custom-reward-id=d2240303-53ff-47c2-a741-b7ac31302e94" in data:
            custom = "DRINK! DRINK! DRINK! DRINK! DRINK!"
            speak.Speak(custom)
            return

        # Custom reward for Speak in Bangla for 5 minutes, change the reward id to yours
        elif "custom-reward-id=a9e882c7-f01b-45f2-9705-525a83fd95e7" in data:
            custom = "You gotta speak in Bangla now for 5 minutes. Can you keep that up atleast?"
            speak.Speak(custom)
            return

        elif "custom-reward-id=60785c5c-2e61-4525-a458-888242be5767" in data:
            ind = data.index("PRIVMSG #ingeniousartist :")+26
            name_ind = data.index("display-name=")+13
            i = name_ind
            end_ind = 0
            while True:
                if data[i]==";":
                    end_ind = i
                    break
                i+=1
            
            timeout = data[name_ind:end_ind] + " has timed out " + data[ind:] + " for 10 minutes"
            speak.Speak(timeout)
            return
            
            