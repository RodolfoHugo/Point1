from Model.point import Point

def main(args=[]):

	P1 = Point(2,4)
	print(P1)

	P2 = Point(3,5)
	print(P2)

	P3 = (P1 + P2)
	print(P3)


if __name__ == '__main__':
	main()	
