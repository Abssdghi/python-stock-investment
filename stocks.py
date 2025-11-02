import random

wallet = 1000

def stocks(count):
    result = []
    
    for i in range(count):
        Rate = random.choices(range(1, 101), weights=[0.5/i for i in range(1, 101)], k=1)[0]/100
        Probability = random.choices(range(1, 101), weights=[i for i in range(1, 101)], k=1)[0]/100
        stock = {}
        stock['rate'] = Rate
        stock['prob'] = Probability
        result.append(stock)
    
    return result


def Investment(wallet, rate, prob):
    random_number = random.choice(range(1,101))/100
    if (random_number<=prob):
        wallet+=wallet*rate
        print('+++')
    else:
        wallet-=wallet*rate
        print("---")

    return wallet


while (True):
    print()
    print('wallet : ',wallet)
    x=1
    my_stocks = stocks(3)

    while True:
        for i in my_stocks:
            print(f"{x}: {i['rate']*100}% Rate, {i['prob']*100}% Success ")
            x+=1
        
        s = int(input('Select option: '))
        money = int(input('Investment amount: '))
        
        if money > wallet:
            print("Error: Investment amount exceeds wallet balance!")
            x = 1
            continue
        
        break
    
    choice = my_stocks[s-1]
    wallet-=money
    wallet+=Investment(money, choice['rate'], choice['prob'])
    

    
        
    



