if __name__ == "__main__":
    
    codigo=int(input('escriba el codigo completo: '))
    v=codigo%10
    n=codigo//10
    a=n%10
    n=n//10
    b=n%10
    n=n//10
    c=n%10
    d=n//10
    s=a*c+(b+d)
    vc=s%10
    if v==vc:
        z=1
    else:
        z=0
    print(z)
