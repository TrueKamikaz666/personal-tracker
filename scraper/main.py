from sources.monsterhigh.mattel import Mattel


sources = [

    Mattel()

]


monster_high = []


for source in sources:

    monster_high.append(

        source.run()

    )


print(monster_high)
