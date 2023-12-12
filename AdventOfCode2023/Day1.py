



def main(): 
    sums = 0
    count =  0  
    with open("Results.txt") as file:
        for line in file:
            ournumber = "" 
            #print(line)
            newline = line.rstrip()
            print(newline)
            newline = converstring(newline)
            print(newline)
            for char in newline: 
                if char.isdigit(): 
                    #print(char)
                    ournumber = ournumber + str(char)
                    break 
            txt = newline [::-1]
            for char in txt: 
                if char.isdigit(): 
                    ournumber = ournumber + str(char)
                    break 
            print(ournumber)
            sums = sums + int(ournumber)
            count = count + 1 
            #if count > 6: 
            #    break 

        print(sums)


def converstring(x): 
    x = x.replace("one","o1e")
    x = x.replace("two","t2o")
    x = x.replace("three","t3e")
    x = x.replace("four","f4r")
    x = x.replace("five","f5e")
    x = x.replace("six","s6x")
    x = x.replace("seven", "s7n")
    x = x.replace("eight","e8t")
    x = x.replace("nine","n9e")
    return x 


if __name__ == '__main__': 
    main() 