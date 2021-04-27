South_points=0
midwest_points=0
pacific_west_points=0
northeast_points=0
west_points=0
northeastcheck=0
westcheck=0
midwestcheck=0
pacificwestcheck=0
southcheck=0
finalregion=""
##setting up variables
import turtle

t=turtle.Turtle()
t.penup()
window=turtle.Screen()
window.setup(width=775 ,height=500)
window.bgpic('usamap.gif')
window.addshape('northeast.gif')
window.addshape('pacificnorthwest.gif')
window.addshape('south.gif')
window.addshape('midwest.gif')
window.addshape('west.gif')
##setting up turtle
def question1():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call the gray bug that turns into a ball when it is touched? \n 1: roly poly \n 2: pill bug \n 3: potato bug \n 4: No idea \n"))
    if answer == 1:
        South_points+=1
        west_points+=1
        pacific_west_points+=1
    if answer == 2:
        northeast_points+=1
    if answer==3:
        pacific_west_points+=1
    if answer==4:
        northeast_points+=1
def question2():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call the small lobster-like creature that is found in lakes and streams? \n 1: crayfish \n 2: crawfish \n 3: crawdad \n 4: No idea \n"))
    if answer == 1:
        northeast_points+=1
        midwest_points+=1
    if answer == 2:
        South_points+=1
        pacific_west_points+=1
    if answer==3:
        pacific_west_points+=1
    if answer==4:
        west_points+=1
def question3():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call the thing you drink water from at school? \n 1: water fountain \n 2: Drinking fountain \n 3: Bubbler \n"))
    if answer == 1:
        South_points+=1
        northeast_points+=1
        midwest_points+=1
    if answer == 2:
        pacific_west_points+=1
        west_points+=1
    if answer==3:
        midwest_points+=3
def question4():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("How do you pronounce caramel?  \n 1: keh-ruh-mel  \n 2: car-mul \n"))
    if answer == 1:
        northeast_points+=1
        South_points+=1
    if answer == 2:
        northeast_points+=1
        west_points+=1
        midwest_points+=1
        pacific_west_points+=1
def question5():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("Do you call coleslaw “slaw”?  \n 1:Yes  \n 2:No \n"))
    if answer == 1:
        South_points+=1
    if answer == 2:
        northeast_points+=1
        west_points+=1
        pacific_west_points+=1
        midwest_points+=1
def question6():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What would you say to address two or more people?  \n 1:you guys  \n 2:y'all  \n 3:you all  \n"))
    if answer == 1:
        northeast_points+=1
        west_points+=1
        midwest_points+=1
        pacific_west_points+=1
    if answer == 2:
        South_points+=1
    if answer==3:
        northeast_points+=1
def question7():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call a long sandwich with cold cuts and other sandwich ingredients on it?  \n 1:sub  \n 2:hoagie \n"))
    if answer == 1:
        west_points+=1
        midwest_points+=1
        pacific_west_points+=1
        South_points+=1
    if answer == 2:
        northeast_points+=3
def question8():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call rubber soled shoes usually worn for athletic activity?  \n 1:Tennis shoes  \n 2:sneakers  \n 3:Other \n"))
    if answer == 1:
        South_points+=1
        west_points+=1
        pacific_west_points+=1
        midwest_points+=1
    if answer == 2:
        northeast_points+=1
def question9():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call large roads meant for long distance travel that you are meant to drive fast on?  \n 1: Highway  \n 2: Freeway  \n 3: Other \n"))
    if answer == 1:
        northeast_points+=1
        west_points+=1
        South_points+=1
        midwest_points+=1
    if answer == 2:
        pacific_west_points+=1
        west_points+=1
def question10():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you use as a general term for soft drinks?  \n 1: Soda  \n 2: Coke  \n 3: Pop  \n 4: Other \n"))
    if answer == 1:
        northeast_points+=1
        pacific_west_points+=1
        west_points+=1
    if answer == 2:
        South_points+=1
    if answer==3:
        midwest_points+=1
