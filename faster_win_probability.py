@memo
def Pwin3(me, you, pending):
       if me + pending >= goal:
           return 1
       elif you >= goal:
           return 0
       else:
            #P.Norvig version
            Proll = (1 - Pwin3(you, me + 1, 0) +
                    sum(Pwin3(me, you, pending+d) for d in (2,3,4,5,6)))/6.
            return (Proll if not pending else
                    max(Proll, 1- Pwin3(you,me+pending,0)))
            #other version
           #state = (0,me,you,pending)
           #return max(Q_pig(state, action, Pwin2)
            #          for action in pig_actions(state))