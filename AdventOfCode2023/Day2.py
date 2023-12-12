import re 


def main(): 
    sums = 0
    count =  1
    with open("Results.txt") as file:
        for line in file:
            passes = True 
            greenh = 0 
            redh = 0
            blueh = 0 
            ournumber = "" 
            #print(line)
            newline = line.rstrip()
            string = newline.find(': ')
            string = newline[string + 2:]
            print(string)
            string = string.replace('; ', ";")
            games = string.split(';')
            for i in games: 
                single = i.replace(', ', ',')
                single = i.split(', ')
                for j in single: 
                    if 'red' in j: 
                        c = j.split(' ')
                        if int(c[0]) > redh: 
                            redh = int(c[0])
                    if 'green' in j: 
                        c = j.split(' ')
                        if int(c[0]) > greenh: 
                            greenh = int(c[0])
                            
                    if 'blue' in j: 
                        c = j.split(' ')
                        if int(c[0]) > blueh: 
                            blueh = int(c[0])
            
            sums = sums + (blueh * greenh * redh)

            count = count + 1 
            print(sums)

if __name__ == '__main__': 
    main() 