import numpy as np

# define range of WHT color in HSV
LOW_WHT = np.array([70,60,180])
UPP_WHT = np.array([90,110,200])
WHT = (LOW_WHT, UPP_WHT)
# define range of GRY color in HSV
LOW_GRY = np.array([80,80,150])
UPP_GRY = np.array([90,125,185])
GRY = (LOW_GRY, UPP_GRY)

# define range of BLK color in HSV
LOW_BLK = np.array([0,0,0])
UPP_BLK = np.array([180,255,65])
BLK = (LOW_BLK, UPP_BLK)

# define range of YLW color in HSV
LOW_YLW = np.array([26,215,136])
UPP_YLW = np.array([40,255,255])
YLW = (LOW_YLW, UPP_YLW)


# define range of ORG color in HSV
LOW_ORG = np.array([35,120,150])
UPP_ORG = np.array([45,215,195])
ORG = (LOW_ORG, UPP_ORG)

# define range of GRN color in HSV
LOW_GRN = np.array([80,210,150])
UPP_GRN = np.array([90,255,255])
GRN = (LOW_GRN, UPP_GRN)

# define range of RED color in HSV
LOW_RED = np.array([0,0,140])
UPP_RED = np.array([60,65,165])
RED = (LOW_RED, UPP_RED)

# define range of PNK color in HSV
LOW_PNK = np.array([95,0,160])
UPP_PNK = np.array([130,45,195])
PNK = (LOW_PNK, UPP_PNK)

# define range of COP color in HSV
LOW_COP = np.array([10,190,60])
UPP_COP = np.array([50,255,125])
COP = (LOW_COP, UPP_COP)

# define range of BWN color in HSV
LOW_BWN = np.array([40,60,70])
UPP_BWN = np.array([70,125,115]) 
BWN = (LOW_BWN, UPP_BWN)

# define range of BLU color in HSV
LOW_BLU = np.array([92,145,120])
UPP_BLU = np.array([100,205,155])
BLU = (LOW_BLU, UPP_BLU)


# Part configurations
test_003_31050_10 = (
	# Only 2 sections

	# Section 2
	(
		# First column
		((90,22), (120,50), BLU),
		((90,50), (120,80), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		# Second column
		((55,90), (85,120), GRN),
		((60,110), (90,140), RED),
		((55,130), (85,160), GRN),
		((60,150), (90,180), RED),
	),
	
	# Section 3
	(
		((90,20), (120,50), BLU),
		((90,35), (120,65), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		((80,80), (110,110), GRN),
		((90,100), (120,130), RED),
		((90,115), (120,145), GRN),
		((85,145), (115,175), RED),
	)

)


test_003_31049_10 = (
	# Only 2 sections

	# Section 1
	(
		# First column (far right)
		((155,90), (185,115), BLK),
		((160,125), (185,155), WHT)
	),
	# Section 2
	(
		# First column
		((90,22), (120,50), BLU),
		((90,50), (120,80), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		# Second column
		((55,90), (85,120), GRN),
		((60,110), (90,140), RED),
		((55,130), (85,160), GRN),
		((60,150), (90,180), RED),
	),
	
	# Section 3
	(
		((90,20), (120,50), BLU),
		((90,35), (120,65), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		((80,80), (110,110), GRN),
		((90,100), (120,130), RED),
		((90,115), (120,145), GRN),
		((85,145), (115,175), RED),
	)

)


test_003_31048_10 = (
	# Section 1
	(
		# First column (far right)
		((155,90), (185,115), BLK),
		((160,125), (185,155), WHT),
		
		# Second column
		((100,10), (130,40), YLW),
		((105,35), (135,65), BWN),
		((105,190), (135,220), BWN),
		((100,210), (130,240), YLW),
	
		# Third column
		((45,60), (75,90), ORG),
		((45,90), (75,120), GRY),
		((45,140), (75,170), GRY),
		((45,170), (75,200), ORG)
	),
	
	# Section 2
	(
		# First column
		((90,22), (120,50), BLU),
		((90,50), (120,80), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		# Second column
		((55,90), (85,120), GRN),
		((60,110), (90,140), RED),
		((55,130), (85,160), GRN),
		((60,150), (90,180), RED),
	),
	
	# Section 3
	(
		((90,20), (120,50), BLU),
		((90,35), (120,65), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		((80,80), (110,110), GRN),
		((90,100), (120,130), RED),
		((90,115), (120,145), GRN),
		((85,145), (115,175), RED),
	)

)


test_003_30466_10 = (
	# Section 1
	(
		# First column (far right)
		((155,90), (185,115), BLK),
		((160,125), (185,155), WHT),
		
		# Second column
		((100,10), (130,40), YLW),
		((105,35), (135,65), BWN),
		((105,190), (135,220), BWN),
		((100,210), (130,240), YLW),
	
		# Third column
		((45,60), (75,90), ORG),
		((45,90), (75,120), GRY),
		((45,140), (75,170), GRY),
		((45,170), (75,200), ORG)
	),
	
	# Section 2
	(
		# First column
		((90,22), (120,50), BLU),
		((90,50), (120,80), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		# Second column
		((55,90), (85,120), GRN),
		((60,110), (90,140), RED),
		((55,130), (85,160), GRN),
		((60,150), (90,180), RED),
	),
	
	# Section 3
	(
		((90,20), (120,50), BLU),
		((90,35), (120,65), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		((80,80), (110,110), GRN),
		((90,100), (120,130), RED),
		((90,115), (120,145), GRN),
		((85,145), (115,175), RED),
	)

)

# Office Part
test_003_31049_00 = (
	# Section 1
	(
		# First column (far right)
		((155,90), (185,115), BLK),
		((160,125), (185,155), WHT),
		
		# Second column
		((100,10), (130,40), YLW),
		((105,35), (135,65), BWN),
		((105,190), (135,220), BWN),
		((100,210), (130,240), YLW),
	
		# Third column
		((45,60), (75,90), ORG),
		((45,90), (75,120), GRY),
		((45,140), (75,170), GRY),
		((45,170), (75,200), ORG)
	),
	
	# Section 2
	(
		# First column
		((90,22), (120,50), BLU),
		((90,50), (120,80), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		# Second column
		((55,90), (85,120), GRN),
		((60,110), (90,140), RED),
		((55,130), (85,160), GRN),
		((60,150), (90,180), RED),
	),
	
	# Section 3
	(
		((90,20), (120,50), BLU),
		((90,35), (120,65), PNK),
		((90,185), (120,215), PNK),
		((90,215), (120,245), BLU),
		
		((80,80), (110,110), GRN),
		((90,100), (120,130), RED),
		((90,115), (120,145), GRN),
		((85,145), (115,175), RED),
	)

)
