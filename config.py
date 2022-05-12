# CW SPEED
ONE_UNIT = 0.06
TWO_UNITS = 2 * ONE_UNIT
THREE_UNITS = 3 * ONE_UNIT
SEVEN_UNITS = 7 * ONE_UNIT

# 10000 maximum volume
SPEAKER_VOLUME = 10000 # Internal speaker
OUTPUT_VOLUME = 250 # Audio output

# Frequency
CW_TONE_SPEAKER = 1200
CW_TONE_OUTPUT = 600

# PTT behavior
PTT_KEYER = False # Will be depricated soon ... we will have a dedicated CW key output
PTT_HANGTIME = 0.3 # For manual keying (paddle and straight)

# Keyboard input (or 2nd cw key)
KBD = False # If False you can add a second cw key (paddle or straight)
KBD_KEY_PADDLE = True

# CW Memories (for with the keyboard)
SW1 = "CQ DE ON3URE"
SW2 = "73 DE ON3URE"
SW3 = "ON3URE"
SW4 = "QTH MERCHTEM BELGIUM"
SW5 = "599"
SW6 = "ON4AOW"
SW7 = "ON6WJ"
SW8 = "ON4IT"

# Voice Memories (for with the keyboard)
# 16bit 16khz mono is more then sufficient (22khz will work to)
VSW1 = "on3ure.wav"
VSW2 = "2.wav"
VSW3 = "3.wav"
VSW4 = "4.wav"
VSW5 = "5.wav"
VSW6 = "6.wav"
VSW7 = "7.wav"
VSW8 = "8.wav"

# Beacon settings
BEACON = "ON3URE CW BEACON IN TEST"
BEACON_SLEEP = 600