def question11():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call the night before Halloween? \n 1: No special word for the night  \n 2: Devil's Night  \n 3: Mischief Night \n"))
    if answer == 1:
        pacific_west_points+=1
        South_points+=1
        west_points+=1
        northeast_points+=1
        midwest_points+=1
    if answer == 2:
        midwest_points+=2
    if answer==3:
        northeast_points+=2
def question12():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("How do you pronounce ''syrup''? \n 1: Sir-up  \n 2: Sear-up  \n 3:other  \n"))
    if answer == 1:
        pacific_west_points+=1
        South_points+=1
        west_points+=1
        northeast_points+=1
        midwest_points+=1
    if answer == 2:
        northeast_points+=2
def question13():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call the insect that flies around and lights up during the summer? \n 1: Firefly  \n 2: Lightning Bug \n"))
    if answer == 1:
        pacific_west_points+=1
        west_points+=1
        northeast_points+=1
    if answer == 2:
        midwest_points+=1
        northeast_points+=1
        South_points+=1
def question14():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("What do you call a large truck with 18 wheels? \n 1: Semi Truck \n 2: Tractor Trailer \n 3: 18 Wheeler \n"))
    if answer == 1:
        pacific_west_points+=1
        west_points+=1
        midwest_points+=1
        South_points+=1
    if answer == 2:
        northeast_points+=1
    if answer ==3:
        South_points+=1
def question15():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    answer=int(input("How do you pronounce ''mayonnaise''? \n 1: Man-aze  \n 2: May-uh-naze \n"))
    if answer == 1:
        South_points+=1
        pacific_west_points+=1
    if answer == 2:
        midwest_points+=1
        west_points+=1
        northeast_points+=1
##defining questions as functions, makes it look a lot cleaner
def midwestred():
    t.goto(90,80)
    t.shape('midwest.gif')
    t.stamp()
    t.shape('arrow')
def southred():
    t.goto(100,-80)
    t.shape('south.gif')
    t.stamp()
    t.shape('arrow')
def pacificwestred():
    t.goto(-300,32)
    t.shape('pacificnorthwest.gif')
    t.stamp()
    t.shape('arrow')
def westred():
    t.goto(-150,28)
    t.shape('west.gif')
    t.stamp()
    t.shape('arrow')
def northeastred():
    t.goto(290,150)
    t.shape('northeast.gif')
    t.stamp()
    t.shape('arrow')
##defining turtle functions for putting parts of map up
def mapcheck():
    global South_points
    global west_points
    global pacific_west_points
    global northeast_points
    global midwest_points
    global southcheck
    global westcheck
    global pacificwestcheck
    global northeastcheck
    global midwestcheck
    global finalregion
    regionpointlist=[]
    if southcheck<1:
        regionpointlist.append(South_points)
    if northeastcheck<1:
        regionpointlist.append(northeast_points)
    if westcheck<1:
        regionpointlist.append(west_points)
    if midwestcheck<1:
        regionpointlist.append(midwest_points)
    if pacificwestcheck<1:
        regionpointlist.append(pacific_west_points)
    if max(regionpointlist)!=South_points:
        southred()
        southcheck+=1
    if max(regionpointlist)!=west_points:
        westred()
        westcheck+=1
    if max(regionpointlist)!=midwest_points:
        midwestred()
        midwestcheck+=1
    if max(regionpointlist)!=northeast_points:
        northeastred()
        northeastcheck+=1
    if max(regionpointlist)!=pacific_west_points:
        pacificwestred()
        pacificwestcheck+=1
    finalregion=max(regionpointlist)
    
##function that checks the map for the region with lowest points and rules it out.
question1()
question2()
question3()
question4()
question5()
question6()
question7()
question8()
question9()
question10()
question11()
question12()
question13()
question14()
question15()
mapcheck()
if finalregion==northeast_points:
    print("You are from the Northeast region of the United States")
if finalregion==South_points:
    print("You are from the Southern region of the United States")
if finalregion==west_points:
    print("You are from the Western region of the United States")
if finalregion==midwest_points:
    print("You are from the Midwest region of the United States")
if finalregion==pacific_west_points:
    print("You are from the Pacific region of the United States")

t.goto(-200,-200)

