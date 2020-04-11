import random
capitals={'alabama':'montgomery','alaska':'juneau','arizona':'phoenix','arkansas':'little rock',
          'california':'sacremento','colorado':'denver','connecticut':'hartford','delaware':'dover','florida':'tallahassee',
          'georgia':'atlanta','hawaii':'honolulu','idaho':'boise','illinois':'springfield','indiana':'indianapolis',
          'iowa':'des moines','kansas':'topeka','kentucky':'frankfort','louisiana':'baton rogue','maine':'augusta',
          'maryland':'annapolis','massachussetts':'boston','michigan':'lansing','minnesota':'saint paul','mississippi':'jackson',
          'missouri':'jefferson city','montana':'helena','nebraska':'lincoln','nevada':'carson city','new hampshire':'concord',
          'new jersey':'trenton','new mexico':'santa fe','new york':'albany','north carolina':'raleigh','north dakota':'bismarck',
          'ohio':'columbus','oklahoma':'oklahoma city','oregon':'salem','pennysylvania':'harrisburg','rhode island':'providence',
          'south carolina':'columbia','south dakota':'pierre','tennessee':'nashville','texas':'austin','utah':'salt lake city',
          'vermont':'montpelier','virginia':'richmond','washington':'olympia','west virginia':'charleston','wisconsin':'madison','wyoming':'cheyenne'}
for quiznum in range(5):
    #create the quiz and answer key files
    quizfile=open('capitalsquiz%s.txt' %(quiznum+1),'w')
    answerkeyfile=open('capitalsquiz_answers%s.txt' %(quiznum+1),'w')


    #write out the header for the quiz
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((''*20)+ 'state capitals quiz (form %s)' % (quiznum+1))
    quizfile.write('\n\n')

    #shuffle the order of states
    states=list(capitals.keys())
    random.shuffle(states)

    #loop through all states ,making a question for each
    for questionnum in range(50):
        #get right and wrong answers
        correctanswer=capitals[states[questionnum]]
        wronganswers=list(capitals.values())
        del wronganswers[wronganswers.index(correctanswer)]
        wronganswers=random.sample(wronganswers,3)
        answeroptions=wronganswers+[correctanswer]
        random.shuffle(answeroptions)

        #loop through all 50 states,making a question for each
   # for questionnum in range(50):
        #write the question and answer options to quiz file
        quizfile.write('%s. what is the capital of %s?\n' %(questionnum+1,states[questionnum]))
        for i in range(4):
            quizfile.write('  %s.%s\n' %('abcd'[i],answeroptions[i]))
        quizfile.write('\n')

            #write the anser key to a file
        answerkeyfile.write('%s-%s\n' %(questionnum+1,'abcd'[answeroptions.index(correctanswer)]))
quizfile.close()
answerkeyfile.close()
