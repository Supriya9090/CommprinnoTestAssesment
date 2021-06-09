t = int(input())
while(t):
    store = {
        "b":"BattleShip",
        "c":"cruiser",
        "d":"destroyer",
        "f":"friate"
        }
    item  = input().lower()
    if item in store:
        print(store[item])
    t-=1