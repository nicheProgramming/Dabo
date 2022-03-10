# Define the possible symbols on the wheel
symbolShapes = ["square", 
                "triangle", 
                "circle", 
                "swirl", 
                "quark", 
                "ds9", 
                "blackHole"]

class instantiateWheel:
    def buildOneWheel(self, position):
        # The inner wheel doesn't need to account for color, the others do
        if self.position == 0:
            # Store shape, then number of shapes
            self.wheel = [["square", 3],
                          ["swirl", 1],
                          ["circle", 1],
                          ["triangle", 3],
                          ["circle", 1],  
                          ["triangle", 1],
                          ["square", 2],
                          ["ds9", 1],
                          ["square", 1],
                          ["square", 3],
                          ["circle", 3],
                          ["square", 2],
                          ["blackHole", 1],
                          ["circle", 1],
                          ["square", 3],
                          ["triangle", 2],
                          ["triangle", 1],
                          ["blackHole", 1],
                          ["circle", 3],
                          ["square", 1],
                          ["ds9", 1],
                          ["triangle", 2],
                          ["blackHole", 1],
                          ["circle", 2],
                          ["triangle", 1],
                          ["circle", 3],
                          ["quark", 1],
                          ["triangle", 3],
                          ["circle", 2],
                          ["triangle", 2],
                          ["square", 1],
                          ["ds9", 1],
                          ["triangle", 3],
                          ["square", 2],
                          ["blackHole", 1],
                          ["circle", 2]
            ]
        # Store shape, number of shapes, then color
        elif self.position == 1:
            self.wheel = [["triangle", 1, "red"],
                          ["circle", 3, "blue"],
                          ["quark", 1, None],
                          ["triangle", 3, "green"],
                          ["circle", 2, "red"],
                          ["triangle", 2, "green"],
                          ["square", 1, "blue"],
                          ["ds9", 1, None],
                          ["triangle", 3, "red"],
                          ["green", 2, "green"],
                          ["blackHole", 1, None],
                          ["circle", 2, "blue"],
                          ["square", 3, "red"],
                          ["swirl", 1, None],
                          ["circle", 1, "green"],
                          ["triangle", 3, "blue"],
                          ["circle", 1, "red"],
                          ["triangle", 1, "green"],
                          ["square", 2, "blue"],
                          ["ds9", 1, None],
                          ["square", 1, "red"],
                          ["square", 3, "blue"],
                          ["circle", 3, "green"],
                          ["square", 2, "red"],
                          ["blackHole", 1, None],
                          ["circle", 1, "blue"],
                          ["square", 3, "green"],
                          ["triangle", 2, "red"],
                          ["triangle", 1, "blue"],
                          ["swirl", 1, None],
                          ["circle", 3, "red"],
                          ["square", 1, "green"],
                          ["ds9", 1, None],
                          ["triangle", 2, "blue"],
                          ["blackHole", 1, None],
                          ["circle", 2, "green"]
            ]
        elif self.position == 2:
            # Store shape, number of shapes, then color
            self.wheel = [["blackHole", 1, None],
                          ["circle", 2, "green"],
                          ["triangle", 1, "red"],
                          ["circle", 3, "blue"],
                          ["quark", 1, None],
                          ["triangle", 3, "green"],
                          ["circle", 2, "red"],
                          ["triangle", 2, "green"],
                          ["square", 1, "blue"],
                          ["ds9", 1, None],
                          ["triangle", 3, "red"],
                          ["square", 2, "green"],
                          ["blackHole", 1, None],
                          ["circle", 2, "blue"],
                          ["square", 3, "red"],
                          ["swirl", 1, None],
                          ["circle", 1, "green"],
                          ["triangle", 3, "blue"],
                          ["circle", 1, "red"],
                          ["triangle", 1, "green"],
                          ["square", 2, "blue"],
                          ["ds9", 1, None],
                          ["square", 1, "red"],
                          ["square", 3, "blue"],
                          ["circle", 3, "green"],
                          ["square", 2, "red"],
                          ["blackHole", 1, None],
                          ["circle", 1, "blue"],
                          ["square", 3, "green"],
                          ["triangle", 2, "red"],
                          ["triangle", 1, "blue"],
                          ["swirl", 1, None],
                          ["circle", 3, "red"],
                          ["square", 1, "green"],
                          ["ds9", 1, None],
                          ["triangle", 2, "blue"]
            ]
        return self.wheel
    
    def buildWholeWheel(self):
        result = None * 3

        result[0] = self.buildOneWheel(0)
        result[1] = self.buildOneWheel(1)
        result[2] = self.buildOneWheel(2)

        return result