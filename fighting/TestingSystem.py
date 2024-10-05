from classes import Hitbox

class HitboxTests():
    # Create and initiate testing class
    def __init__(self) -> None:
        self.testAmount = 6

    # Start hitbox collision testing
    def CollisionTest(self):
        print("Starting testing hitboxes...")
        
        # Start counting correctly ansered tests
        correctTests = 0

        h1 = Hitbox(0, 0, 10, 10)
        h2 = Hitbox(1000, 1000, 10, 10)

        # Hitboxes far away from eachother
        # Expected - False
        if not h1.DoHitboxesCollide(h2):
            print("Test 1 - passed!")
            correctTests += 1
        else:
            print("Test 1 - failed!")


        h1 = Hitbox(40, 40, 10, 10)
        h2 = Hitbox(50, 50, 10, 10)

        # Hitboxes touch by a corner
        # Expected - True
        if h1.DoHitboxesCollide(h2):
            print("Test 2 - passed!")
            correctTests += 1
        else:
            print("Test 2 - failed!")


        h1 = Hitbox(50, 40, 10, 10)
        h2 = Hitbox(50, 50, 10, 10)

        # Hitboxes touch by a side
        # Expected - True
        if h1.DoHitboxesCollide(h2):
            print("Test 3 - passed!")
            correctTests += 1
        else:
            print("Test 3 - failed!")

        
        h1 = Hitbox(50, 50, 10, 10)
        h2 = Hitbox(50, 50, 10, 10)

        # Hitboxes are the same
        # Expected - True
        if h1.DoHitboxesCollide(h2):
            print("Test 4 - passed!")
            correctTests += 1
        else:
            print("Test 4 - failed!")


        h1 = Hitbox(50, 50, 10, 10)
        h2 = Hitbox(40, 40, 10, 10)

        # Hitboxes touch by a corner
        # Expected - True
        if h1.DoHitboxesCollide(h2):
            print("Test 5 - passed!")
            correctTests += 1
        else:
            print("Test 5 - failed!")


        h1 = Hitbox(50, 50, 10, 10)
        h2 = Hitbox(50, 40, 10, 10)

        # Hitboxes touch by a side
        # Expected - True
        if h1.DoHitboxesCollide(h2):
            print("Test 6 - passed!")
            correctTests += 1
        else:
            print("Test 6 - failed!")

        print("Tests passed: ", str(correctTests) + " / " + str(self.testAmount))


tests = HitboxTests()

tests.CollisionTest()