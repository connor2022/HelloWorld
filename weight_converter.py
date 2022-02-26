weight = int(input("Weight: ")) #asks for a weight and will turn it into a number rather than string
format = input("(K)g or (L)bs: ")
if(("L" in format) or ("l" in format)) == True: #tests if you typed either l or L
    print("Weight in Kg:", round(int(weight) * 0.453592)) #rounds the number (weight) and multiplies it by kg-lb ratio
    exit(0)
elif(("k" in format) or ("K" in format)) == True: #tests if you typed k or K
    print("Weight in Lbs:", round(int(weight) * 2.20462))
    exit(0)
else: #if you typed any letter of number other than k, K, l. L it will end
    print("u did not say anything right bro how")
