#this is the checkpoint
#friends = { 
#    "Shane" : 10, 
#    "Samantha" : 9, 
#    "Shiloh" : 12, 
#    "Sean" : 11 
#}
#friends["Sebastian"] = 8
#friends.pop("Shiloh")
#print(friends)
#Dictionary of shapes challenge
#shapes = {
#"Triangle": 8,
#"Circle": 15,
#"Square": 10,
#"Rectangle" : 12
#}
#newsh = input("Input a new shape")
#newhi = int(input('Input the height'))
#shapes[newsh] = newhi
#print(shapes)
trees = { 
    "aspen" : 75, 
    "pine" : 82, 
    "maple" : 60, 
    "oak" : 65, 
    "willow" : 80, 
    "cottonwood" : 100 
}
tree = input('Which tree do you want to remove?')
trees.pop(tree)
print(trees)