"""Next Noob Project
Intro DocString
Nested Loops Example"""

# Just learning
MESSAGE = "Looping in Python!"
RANGE = 5
COUNTER = 0
OUTERCOUNTER = 0

# Create loop
for _ in range(RANGE):
    OUTERCOUNTER += 1
    INNERCOUNTER = 0
    for _ in range(RANGE):
        INNERCOUNTER += 1
        print(f"Outer Loop: {OUTERCOUNTER}")
        print(f"  Inner Loop: {INNERCOUNTER}")
        COUNTER += 1
        print(f"Total count: {COUNTER}")
        print("---")
        print(MESSAGE)
        # EOF
