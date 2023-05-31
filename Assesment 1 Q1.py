#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 22:12:01 2023

@author: zaneleakibo-betts
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 14:10:32 2023

@author: Stish
"""
import tkinter as tk

# tk._test()

window = tk.Tk()

hasPound = tk.BooleanVar()
has50p = tk.BooleanVar()
has20p = tk.BooleanVar()
has10p = tk.BooleanVar()
has5p = tk.BooleanVar()
has2p = tk.BooleanVar()
has1p = tk.BooleanVar()


window.title("Change Calculator")
# window.iconbitmap("changeicon.png")
window.configure(background='red')
window.geometry("600x400")

coins = {100,50,20,10,5,2,1}
#rCoins = list(coins)
#rCoins.sort(reverse=True)
##l_coins= list(coins)
##l_coins.sort(reverse=True)
def exitApp():
    print("Ending App...")
    window.destroy()

def change():
    # Get the change amount from the entry widget
    change_amount = int(lblCoinEntry.get())
    
    
    # Calculate the minimum coin change
    result = {}
    result = {}
    value = change_amount
    l_coins = list(coins)
    l_coins.sort(reverse=True)

    for coin in l_coins:
        result[coin] = value // coin
        value = value % coin

    # Display the minimum coin change
    result_str = ""
    for coin in coins:
        if coin in result:
            coin_name = f"{'£' if coin == 100 else str(coin)+'p'}"
            result_str += f"{coin_name:3} {result[coin]:2}\n"
    lblResult.configure(text=result_str)

def exclude(n):
    global coins
    global rCoins
    c ={100:hasPound.get(),
         50:has50p.get(),
         20:has20p.get(),
         10:has10p.get(),
         5:has5p.get(), 
          2:has2p.get(),
          1:has1p.get()
     }.get(n)
    print(f"{n}: {c}")
    if  c:
        coins = coins - {n}
    else:
        coins.add(n)
    print(f"Coins available {coins}")
    # <<Execute command 'change'>>
    

    
# Title
lblTitle =tk.Label(text="Change Machine...", 
                   font=('Time New Roman', 24,'bold'),
                   bg ='black',
                   fg='white') 
lblTitle.grid(row=0,column=0,columnspan=3,pady=(3,10))

#Entry
lblChangeReq =tk.Label(text="Change Required: ", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblChangeReq.grid(row=1,column=0, sticky=tk.W, padx=(5,5))

lblCoinEntry =tk.Entry(text="", 
                   font=('Time New Roman', 12,'bold') ) 
lblCoinEntry.grid(row=2,column=1,sticky=tk.W, columnspan=6,pady=(5,5) )

#Coin Availability
lblCoins_Not_Availability =tk.Label(text="Coins NOT Avalabile:", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblCoins_Not_Availability.grid(row=3,column=0,sticky=tk.W, pady=(5,2) )


cbPound = tk.Checkbutton(window, text="£1", variable=hasPound,
                         font=('Time New Roman', 12,'bold'),
                         bg ='yellow',
                         fg='red',
                         command= lambda: exclude(100))
cbPound.grid(row=3, column=1)
cb50p = tk.Checkbutton(window, text="50p", variable=has50p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='yellow',
                       fg='red',
                       command= lambda: exclude(50)) 
cb50p.grid(row=3, column=2)
cb20p = tk.Checkbutton(window, text="20p", variable=has20p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='yellow',
                       fg='red',
                       command= lambda: exclude(20)) 
cb20p.grid(row=3, column=3)
cb10p = tk.Checkbutton(window, text="10p", variable=has10p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='yellow',
                       fg='red',
                       command= lambda: exclude(10)) 
cb10p.grid(row=3, column=4)
cb5p = tk.Checkbutton(window, text="5p", variable=has5p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='yellow',
                       fg='red',
                       command= lambda: exclude(5)) 
cb5p.grid(row=3, column=5)

cb2p = tk.Checkbutton(window, text="2p", variable=has2p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='yellow',
                       fg='red',
                       command= lambda: exclude(2))
cb2p.grid(row=3, column=6)
cb1p = tk.Checkbutton(window, text="1p", variable=has1p,
                       font=('Time New Roman', 12,'bold'),
                       bg ='yellow',
                       fg='red',
                       command= lambda: exclude(1))
cb1p.grid(row=3, column=7)


#Result
lblBreakdown = tk.Label(text="Coin break down:", 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblBreakdown.grid(row=4,column=0)

lblResult = tk.Label(text='', 
                   font=('Time New Roman', 12,'bold'),
                   bg ='black',
                   fg='white') 
lblResult.grid(row=5,column=0)



# Exec button
btnExe = tk.Button(text="Exec", command=change, width=10,height=2)
btnExe.grid(row=7,column=6)

btnQuit = tk.Button(text="Quit", command=exitApp, width=10,height=2)
btnQuit.grid(row=8,column=6)


window.mainloop()
