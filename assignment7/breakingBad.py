def does_it_wrk(outfut, pairs):
    # Juts gona lookie for bad combies here
    for i in range(len(outfut)):
        for j in range(i+1, len(outfut)):
            combo1 = (outfut[i], outfut[j])
            combo2 = (outfut[j], outfut[i])
            if combo1 in pairs or combo2 in pairs:
                return False
    return True

def lets_give_it_a_go(idx, N, stuff_up_for_grabz, oopsie_daisies, waltz_stuff, jessz_stuff):
    if idx == N:
        if does_it_wrk(waltz_stuff, oopsie_daisies) and does_it_wrk(jessz_stuff, oopsie_daisies):
            return waltz_stuff, jessz_stuff
        else:
            return None, None
    
    # Toss this to Walt and see if its kool
    waltz_stuff.append(stuff_up_for_grabz[idx])
    w_things, j_things = lets_give_it_a_go(idx+1, N, stuff_up_for_grabz, oopsie_daisies, waltz_stuff, jessz_stuff)
    if w_things:
        return w_things, j_things
    waltz_stuff.pop()  
    
    # Lets try handin this to Jess then
    jessz_stuff.append(stuff_up_for_grabz[idx])
    w_things, j_things = lets_give_it_a_go(idx+1, N, stuff_up_for_grabz, oopsie_daisies, waltz_stuff, jessz_stuff)
    if w_things:
        return w_things, j_things
    jessz_stuff.pop()  

    return None, None

N = int(input())
all_the_things = [input().strip() for i in range(N)]
M = int(input())
bad_combos = set(tuple(input().split()) for i in range(M))

the_waltz_stuff, the_jessz_stuff = lets_give_it_a_go(0, N, all_the_things, bad_combos, [], [])

if the_waltz_stuff:
    print(" ".join(the_waltz_stuff))
    print(" ".join(the_jessz_stuff))
else:
    print("impossible")
