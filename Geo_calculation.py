import Geometric as geo
print("Enter the choice")
print("1) Area of triangle")
print("2) Area of circle")
print("3) Area of rectangle")
print("4) Area of square")
print("5) Perimeter of triangle  ")
print("6) Perimeter of recatangle ")
print("7) Perimeter of square ")
print("8) circumfrence of circle ")
n = int(input())
match n:
    case 1:
        print("Enter the base and height")
        b = int(input())
        h = int(input())
        print(f"Area: {geo.Atri(b,h)}")
    case 2:
        print("Enter the radius")
        r = float(input())
        print(f"Area: {geo.Acircle(r)}")
    case 3:
               print("Enter the length and breath")
               l = float(input())
               b = float(input())
               
               print(f"Area: {geo.Arect(l,b)}")
    case 4:
        print("Enter the length")
        r = float(input())
        print(f"Area: {geo.Asqr(r)}")
    case 5:
        print("Enter the a, b, c")
        a = float(input())
        b = float(input())
        c = float(input())
        
        print(f"Perimeter: {geo.Ptri(a,b,c)}")
    case 6:
        print("Enter the length , breadth")
        l = float(input())
        b = float(input())
        print(f"Perimeter: {geo.Prect(l,b)}")
    case 7:
        print("Enter the length")
        l =  float(input())
        print(f"perimeter: {geo.Psqr(l)}")
    case 8:
        print("Enter the radius")
        c = float(input())
        print(f"Circumfrence: {geo.circumcircle(c)}")       

